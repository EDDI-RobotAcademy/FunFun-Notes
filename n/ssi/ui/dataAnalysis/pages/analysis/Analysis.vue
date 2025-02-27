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
    </v-card>
  </v-container>
</template>

<script>
import { useDataAnalysisStore } from "~/dataAnalysis/stores/dataAnalysisStore";

export default {
  data() {
    return {
      selectedFile: null, // 선택한 파일을 저장
    };
  },
  methods: {
    async uploadFile() {
      const dataAnalysisStore = useDataAnalysisStore();
      if (!this.selectedFile) {
        this.$toast.error("Please select a file first.");
        return;
      }
      try {
        await dataAnalysisStore.requestDataAnalysis(this.selectedFile); // Pinia 액션 호출
        this.$toast.success("File uploaded successfully!");
      } catch (error) {
        console.error("Error uploading file:", error);
        this.$toast.error("File upload failed.");
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
