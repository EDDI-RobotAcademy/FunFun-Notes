<template>
  <v-container>
    <h2>안녕 Nuxt3 TypeScript 기반 Game Software List</h2>
    
    <!-- 상품 등록 링크 -->
    <div style="text-align: left; margin: 15px;">
      <NuxtLink :to="{ name: 'ProductRegisterPage' }">게임 소프트웨어 등록</NuxtLink>
    </div>
    
    <!-- 상품 목록 -->
    <v-row v-if="productList.length > 0">
      <v-col v-for="(product, index) in productList" :key="index" sm="6">
        <v-card @click="goToProductReadPage(product.productId)">
          <v-img :src="getProductImageUrl(product.productImage)" aspect-ratio="1" class="grey lighten-2">
            <template v-slot:placeholder>
              <v-row class="fill-height ma-0" align="center" justify="center">
                <v-progress-circular indeterminate color="grey lighten-5"/>
              </v-row>
            </template>
          </v-img>
          <v-card-title>{{ product.productName }}</v-card-title>
          <v-card-subtitle>{{ product.productPrice }}</v-card-subtitle>
        </v-card>
      </v-col>
    </v-row>

    <!-- 상품이 없을 경우 안내 메시지 -->
    <v-row v-else>
      <v-col cols="12" class="text-center">
        <v-alert type="info">등록된 게임 소프트웨어가 없습니다!</v-alert>
      </v-col>
    </v-row>

    <!-- 이미지 배너 -->
    <v-row>
      <v-col cols="12" class="text-center">
        <v-img src="@/assets/images/fixed/mario.jpg" aspect-ratio="1" class="grey lighten-2">
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
// import { useGameSoftwareStore } from '../../stores/gameSoftwareStore' // Pinia store 가져오기
import { useRouter } from 'vue-router'

// Pinia store
// const productStore = useProductStore()

// 상품 목록 가져오기
// const productList = computed(() => productStore.productList)

// 라우터 설정
const router = useRouter()

// 상품 이미지 URL을 반환하는 함수
const getProductImageUrl = (imageName: string) => {
  return require('@/assets/images/uploadImages/' + imageName)
}

// 상품 상세 페이지로 이동하는 함수
const goToProductReadPage = (productId: string) => {
  router.push({
    name: 'ProductReadPage',
    params: { productId },
  })
}

// 컴포넌트 마운트 시 상품 목록 요청
onMounted(() => {
//   productStore.requestProductListToDjango()
})
</script>

<style scoped>
.btn-text {
  color: white;
}
</style>
