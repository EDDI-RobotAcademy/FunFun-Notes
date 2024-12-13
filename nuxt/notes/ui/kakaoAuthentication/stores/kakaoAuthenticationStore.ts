import { defineStore } from "pinia";

export const useKakaoAuthenticationStore = defineStore('kakaoAuthenticationStore', {
    state: kakaoAuthenticationState,
    actions: kakaoAuthenticationAction,
})