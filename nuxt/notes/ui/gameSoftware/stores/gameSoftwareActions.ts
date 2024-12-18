import * as axiosUtility from "../../utility/axiosInstance"

export const gameSoftwareAction = {
    async requestGameSoftwareList(page: number = 1, perPage: number = 12): Promise<void> {
        const { djangoAxiosInstance } = axiosUtility.createAxiosInstances()

        try {
            const res = await djangoAxiosInstance.get('/game-software/list', {
                params: { page, perPage }
            })
            console.log('Response Data:', res.data)

            this.productList = res.data
        } catch (error) {
            console.log('requestGameSoftwareList() 중 에러:', error)
        }
    },
    async requestCreateGameSoftware(imageFormData: FormData): Promise<void> {
        console.log(`requestCreateGameSoftware(): ${imageFormData}`)
        const { djangoAxiosInstance } = axiosUtility.createAxiosInstances()

        try {
            const res = await djangoAxiosInstance.post('/game-software/create', 
                imageFormData, {
                    headers: {
                        'Content-Type': 'multipart/form-data',
                    },
                },
            )
            console.log('Response Data:', res.data)

            this.productList = res.data
        } catch (error) {
            console.log('requestCreateGameSoftware() 중 에러:', error)
        }
    },
}