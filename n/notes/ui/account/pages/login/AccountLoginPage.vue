<template>
  <v-container fluid class="d-flex justify-center align-center pa-0" 
    :style="{ backgroundImage: `url(${loginBgImage})`, backgroundSize: 'cover', backgroundPosition: 'center', height: '100vh' }">
    <v-row justify="center" align="center" class="fill-height ma-0">
      <v-col cols="12" sm="8" md="6" class="text-center">
        <!-- 관리자 로그인 버튼 -->
        <v-btn class="admin-login-btn" @click="goToAdminLogin" block>
          관리자 로그인
        </v-btn>

        <!-- 카카오 로그인 버튼 -->
        <v-btn class="kakao-login-btn" @click="goToKakaoLogin" block>
          <!-- 카카오 로그인 -->
        </v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import loginBgImage from '@/assets/images/fixed/login_bg2.webp';
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { useKakaoAuthenticationStore } from '../../../kakaoAuthentication/stores/kakaoAuthenticationStore';

const router = useRouter();

// Pinia store 상태
const kakaoAuthentication = useKakaoAuthenticationStore();

// Kakao 로그인 함수
const goToKakaoLogin = async () => {
  await kakaoAuthentication.requestKakaoLoginToDjango();
};

// 관리자 로그인 함수 (예시)
const goToAdminLogin = () => {
  router.push('/account/admin-login');
};
</script>

<style scoped>
/* 로그인 및 회원가입 버튼 설정 */
.v-btn {
  width: 100%;
  height: 50px;
  margin: 1.3vh auto;
}

.introduction {
  color: rgb(255, 255, 255);
  word-break: break-word;
}

@media (max-width: 768px) {
  .v-btn {
    height: 45px; /* 모바일 환경에서는 높이를 줄임 */
  }
  .login_logo {
    height: 19vh;
  }
}

@media (max-width: 480px) {
  .v-btn {
    height: 33px; /* 작은 모바일 환경에서는 더 작게 설정 */
  }
  .login_logo {
    height: 13vh;
  }
  .introduction {
    white-space: pre-wrap;
  }
}

/* Kakao 로그인 버튼 설정 */
.kakao-login-btn {
  width: 100%;
  max-width: 300px; /* 최대 너비 설정 */
  height: 50px;
  background-image: url("@/assets/images/fixed/btn_login_kakao.png");
  background-size: contain;
  background-repeat: no-repeat;
  background-position: center;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #FFEA00;
  border-radius: 1.4vh;
  cursor: pointer;
  margin-top: 20px; /* 위쪽 버튼과의 간격 */
}

/* 관리자 로그인 버튼 스타일링 */
.admin-login-btn {
  width: 100%;
  max-width: 300px; /* 최대 너비 설정 */
  height: 50px;
  background-color: #4CAF50; /* 관리자 버튼 색상 */
  color: white;
  font-weight: bold;
  border-radius: 1.4vh;
  margin-bottom: 20px; /* 카카오 로그인 버튼과의 간격 */
  cursor: pointer;
}

.v-text-field input {
  background-color: transparent !important;
  color: black !important;
}

.v-label {
  color: black !important;
}

:deep(.v-label.v-field-label) {
  color: rgba(255, 255, 255, 0.8) !important;
}

:deep(.v-text-field input) {
  color: #fff;
}

:deep(.mdi-eye::before),
:deep(.mdi-eye-off::before) {
  color: rgba(255, 255, 255, 0.8) !important;
}

:deep(.v-messages__message) {
  color: rgb(0, 0, 255) !important;
  font-size: 12px;
}

:deep(.v-field--error:not(.v-field--disabled) .v-label.v-field-label) {
  color: rgba(0, 0, 255) !important;
}
</style>
