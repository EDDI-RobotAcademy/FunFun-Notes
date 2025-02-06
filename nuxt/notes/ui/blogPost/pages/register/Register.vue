<template>
  <client-only>
    <v-container>
      <v-card>
        <v-card-title>블로그 포스트 작성</v-card-title>
        <v-card-text>
          <v-text-field v-model="title" label="제목" outlined></v-text-field>

          <!-- QuillEditor가 동적으로 로드되고 사용되도록 client-only 내부에 배치 -->
          <div class="editor-container" v-if="QuillEditor">
            <QuillEditor v-model:content="content" :options="editorOptions" toolbar="full" />
          </div>

          <v-btn color="primary" class="mt-3" @click="submitPost">등록</v-btn>
        </v-card-text>
      </v-card>
    </v-container>
  </client-only>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";
import { useRuntimeConfig, useNuxtApp } from "nuxt/app";
import { useBlogPostStore } from "~/stores/blogPostStore";
import "@vueup/vue-quill/dist/vue-quill.snow.css"; // ✅ 스타일 유지

const title = ref("");
const content = ref("");
const router = useRouter();
const config = useRuntimeConfig();
const blogPostStore = useBlogPostStore();
const editorOptions = ref({
  theme: "snow",
  placeholder: "Write here...",
});

// QuillEditor 컴포넌트 동적 로딩을 위한 상태 변수
const QuillEditor = ref(null);

// 🚀 클라이언트에서만 QuillEditor 등록
onMounted(async () => {
  const { QuillEditor: LoadedQuillEditor } = await import("@vueup/vue-quill");
  QuillEditor.value = LoadedQuillEditor;
});

// 블로그 포스트 제출
const submitPost = async () => {
  if (!title.value || !content.value) {
    alert("제목과 내용을 입력하세요.");
    return;
  }

  await blogPostStore.createPost({ title: title.value, content: content.value });
  alert("블로그 포스트가 등록되었습니다!");
  router.push("/blog/list");
};
</script>

<style scoped>
:deep(.ql-editor) {
  min-height: 200px;
}
:deep(.ql-toolbar.ql-snow) {
  border-top-left-radius: 5px;
  border-top-right-radius: 5px;
}
:deep(.ql-container.ql-snow) {
  border-bottom-left-radius: 5px;
  border-bottom-right-radius: 5px;
}
</style>
