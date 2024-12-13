import * as axiosUtility from "../../utility/axiosInstance"

export const kakaoAuthenticationAction = {
    async requestKakaoOauthRedirectionToDjango(): Promise<void> {
        const { djangoAxiosInstance } = axiosUtility.createAxiosInstances()

        try {
            return djangoAxiosInstance.get('/kakao-oauth/kakao').then((res) => {
                window.location.href = res.data.url
            })
        } catch (error) {
            console.log('requestKakaoOauthRedirectionToDjango() 중 에러:', error)
        }
    }
}