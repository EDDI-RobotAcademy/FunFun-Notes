import * as axiosUtility from "../../utility/axiosInstance"

export const cartAction = {
    async requestCartList(page: number = 1, perPage: number = 10): Promise<void> {
        const { djangoAxiosInstance } = axiosUtility.createAxiosInstances()

        try {
            const res = await djangoAxiosInstance.get('/cart/list', {
                params: { page, perPage }
            })
            console.log('Response Data:', res.data)

            this.cartList = res.data.dataList
            this.totalPages = res.data.totalPages
            this.currentPage = page
        } catch (error) {
            console.log('requestGameSoftwareList() 중 에러:', error)
        }
    },
}