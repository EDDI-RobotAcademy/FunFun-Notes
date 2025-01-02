<template>
  <v-container>
    <v-app>
      <NavigationBar />
      <v-main>
        <NuxtPage />
        <!-- NuxtPage 컴포넌트는 자동으로 pages/about.vue를
        렌더링합니다. 즉, 어떤 URL이 요청되든, 그에 해당하는 페이지가 자동으로
        로드되고 표시됩니다. 여기서는 pages의 index.vue로 로드-->
      </v-main>
    </v-app>
  </v-container>
</template>

<script setup></script>

<style scoped></style>
