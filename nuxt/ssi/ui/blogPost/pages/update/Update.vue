<template>
    <client-only>
        <v-container>
            <v-card>
                <v-card-title>블로그 포스트 수정</v-card-title>
                <v-card-text>
                    <v-text-field v-model="title" label="제목" outlined></v-text-field>

                    <div class="editor-container" v-if="QuillEditor">
                        <QuillEditor
                            v-model="content"
                            :options="editorOptions"
                            toolbar="full"
                            ref="quillEditorRef"
                        />
                    </div>

                    <v-card-actions class="justify-end">
                        <v-btn color="primary" class="mt-3" @click="submitPost">저장</v-btn>
                        <v-btn color="secondary" class="mt-3" @click="goBack">취소</v-btn>
                    </v-card-actions>
                </v-card-text>
            </v-card>
        </v-container>
    </client-only>
</template>

<script setup lang="ts">
import { ref, onMounted, nextTick } from "vue";
import { useRoute, useRouter } from "vue-router";
import { useBlogPostStore } from "~/stores/blogPostStore";
import { createAwsS3Instance, getSignedUrlFromS3 } from '~/utility/awsS3Instance';
import { v4 as uuidv4 } from 'uuid';
import { compressHTML } from '~/utility/compression'; // ✅ HTML 압축 유틸리티 추가
import { useRuntimeConfig } from "nuxt/app";
import "@vueup/vue-quill/dist/vue-quill.snow.css";

const title = ref("");
const content = ref("");
const router = useRouter();
const route = useRoute();
const blogPostStore = useBlogPostStore();
const editorOptions = ref({
    theme: "snow",
    placeholder: "Write here...",
});

const QuillEditor = ref(null);
const quillEditorRef = ref(null);

const config = useRuntimeConfig();

onMounted(async () => {
    console.log("Mounted: Dynamically loading QuillEditor...");
    const { QuillEditor: LoadedQuillEditor } = await import("@vueup/vue-quill");
    QuillEditor.value = LoadedQuillEditor;
    console.log("Mounted: QuillEditor loaded successfully.");

    const postId = route.params.id;
    const statePost = history.state.post;  // ✅ 전달된 데이터 확인

    if (statePost) {
        console.log("Already has post data")
        // ✅ Read에서 받은 데이터 사용 (S3 요청 X)
        title.value = statePost.title;
        content.value = statePost.content;
        nextTick(() => {
            const quillInstance = quillEditorRef.value?.getQuill();
            if (quillInstance) {
                quillInstance.root.innerHTML = content.value;
            }
        });
    } else if (postId) {
        console.log("Need to acquire post data")
        // ❌ 만약 state 데이터가 없으면 (새로고침 등), S3에서 가져옴
        const data = await blogPostStore.requestReadPost(postId);
        if (data) {
            title.value = data.title;
            const url = await getSignedUrlFromS3(`blog-post/${data.content}`);
            const response = await fetch(url);
            content.value = await response.text();
            nextTick(() => {
                const quillInstance = quillEditorRef.value?.getQuill();
                if (quillInstance) {
                    quillInstance.root.innerHTML = content.value;
                }
            });
        }
    }
});

const slugify = (str: string) => {
    return str
        .toLowerCase()
        .replace(/[^\w\s-]/g, "")
        .replace(/[\s_-]+/g, "-")
        .replace(/^-+|-+$/g, "");
};

const uploadToS3 = async (content: string, title: string) => {
    const s3Client = createAwsS3Instance();
    const uniqueId = uuidv4(); // 고유 ID 생성
    const filename = `${slugify(title)}-${uniqueId}.html`;

    const params = {
        Bucket: config.public.AWS_BUCKET_NAME,
        Key: `blog-post/${filename}`,
        Body: content,
        ContentType: "text/html",
    };

    console.log("📝 S3 Upload Params:", params);

    try {
        const data = await s3Client.send(new PutObjectCommand(params));
        console.log("✅ Content uploaded to S3:", data);
        return filename;
    } catch (err) {
        console.error("❌ Error uploading content to S3", err);
        throw new Error("S3 업로드 실패");
    }
};

const submitPost = async () => {
    console.log("🚀 Submit post started...");

    if (!title.value || !content.value) {
        alert("제목과 내용을 입력하세요.");
        return;
    }

    await nextTick(async () => {
        const quillInstance = quillEditorRef.value?.getQuill();
        if (!quillInstance) {
            console.error("❌ Quill instance is not available.");
            return;
        }

        const contentHtmlString = quillInstance.root.innerHTML;
        console.log("📄 HTML content to upload:", contentHtmlString);

        if (!contentHtmlString) {
            console.error("❌ Failed to extract content from QuillEditor.");
            return;
        }

        const compressedHTML = await compressHTML(contentHtmlString);
        console.log("📄 압축된 HTML:", compressedHTML);

        try {
            // 기존 파일명 사용하여 덮어쓰기
            const filename = content.value;  // 기존 S3 파일명을 그대로 사용
            console.log("📝 S3 Upload Params:", filename);

            await uploadToS3(compressedHTML, filename);  // 업로드 시 기존 파일명 사용

            // 게시글 수정 요청
            await blogPostStore.requestUpdatePost({
                id: route.params.id,
                title: title.value,
            });

            alert("블로그 포스트가 수정되었습니다!");
            router.push(`/blog-post/read/${route.params.id}`);
        } catch (error) {
            console.error("❌ 블로그 포스트 수정 실패:", error);
            alert("포스트 수정 중 오류가 발생했습니다.");
        }
    });
};

const goBack = () => {
    router.push(`/blog-post/read/${route.params.id}`);
};
</script>