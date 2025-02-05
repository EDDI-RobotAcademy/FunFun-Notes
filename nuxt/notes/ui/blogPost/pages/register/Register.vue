<template>
  <v-container>
    <v-card>
      <v-card-title>블로그 포스트 작성</v-card-title>
      <v-card-text>
        <v-text-field v-model="title" label="제목" outlined></v-text-field>

        <!-- 클라이언트 사이드에서만 QuillEditor를 로딩 -->
        <ClientOnly>
          <QuillEditor v-model="content" theme="snow" @image-added="uploadImage" />
        </ClientOnly>

        <v-btn color="primary" class="mt-3" @click="submitPost">등록</v-btn>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { useRuntimeConfig } from 'nuxt/app';
import { Upload } from '@aws-sdk/lib-storage';
import { createAwsS3Instance } from '~/utility/awsS3Instance';
import { useBlogPostStore } from '~/stores/blogPostStore';
import { QuillEditor } from '@vueup/vue-quill';
import '@vueup/vue-quill/dist/vue-quill.snow.css';

// 상태 및 컴포넌트 초기화
const title = ref('');
const content = ref('');  // QuillEditor에서 사용할 content

const router = useRouter();
const config = useRuntimeConfig();
const blogPostStore = useBlogPostStore();

// 이미지 업로드 핸들러
const uploadImage = async (file, callback) => {
  const s3Client = createAwsS3Instance();
  const fileKey = `blog_images/${file.name}`;

  try {
    const upload = new Upload({
      client: s3Client,
      params: {
        Bucket: config.public.AWS_BUCKET_NAME,
        Key: fileKey,
        Body: file,
        ContentType: file.type,
      },
    });

    await upload.done();
    const imageUrl = `https://${config.public.AWS_BUCKET_NAME}.s3.${config.public.AWS_REGION}.amazonaws.com/${fileKey}`;
    callback(imageUrl); // Quill에 이미지 URL 반환
  } catch (error) {
    console.error('이미지 업로드 실패:', error);
  }
};

// 블로그 포스트 제출 메서드
const submitPost = async () => {
  if (!title.value || !content.value) {
    alert('제목과 내용을 입력하세요.');
    return;
  }

  await blogPostStore.createPost({ title: title.value, content: content.value });
  alert('블로그 포스트가 등록되었습니다!');
  router.push('/blog/list');
};
</script>

<style scoped lang="css">
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
