import { defineStore } from "pinia";
import { kakaoAuthenticationState } from "./kakaoAuthenticationState";
import { kakaoAuthenticationAction } from "./kakaoAuthenticationAction";

export const useKakaoAuthenticationStore = defineStore('kakaoAuthenticationStore', {
    state: kakaoAuthenticationState,
    actions: kakaoAuthenticationAction,
})