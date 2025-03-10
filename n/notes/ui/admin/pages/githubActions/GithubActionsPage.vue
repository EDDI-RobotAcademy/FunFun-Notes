<template>
  <v-container>
    <v-row>
      <v-col cols="12">
        <v-card>
          <v-card-title>GitHub Actions 모니터링</v-card-title>
          <v-card-subtitle>실시간으로 CI/CD 상태를 확인하세요</v-card-subtitle>
          <v-divider></v-divider>
          <v-card-text>
            <!-- 리포지토리 선택 -->
            <v-select
              v-model="selectedRepo"
              :items="repositories"
              item-title="name"
              item-value="name"
              label="모니터링할 리포지토리 선택"
              outlined
            ></v-select>
            <v-btn color="primary" @click="fetchWorkflowRuns">데이터 새로고침</v-btn>
          </v-card-text>
          <v-divider></v-divider>
          <v-list>
            <v-list-item v-for="run in workflows" :key="run.id">
              <v-list-item-content>
                <v-list-item-title>
                  {{ run.name }} - {{ run.status }} ({{ run.conclusion || '진행 중' }})
                </v-list-item-title>
                <v-list-item-subtitle>
                  실행 시간: {{ formatDate(run.created_at) }}
                </v-list-item-subtitle>
              </v-list-item-content>
              <v-list-item-action>
                <v-btn icon @click="viewDetails(run.html_url)">
                  <v-icon>mdi-open-in-new</v-icon>
                </v-btn>
              </v-list-item-action>
            </v-list-item>
          </v-list>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from "vue";
import { useAdminStore } from "~/admin/stores/adminStore";

// Pinia 스토어 가져오기
const adminStore = useAdminStore();

// 선택된 리포지토리
const selectedRepo = ref<{ name: string; url: string } | null>(null);

// 두 저장소의 목록
const repositories = [
  { name: "Mashed-Potato-Frontend", url: "https://github.com/silenc3502/Mashed-Potato-Frontend" },
  { name: "Mashed-Potato-Data-Server", url: "https://github.com/silenc3502/Mashed-Potato-Data-Server" }
];

// 사용자의 토큰
const userToken = "your-user-token";

// 선택한 리포지토리의 워크플로우 데이터 필터링
const filteredWorkflows = computed(() => {
  return adminStore.workflows.filter(workflow => workflow.repoName === selectedRepo.value?.name);
});

// GitHub Workflow 데이터 가져오기
const fetchWorkflowRuns = async () => {
  if (!selectedRepo.value) {
    alert("리포지토리를 선택해 주세요.");
    return;
  }

  try {
    console.log(`🔄 ${selectedRepo.value.name}의 GitHub Workflow 데이터 요청`);
    await adminStore.requestGithubWorkflow(userToken, selectedRepo.value.url); // 🔥 repoUrl 추가
  } catch (error) {
    console.error("❌ fetchWorkflowRuns() 오류:", error);
  }
};

// 워크플로우 상세 페이지로 이동하는 함수
const viewDetails = (url: string) => {
  window.open(url, "_blank");
};

// 날짜 포맷을 사람이 읽기 좋은 형식으로 변환하는 함수
const formatDate = (dateString: string) => {
  return new Date(dateString).toLocaleString();
};

onMounted(() => {
  fetchWorkflowRuns();
});
</script>
