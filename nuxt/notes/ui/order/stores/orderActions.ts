import * as axiosUtility from "../../utility/axiosInstance"

export const orderAction = {
  async requestCreateOrder(selectedCartItems, userToken) {
    const { djangoAxiosInstance } = axiosUtility.createAxiosInstances();

    // 요청 데이터 준비
    const requestForm = {
      items: selectedCartItems, // 선택된 장바구니 항목들
      userToken: userToken, // 사용자 인증 토큰
    };

    try {
      // 주문 생성 요청
      const response = await djangoAxiosInstance.post("/order/create", requestForm);

      // 요청 성공 여부 확인
      if (response.data.success) {
        console.log("주문 성공:", response.data);
        return { success: true, orderId: response.data.orderId };
      } else {
        console.error("주문 실패:", response.data.message);
        return { success: false, message: response.data.message };
      }
    } catch (error) {
      console.error("주문 생성 중 오류 발생:", error);
      return { success: false, message: "서버 오류로 인해 주문 생성에 실패했습니다." };
    }
  },
}