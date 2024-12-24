<template>
  <!-- Game Software 상세 정보 표시 페이지 -->
  <v-container>
    <div style="text-align: left; margin: 15px;">
      <!-- 이전 페이지로 돌아가는 링크 -->
      <NuxtLink :to="{ name: 'GameSoftwareList' }">⬅️ 목록으로 돌아가기</NuxtLink>
    </div>

    <!-- 로딩 중일 때 스피너 표시 -->
    <v-row v-if="isLoading">
      <v-col cols="12" class="text-center">
        <v-progress-circular indeterminate color="grey lighten-5"/>
      </v-col>
    </v-row>

    <!-- 게임 소프트웨어 상세 정보 표시 -->
    <v-row v-else>
      <v-col cols="12" md="6">
        <!-- 이미지 표시 -->
        <v-img :src="getGameSoftwareImageUrl(gameSoftware.image)" aspect-ratio="1" class="grey lighten-2">
          <template v-slot:placeholder>
            <v-row class="fill-height ma-0" align="center" justify="center">
              <v-progress-circular indeterminate color="grey lighten-5"/>
            </v-row>
          </template>
        </v-img>
      </v-col>

      <v-col cols="12" md="6">
        <!-- 상세 정보 표시 -->
        <h2>{{ gameSoftware.title }}</h2>
        <p><strong>가격:</strong> {{ gameSoftware.price }}</p>
        <p><strong>설명:</strong> {{ gameSoftware.description }}</p>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import { useGameSoftwareStore } from '../../stores/gameSoftwareStore';

interface ImageModule {
  default: string;
}

const gameSoftwareStore = useGameSoftwareStore();
const route = useRoute();
const gameSoftwareId = route.params.id
console.log(`현재 읽은 id: ${gameSoftwareId}`)

const isLoading = ref(true);
const gameSoftware = ref({
  id: '',
  title: '',
  price: '',
  description: '',
  image: '',
});

const images = import.meta.glob('@/assets/images/uploadImages/*', { eager: true }) as Record<string, ImageModule>;

const getGameSoftwareImageUrl = (imageName: string) => {
  const imagePathKey = `/assets/images/uploadImages/${imageName}`;
  const imagePath = images[imagePathKey];
  return imagePath ? imagePath.default : '/assets/images/default-image.jpg';
};

onMounted(async () => {
  const { id } = route.params;

  const software = await gameSoftwareStore.requestGameSoftwareById(id as string);
  if (software) {
    gameSoftware.value = software;
  }
  isLoading.value = false;
});
</script>

<style scoped>
</style>