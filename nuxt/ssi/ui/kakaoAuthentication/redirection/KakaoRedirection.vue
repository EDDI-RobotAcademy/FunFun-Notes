<template>
    <div></div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'

const accountStore = useAccountStore()
const kakaoAuthenticationStore = useKakaoAuthentication()

const router = useRouter()
const route = useRoute()

const setRedirectKakaoData = async() => {
    const code = route.query.code

    const isEmailDuplication = await kakaoAuthenticationStore.requestKakaoLoginToDjango({ email })

    if (isEmailDuplication === true) {
        console.log('이미 가입한 회원입니다!')
    } else {
        console.log('새로 가입이 필요한 회원입니다.')
    }
}

onMounted(async () => {
    await setRedirectKakaoData()
})
</script>