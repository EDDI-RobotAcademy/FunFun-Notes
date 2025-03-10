import * as axiosUtility from "../../utility/axiosInstance";
import { AxiosResponse } from "axios"

export const adminAction = {

	async requestGithubWorkflow(userToken: string): Promise<any> {
    const { djangoAxiosInstance } = axiosUtility.createAxiosInstances();
    try {
      // userToken을 body로 보내기
      const res: AxiosResponse = await djangoAxiosInstance.post(
        "/admin/github-workflow", // Django 서버에서 처리할 엔드포인트
        { userToken } // userToken을 요청 바디로 전달
      );
      
      // 응답에서 이메일 추출
      // Golang API에서 이메일을 받았다면 추가 처리
      return res.data.workflowInfo;
    } catch (error) {
      console.error("requestGithubWorkflow() axios 오류!", error);
      throw new Error("Failed to fetch GitHub Workflow data");
    }
  },
};