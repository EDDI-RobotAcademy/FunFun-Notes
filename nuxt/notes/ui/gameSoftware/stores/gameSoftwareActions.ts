import * as axiosUtility from "../../utility/axiosInstance"

export const gameSoftwareAction = {
    async requestKakaoLoginToDjango(): Promise<void> {
        const { djangoAxiosInstance } = axiosUtility.createAxiosInstances()

        try {
            return djangoAxiosInstance.get('/kakao-oauth/request-login-url').then((res) => {
                console.log(`res: ${res}`)
                window.location.href = res.data.url
            })
        } catch (error) {
            console.log('requestKakaoOauthRedirectionToDjango() 중 에러:', error)
        }
    },
    async requestAccessToken(code:string):Promise<void>{
        const { djangoAxiosInstance } = axiosUtility.createAxiosInstances();
        try{
            const response = await djangoAxiosInstance.post('/kakao-oauth/redirect-access-token', code)
            localStorage.setItem("userToken", response.data.userToken)
        } catch(error){
            console.log('Access Token 요청 중 문제 발생:', error)
            throw error
        }
    },
}