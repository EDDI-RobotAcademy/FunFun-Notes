<template>
  <v-container>
    <v-card>
      <v-card-title>이미지 등록</v-card-title>
      <v-card-text>
        <v-text-field v-model="title" label="갤러리 제목" outlined></v-text-field>

        <v-file-input 
          v-model="imageFile" 
          label="이미지 선택" 
          accept="image/*" 
          outlined 
          @change="previewImage"
        ></v-file-input>

        <v-img v-if="previewUrl" :src="previewUrl" class="mt-3" height="200px"></v-img>

        <v-btn color="primary" class="mt-3" @click="uploadImage">등록</v-btn>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { S3Client, PutObjectCommand } from '@aws-sdk/client-s3';
import { useImageGalleryStore } from '~/stores/imageGalleryStore';
import { useRuntimeConfig } from 'nuxt/app';

const config = useRuntimeConfig();
const router = useRouter();
const imageGalleryStore = useImageGalleryStore();

const title = ref('');
const imageFile = ref(null);
const previewUrl = ref(null);

const previewImage = (event) => {
  if (event && event.target.files.length > 0) {
    const file = event.target.files[0];
    previewUrl.value = URL.createObjectURL(file);
  }
};

const uploadImage = async () => {
  if (!title.value || !imageFile.value) {
    alert("제목과 이미지를 모두 입력하세요.");
    return;
  }

  const file = imageFile.value[0];
  const s3Client = new S3Client({
    region: config.public.AWS_REGION,
    credentials: {
      accessKeyId: config.public.AWS_ACCESS_KEY_ID,
      secretAccessKey: config.public.AWS_SECRET_ACCESS_KEY,
    },
  });

  const fileKey = `image_gallery/${file.name}`;

  const uploadParams = {
    Bucket: config.public.AWS_BUCKET_NAME,
    Key: fileKey,
    Body: file,
    ACL: 'public-read',
    ContentType: file.type,
  };

  try {
    const command = new PutObjectCommand(uploadParams);
    await s3Client.send(command);

    const imageUrl = `https://${config.public.AWS_BUCKET_NAME}.s3.${config.public.AWS_REGION}.amazonaws.com/${fileKey}`;
    console.log('S3 Upload Success:', imageUrl);

    await imageGalleryStore.registerImage({ title: title.value, imageUrl });

    alert("이미지가 성공적으로 등록되었습니다!");
    router.push('/image-gallery'); // 갤러리 페이지로 이동
  } catch (error) {
    console.error('S3 Upload Error:', error);
    alert("이미지 업로드 실패");
  }
};
</script>
