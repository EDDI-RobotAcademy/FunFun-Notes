import * as axiosUtility from "../../utility/axiosInstance";
import { AxiosResponse } from "axios"
import { useAccountStore } from "./accountStore"

export const accountAction = {

	async requestEmail(userToken: string): Promise<any> {
        const { djangoAxiosInstance } = axiosUtility.createAxiosInstances();
        try {
          // userToken을 body로 보내기
          const res: AxiosResponse = await djangoAxiosInstance.post(
            "/account/email",
            { userToken } // userToken을 요청 바디로 전달
          );
          
          // 응답에서 이메일 추출
          return res.data.email;
        } catch (error) {
          console.error("requestEmail() axios 오류!", error);
          throw new Error("Failed to fetch email");
        }
    },
    async withdraw(userToken: string): Promise<void> {
        const { djangoAxiosInstance } = axiosUtility.createAxiosInstances();
        const accountStore = useAccountStore();

        try {
            // 회원 탈퇴 요청
            await djangoAxiosInstance.delete("/account/withdraw", {
                data: { userToken }, // DELETE 요청의 body로 userToken 전달
            });

            // Pinia 스토어의 사용자 정보 초기화
            accountStore.resetAccount();

        } catch (error) {
            console.error("withdraw() axios 오류!", error);
            throw new Error("Failed to withdraw account");
        }
    },
};