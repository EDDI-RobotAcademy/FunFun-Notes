<template>
    <v-app-bar app color="primary" dark>
        <v-btn @click="goToHome">
            <v-toolbar-title>SK Networks AI 8기 with EDDI</v-toolbar-title>
        </v-btn>
        <v-spacer></v-spacer>

        <v-menu close-on-content-click>
            <template v-slot:activator="{ props }">
                <v-btn color="white" v-bind="props">
                    <b>Just for Test</b>
                </v-btn>
            </template>
        </v-menu>

        <!-- v-if="!isAuthenticated"  -->
        <v-btn text @click="signIn" class="btn-text">
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

const signIn = () => {
  console.log('로그인 클릭')
  router.push('/account/login')
}

// 로그아웃 동작
const signOut = () => {
  console.log('로그아웃 클릭')
}
</script>
