<template>
    <!-- v-app-bar의 경우 Vuetify에서 App Bar를 정의함
         color="primary"는 기본 색상을 설정하고 dark로 텍스트 색상(흰색) 지정 -->
    <v-app-bar app color="primary" dark>
        <!-- v-btn은 Vuetify에서의 버튼
             @click="goToHome"을 통해 버튼 클릭 시 goToHome 동작 -->
        <v-btn @click="goToHome">
            <!-- v-toolbar-title을 통해 툴바 제목을 지정 -->
            <v-toolbar-title>SK Networks AI 8기 with EDDI</v-toolbar-title>
        </v-btn>
        <!-- 툴바에서 남은 공간을 차지해 다른 요소들이 오른쪽으로 밀리도록 만듬 -->
        <v-spacer></v-spacer>

        <!-- v-menu는 Vuetify에서 메뉴를 만들 때 사용
             메뉴 외부를 클릭하면 닫힘 (close-on-content-click) -->
        <v-menu close-on-content-click>
            <!-- v-slot:activator는 메뉴 버튼을 설정함 -->
            <template v-slot:activator="{ props }">
                <!-- v-btn을 통해 메뉴 버튼을 만들고
                     v-bind="props"로 메뉴 활성화 시점의 버튼의 동작을 연결함
                     현재 관점에선 Drop Down Menu 구성은 하지 않았음 -->
                <v-btn color="white" v-bind="props">
                    <b>Just for Test</b>
                </v-btn>
            </template>
        </v-menu>

        <v-btn text @click="goToGameSoftwareList" class="btn-text">
            <v-icon left>mdi-gamepad</v-icon>
            <span>게임 소프트웨어</span>
        </v-btn>

        <!-- v-if="!isAuthenticated"  -->
        <!-- 로그인 버튼 -->
        <v-btn text @click="signIn" class="btn-text">
            <!-- 아이콘 설정 (mdi-login은 로그인 아이콘) -->
            <v-icon left>mdi-login</v-icon>
            <span>로그인</span>
        </v-btn>
    </v-app-bar>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router'

const router = useRouter()

const goToHome = () => {
  router.push('/')
}

const goToGameSoftwareList = () => {
    router.push('/game-software/list')
}

// 기존 Domain/index.ts에 등록한 라우터 URL로 맵핑
const signIn = () => {
  console.log('로그인 클릭')
  router.push('/account/login')
}


const signOut = () => {
  console.log('로그아웃 클릭')
}
</script>