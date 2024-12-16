import * as axiosUtility from "../../utility/axiosInstance"

export const kakaoAuthenticationAction = {
    async requestKakaoLoginToDjango(): Promise<void> {
        const { djangoAxiosInstance } = axiosUtility.createAxiosInstances()

        try {
            return djangoAxiosInstance.get('/kakao-oauth/kakao').then((res) => {
                console.log(`res: ${res}`)
                window.location.href = res.data.url
            })
        } catch (error) {
            console.log('requestKakaoOauthRedirectionToDjango() 중 에러:', error)
        }
    }
}