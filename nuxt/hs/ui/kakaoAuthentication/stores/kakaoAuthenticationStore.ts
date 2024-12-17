import { defineStore } from "pinia";
import { kakaoAuthenticationAction } from "./kakaoAuthenticationActions";
import { kakaoAuthenticationState } from "./kakaoAuthenticationState";

export const useKakaoAuthenticationStore = defineStore('kakaoAuthenticationStore', {
    state: kakaoAuthenticationState,
    actions: kakaoAuthenticationAction,
})