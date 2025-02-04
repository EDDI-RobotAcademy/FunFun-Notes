<template>
  <v-container>
    <v-row>
      <v-col cols="12">
        <v-card>
          <v-card-title>이미지 갤러리</v-card-title>
          <v-card-text>
            <!-- No images available message -->
            <div v-if="imageList.length === 0">
              <v-alert type="info">등록된 사진이 없습니다.</v-alert>
            </div>

            <!-- Display gallery if there are images -->
            <v-row v-else>
              <v-col
                v-for="(image, index) in imageList"
                :key="index"
                cols="12" sm="6" md="4"
              >
                <v-card>
                  <v-img :src="image.imageUrl" alt="Gallery Image" height="200px" />
                  <v-card-title>{{ image.title }}</v-card-title>
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
// npm install aws-sdk --save-dev
import { computed, onMounted } from 'vue';
import { useImageGalleryStore } from '~/stores/imageGalleryStore'; // Assuming Pinia store

const imageGalleryStore = useImageGalleryStore();

// Computed properties to get images and pagination data
const imageList = computed(() => imageGalleryStore.imageGalleryList);
const currentPage = computed({
  get: () => imageGalleryStore.currentPage,
  set: (page) => imageGalleryStore.requestImageList({ page, perPage: 10 }), // Set page and items per page
});
const totalPages = computed(() => imageGalleryStore.totalPages);

onMounted(async () => {
  await imageGalleryStore.requestImageList({ page: currentPage.value, perPage: 10 }); // Fetch image list on mount
});
</script>
