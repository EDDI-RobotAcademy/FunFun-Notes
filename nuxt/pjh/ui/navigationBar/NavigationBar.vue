<template>
    <!-- v-app-bar: Vuetify에서 제공하는 상단 바 컴포넌트로, 화면 상단에 고정될 App Bar를 만듭니다.
         app: Vuetify 레이아웃에서 상단 레이아웃을 차지한다는 의미.
         color="primary": Vuetify 테마에서 'primary' 색상을 사용.
         dark: 다크 모드(밝은 글자색) 스타일 적용. -->
    <v-app-bar app color="primary" dark>

        <!-- v-btn: Vuetify의 버튼 컴포넌트. @click="goToHome"로 클릭 시 goToHome 메서드 호출.
             안에 v-toolbar-title이 들어있어 버튼 클릭 시 홈으로 이동하면서, 제목 표시 역할 겸함. -->
        <v-btn @click="goToHome">
            <!-- v-toolbar-title: Vuetify의 툴바 제목 컴포넌트로, 상단 바의 타이틀 표시.
                 "SK Networks AI 8기 with EDDI"라는 문구를 표시. -->
            <v-toolbar-title>SK Networks AI 8기 with EDDI</v-toolbar-title>
        </v-btn>

        <!-- v-spacer: 공간을 채워넣는 Vuetify 컴포넌트로, 왼쪽 타이틀과 오른쪽 버튼 사이에 여백을 만들어서 양쪽 정렬. -->
        <v-spacer></v-spacer>

        <!-- v-menu: Vuetify 메뉴 컴포넌트. close-on-content-click: 메뉴 외부 클릭 시 닫힘.
             template v-slot:activator="{ props }": 클릭 가능한 영역을 정의하는 슬롯.
             이 예시에서는 "Just for Test" 버튼 클릭 시 메뉴가 나타날 수 있는 구조지만,
             내부 내용이 비어있으므로 현재는 동작 의미가 없음. -->
        <v-menu close-on-content-click>
            <template v-slot:activator="{ props }">
                <!-- props를 받아서 v-bind="props"로 버튼에 적용.
                     이 버튼 클릭 시 v-menu가 열리거나 닫힐 수 있음.
                     color="white": 버튼 색상 흰색, <b>Just for Test</b>: 버튼 안에 굵은 글씨 표시. -->
                <v-btn color="white" v-bind="props">
                    <b>Just for Test</b>
                </v-btn>
            </template>
        </v-menu>

        <!-- 아래는 조건을 걸 수도 있는 부분(주석됨). !isAuthenticated라면 로그인 버튼 보여주기 식으로 사용 가능.
             현재는 주석이고 바로 로그인 버튼만 존재한다. -->
        <!-- v-if="!isAuthenticated"  -->

        <!-- 로그인 버튼: text 속성으로 텍스트 형태의 버튼, @click="signIn"으로 클릭 시 signIn 메서드 호출.
             class="btn-text": 커스텀 클래스 적용 가능.
             v-icon left: 버튼 왼쪽에 아이콘 mdi-login 표시.
             <span>로그인</span>: "로그인"이라는 텍스트를 버튼에 표시. -->
        <v-btn text @click="signIn" class="btn-text">
            <v-icon left>mdi-login</v-icon>
            <span>로그인</span>
        </v-btn>

    </v-app-bar>
</template>


<script setup lang="ts">
import { useRouter } from 'vue-router'

const router = useRouter()

// goToHome 함수: 홈('/') 경로로 라우터 이동.
const goToHome = () => {
  router.push('/')
}

// signIn 함수: 로그인('/account/login') 경로로 라우터 이동, 콘솔에 "로그인 클릭" 출력.
const signIn = () => {
  console.log('로그인 클릭')
  router.push('/account/login')
}

// signOut 함수: 로그아웃 동작(현재는 콘솔 메시지만)
const signOut = () => {
  console.log('로그아웃 클릭')
}
</script>
