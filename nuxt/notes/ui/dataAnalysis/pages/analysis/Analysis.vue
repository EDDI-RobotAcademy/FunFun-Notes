<template>
  <v-container class="pa-4">
    <v-card elevation="2" class="pa-4">
      <v-card-title class="text-h5">File Upload</v-card-title>
      <v-card-text>
        <v-file-input
          v-model="selectedFile"
          label="Select a file"
          outlined
          dense
          prepend-icon="mdi-file-upload"
          accept=".xlsx,.xls,.csv"
        />
      </v-card-text>
      <v-card-actions>
        <v-btn
          :disabled="!selectedFile"
          color="primary"
          class="ml-auto"
          @click="uploadFile"
        >
          <v-icon left>mdi-cloud-upload</v-icon>
          Upload
        </v-btn>
      </v-card-actions>
      <v-divider class="my-4"></v-divider>
      <!-- 이미지가 있는 경우 표시 -->
      <v-img
        v-if="imageURL"
        :src="imageURL"
        alt="Analysis Graph"
        max-height="500"
        contain
      />
    </v-card>

    <!-- Snackbar -->
    <v-snackbar v-model="snackbar" :color="snackbarColor" timeout="3000">
      {{ snackbarMessage }}
      <template #action>
        <v-btn color="pink" text @click="snackbar = false">Close</v-btn>
      </template>
    </v-snackbar>
  </v-container>
</template>

<script>
import { useDataAnalysisStore } from "~/dataAnalysis/stores/dataAnalysisStore";

export default {
  data() {
    return {
      selectedFile: null, // 선택한 파일
      imageURL: null, // 표시할 이미지 URL
      snackbar: false, // Snackbar 표시 여부
      snackbarMessage: "", // Snackbar 메시지
      snackbarColor: "", // Snackbar 색상
    };
  },
  methods: {
    async uploadFile() {
      const dataAnalysisStore = useDataAnalysisStore();
      if (!this.selectedFile) {
        this.snackbarMessage = "Please select a file first.";
        this.snackbarColor = "error";
        this.snackbar = true;
        return;
      }
      try {
        const imageURL = await dataAnalysisStore.requestDataAnalysis(this.selectedFile); // Pinia 액션 호출
        this.imageURL = imageURL; // 이미지 URL 저장
        this.snackbarMessage = "File uploaded successfully!";
        this.snackbarColor = "success";
        this.snackbar = true;
      } catch (error) {
        console.error("Error uploading file:", error);
        this.snackbarMessage = "File upload failed.";
        this.snackbarColor = "error";
        this.snackbar = true;
      }
    },
  },
};
</script>

<style scoped>
.v-file-input {
  max-width: 400px;
}
</style>
