<template>
  <div></div>
  <!--ui상 표현할게 없음-->
</template>

<script setup>
import { onMounted } from "vue";
import { useRouter, useRoute } from "vue-router";

import { useAccountStore } from "../../account/stores/accountStore";
import { useKakaoAuthenticationStore } from "../../kakaoAuthentication/stores/kakaoAuthenticationStore";

const accountStore = useAccountStore();
const kakaoAuthenticationStore = useKakaoAuthenticationStore();

const router = useRouter();
const route = useRoute();

const setRedirectKakaoData = async () => {
  const code = route.query.code; //code값만 가져오기
  // 원하는 파라미터값 가져오는 방법=route.query.원하는 값
  await kakaoAuthenticationStore.requestAccessToken({ code });

  // const isEmailDuplication = await kakaoAuthenticationStore.requestKakaoLoginToDjango({ email })

  // if (isEmailDuplication === true) {
  //     console.log('이미 가입한 회원입니다!')
  // } else {
  //     console.log('새로 가입이 필요한 회원입니다.')
  // }
};

onMounted(async () => {
  await setRedirectKakaoData();
});
</script>
