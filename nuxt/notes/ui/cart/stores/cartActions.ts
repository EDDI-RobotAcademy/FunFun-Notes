import * as axiosUtility from "../../utility/axiosInstance"
import { Cart } from "./cartType"

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
    async requestCartSave(requestForm: { id: number, userToken: string, quantity: number }) {
        const { djangoAxiosInstance } = axiosUtility.createAxiosInstances()

        const cart = {
            id: requestForm.id,
            quantity: requestForm.quantity,
        };

        try {
            const response = await djangoAxiosInstance.post("/cart/create", {
                cart: cart, userToken: requestForm.userToken
            });
            console.log("서버에 장바구니 저장 성공:", response.data.success);
            return response.data.success
        } catch (error) {
            console.error("서버에 장바구니 저장 실패:", error);
            this.cartList = this.cartList.filter(
                (item) => item.cartId !== cart.id
            );

            throw error;
        }
    }
}