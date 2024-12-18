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
}