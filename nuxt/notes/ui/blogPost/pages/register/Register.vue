<template>
  <client-only>
    <v-container>
      <v-card>
        <v-card-title>블로그 포스트 작성</v-card-title>
        <v-card-text>
          <v-text-field v-model="title" label="제목" outlined></v-text-field>

          <!-- QuillEditor가 동적으로 로드되고 사용되도록 client-only 내부에 배치 -->
          <div class="editor-container" v-if="QuillEditor">
            <!-- QuillEditor 컴포넌트의 ref 설정 -->
            <QuillEditor 
              v-model:content="content" 
              :options="editorOptions" 
              toolbar="full" 
              ref="quillEditorRef" 
            />
          </div>

          <v-btn color="primary" class="mt-3" @click="submitPost">등록</v-btn>
        </v-card-text>
      </v-card>
    </v-container>
  </client-only>
</template>

<script setup lang="ts">
import { ref, onMounted, nextTick } from "vue";
import { useRouter } from "vue-router";
import { useBlogPostStore } from "~/stores/blogPostStore";
import { S3Client, PutObjectCommand } from "@aws-sdk/client-s3";
import "@vueup/vue-quill/dist/vue-quill.snow.css"; // ✅ 스타일 유지
import { useRuntimeConfig } from "nuxt/app";

import { createAwsS3Instance } from '~/utility/awsS3Instance';

const title = ref("");
const content = ref(""); // Content binding for Quill
const router = useRouter();
const blogPostStore = useBlogPostStore();
const editorOptions = ref({
  theme: "snow",
  placeholder: "Write here...",
});

const config = useRuntimeConfig();

const QuillEditor = ref(null); // QuillEditor component
const quillEditorRef = ref(null); // Ref to access Quill instance

// 🚀 클라이언트에서만 QuillEditor 등록
onMounted(async () => {
  console.log("Mounted: Dynamically loading QuillEditor...");
  const { QuillEditor: LoadedQuillEditor } = await import("@vueup/vue-quill");
  QuillEditor.value = LoadedQuillEditor;
  console.log("Mounted: QuillEditor loaded successfully.");
});

// 제목을 슬러그 형식으로 변환 (중복 처리)
const slugify = (str: string) => {
  return str
    .toLowerCase()
    .replace(/[^\w\s-]/g, "") // 특수 문자 제거
    .replace(/[\s_-]+/g, "-") // 공백 및 하이픈 처리
    .replace(/^-+|-+$/g, ""); // 양옆의 하이픈 제거
};

// S3에 콘텐츠 업로드
const uploadToS3 = async (content: string, filename: string) => {
  const s3Client = createAwsS3Instance()

  const params = {
    Bucket: config.public.AWS_BUCKET_NAME,
    Key: `blog-post/${filename}.html`,  // 슬러그화된 제목 사용
    Body: content,
    ContentType: "text/html",  // HTML 파일로 업로드
  };

  console.log("📝 S3 Upload Params:", params);  // ✅ 파라미터 출력 확인

  try {
    const data = await s3Client.send(new PutObjectCommand(params));
    console.log("Content uploaded to S3:", data);

    // ✅ 업로드 성공 후 fileKey 반환
    return `blog-post/${filename}.html`; 
  } catch (err) {
    console.error("Error uploading content to S3", err);
    throw new Error("S3 업로드 실패");
  }
};

// 블로그 포스트 제출
const submitPost = async () => {
  console.log("Submit post started...");

  if (!title.value || !content.value) {
    alert("제목과 내용을 입력하세요.");
    return;
  }

  await nextTick(async () => {
    const quillInstance = quillEditorRef.value?.getQuill();
    if (!quillInstance) {
      console.error("Quill instance is not available.");
      return;
    }

    const contentHtmlString = quillInstance.root.innerHTML;
    console.log("HTML content to upload:", contentHtmlString);  // ✅ content 확인

    if (!contentHtmlString) {
      console.error("Failed to extract content from QuillEditor.");
      return;
    }

    try {
      const filename = slugify(title.value);  // 제목을 슬러그화
      const fileKey = await uploadToS3(contentHtmlString, filename); // ✅ 파일명 적용
      console.log("File uploaded successfully, key:", fileKey); // ✅ 업로드 성공 로그

      // ✅ Django로 보낼 데이터 (버킷 주소 없이 파일 경로만)
      await blogPostStore.requestRegisterPost({ 
        title: title.value, 
        content: fileKey // ✅ "blog-post/title-uuid.html"만 보냄 
      });

      alert("블로그 포스트가 등록되었습니다!");
      router.push("/blog-post/list");
    } catch (error) {
      console.error("❌ 블로그 포스트 등록 실패:", error); // ✅ 실패한 경우 출력
      alert("포스트 등록 중 오류가 발생했습니다.");
    }
  });
};
</script>

<style scoped>
:deep(.ql-editor) {
  min-height: 200px;
}
:deep(.ql-toolbar.ql-snow) {
  border-top-left-radius: 5px;
  border-top-right-radius: 5px;
}
:deep(.ql-container.ql-snow) {
  border-bottom-left-radius: 5px;
  border-bottom-right-radius: 5px;
}
</style>
