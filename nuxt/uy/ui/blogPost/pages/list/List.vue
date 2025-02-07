<template>
  <v-container>
    <v-row>
      <v-col cols="12">
        <v-card>
          <v-card-title>
            블로그 포스트
            <v-btn color="primary" class="ml-3" @click="goToRegister">글 작성</v-btn>
          </v-card-title>
          <v-card-text>
            <!-- No posts available message -->
            <div v-if="postList.length === 0">
              <v-alert type="info">등록된 포스트가 없습니다.</v-alert>
            </div>

            <!-- Display posts if available -->
            <v-row v-else>
              <v-col
                v-for="(post, index) in postList"
                :key="index"
                cols="12" sm="6" md="4"
              >
                <v-card>
                  <v-img :src="post.thumbnailUrl" alt="Post Thumbnail" height="200px" />
                  <v-card-title>{{ post.title }}</v-card-title>
                </v-card>
              </v-col>
            </v-row>
            
            <!-- Pagination -->
            <v-pagination
              v-model="currentPage"
              :length="totalPages"
              class="mt-3"
            ></v-pagination>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { computed, onMounted, watchEffect } from 'vue';
import { useRouter } from 'vue-router';
import { useBlogPostStore } from '~/stores/blogPostStore'; // Pinia store

const blogPostStore = useBlogPostStore();
const router = useRouter();

const postList = computed(() => blogPostStore.blogPostList);
const currentPage = computed({
  get: () => blogPostStore.currentPage,
  set: (page) => blogPostStore.requestPostList({ page, perPage: 10 }),
});
const totalPages = computed(() => blogPostStore.totalPages);

const goToRegister = () => {
  router.push('/blog-post/register');
};

// 페이지 변경 감지하여 리스트 업데이트
watchEffect(() => {
  blogPostStore.requestPostList({ page: currentPage.value, perPage: 10 });
});

onMounted(async () => {
  await blogPostStore.requestPostList({ page: currentPage.value, perPage: 10 });
});
</script>
