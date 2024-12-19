<template>
  <!-- v-container는 화면 상 적정한 중앙 정렬을 위해 배치함
       일단 너무 따닥 따닥 붙어 있으면 보기 좋지 않음 -->
  <v-container>
    <h2>안녕 Nuxt3 TypeScript 기반 Game Software List</h2>
    
    <!-- 상품 등록 링크 -->
    <div style="text-align: left; margin: 15px;">
     <!-- name을 가지고 Nuxt 상의 라우터를 연결함
          즉 링크를 누르면 register 페이지가 구동됨(URL 이동) -->
     <NuxtLink :to="{ name: 'GameSoftwareRegisterPage' }">게임 소프트웨어 등록</NuxtLink>
    </div>
    
    <!-- 상품 목록 -->
    <!-- Data Server에 리스트를 요청하여 개수가 0보다 큰지 확인 -->
    <v-row v-if="gameSoftwareList.length > 0">
      <!-- 1개라도 존재한다면 리스트에서 요소를 하나씩 빼서 gameSoftware로 취급, index는 몇 번째인지 알림 -->
      <v-col v-for="(gameSoftware, index) in gameSoftwareList" :key="index" sm="6">
        <!-- card 형태의 구성으로 이미지 정보를 출력
             클릭 시 read 동작을 Data Server에 요청함 -->
        <v-card @click="goToGameSoftwareReadPage(gameSoftware.id)">
          <v-img :src="getGameSoftwareImageUrl(gameSoftware.image)" aspect-ratio="1" class="grey lighten-2">
            <!-- 이미지 로딩 중 빙글빙글 도는 부분이 추가됨(지연이 없다면 나타나지 않음) -->
<!--          <v-img :src="`@/assets/images/uploadImages/${gameSoftware.image}`" aspect-ratio="1" class="grey lighten-2" >-->
<!--          <v-img :src="getImageUrl(gameSoftware.image)" aspect-ratio="1" class="grey lighten-2">-->
            <template v-slot:placeholder>
              <v-row class="fill-height ma-0" align="center" justify="center">
                <v-progress-circular indeterminate color="grey lighten-5"/>
              </v-row>
            </template>
          </v-img>
          <!-- 게임 소프트웨어 타이틀 이름 -->
          <v-card-title>{{ gameSoftware.title }}</v-card-title>
          <!-- 가격 정보 -->
          <v-card-subtitle>{{ gameSoftware.price }}</v-card-subtitle>
        </v-card>
      </v-col>
    </v-row>

    <!-- 상품이 없을 경우 안내 메시지 -->
    <!-- 위쪽에 v-if 의 경우 조건을 만족한다면 아래는 신경쓰지 않음
         반면 if 조건이 만족되지 않으면 아래 코드가 대신 실행됨 -->
    <v-row v-else>
      <v-col cols="12" class="text-center">
        <v-alert type="info">등록된 게임 소프트웨어가 없습니다!</v-alert>
      </v-col>
    </v-row>

    <!-- 이미지 배너 -->
    <!-- 마리오 -->
    <v-row>
      <v-col cols="12" class="text-center">
        <v-img src="@/assets/images/fixed/고양이 사진.webp" aspect-ratio="1" class="grey lighten-2">
          <template v-slot:placeholder>
            <v-row class="fill-height ma-0" align="center" justify="center">
              <v-progress-circular indeterminate color="grey lighten-5"/>
            </v-row>
          </template>
        </v-img>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup lang="ts">

import { ref, computed, onMounted } from 'vue'
import { useGameSoftwareStore } from '../../stores/gameSoftwareStore'
import { useRouter } from 'vue-router'
import {resolve} from "path";

const gameSoftwareStore = useGameSoftwareStore()
const gameSoftwareList = computed(() => gameSoftwareStore.gameSoftwareList);

// 라우터 설정
const router = useRouter()

// 상품 이미지 URL을 반환하는 함수
const images = import.meta.glob('@/assets/images/uploadImages/*', { eager: true });
for (const [key, value] of Object.entries(images)) {
    console.log(`Key: ${key}`);
    console.log(`Value:`, value);
}

const getGameSoftwareImageUrl = (imageName: string) => {
    console.log(`imageName: ${imageName}`)
    console.log(`images[\`@/assets/images/uploadImages/${imageName}\`]`)
    console.log(`images: ${images}`)
    const imagePathKey = `/assets/images/uploadImages/${imageName}`
    console.log(`imagePathKey: ${imagePathKey}`)
    const imagePath = images[imagePathKey];
    console.log(`imagePath: ${imagePath.default}`)

    if (imagePath) {
        return imagePath.default;
    }
    return '/assets/images/default-image.jpg';
}

// 상품 상세 페이지로 이동하는 함수
// const goToGameSoftwareReadPage = (id: string) => {
//   router.push({
//     name: 'GameSoftwareReadPage',
//     params: { id },
//   })
// }

// 컴포넌트 마운트 시 상품 목록 요청
onMounted(() => {
  gameSoftwareStore.requestGameSoftwareList()
})
</script>

<style scoped>
.btn-text {
  color: white;
}
</style>