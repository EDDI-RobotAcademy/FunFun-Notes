<template>
    <v-container>
      <h2>안녕 Nuxt3 TypeScript 기반 Board App이야</h2>
      <div style="text-align: left; margin: 15px;">
        <!-- <NuxtLink :to="{ name: 'BoardRegisterPage' }">게시물 작성</NuxtLink> -->
      </div>
      
      <v-data-table
        v-model:items-per-page="perPage"
        :headers="headerTitle"
        :items="pagedItems"
        v-model:pagination="pagination"
        class="elevation-1"
        @click:row="readRow"
        item-value="boardId"
      />
      
      <v-pagination
        v-model="pagination.page"
        :length="totalPages"
        color="primary"
        @input="updateItems"
      />
    </v-container>
  </template>
  
  <script setup lang="ts">
  import { ref, computed, onMounted } from 'vue'
  import { useRouter } from 'vue-router'
  import { useBoardStore } from '~/board/stores/boardStore' // Pinia store 경로
  
  // Pinia store 가져오기
  const boardStore = useBoardStore()
  
  // 상태 및 변수 정의
  const perPage = ref(5)
  const pagination = ref({
    page: 1,
  })
  const headerTitle = [
    { title: 'No', align: 'start', sortable: true, key: 'boardId' },
    { title: '제목', align: 'end', key: 'title' },
    { title: '작성자', align: 'end', key: 'writer' },
    { title: '작성일자', align: 'end', key: 'regDate' },
  ]
  
  // 페이지 계산
  const totalPages = computed(() =>
    Math.ceil(boardStore.boardList.length / perPage.value)
  )
  
  // 현재 페이지에 맞는 데이터
  const pagedItems = computed(() => {
    const startIdx = (pagination.value.page - 1) * perPage.value
    const endIdx = startIdx + perPage.value
    return boardStore.boardList.slice(startIdx, endIdx)
  })
  
  // 게시물 상세 페이지 이동
  const readRow = (event: Event, { item }: { item: any }) => {
    const router = useRouter()
    router.push({
      name: 'BoardReadPage',
      params: { boardId: item.boardId.toString() },
    })
  }
  
  // 데이터 초기 로드
  onMounted(() => {
    boardStore.requestBoardList()
  })
  </script>
  
  <style scoped>
  /* 스타일 정의 */
  </style>