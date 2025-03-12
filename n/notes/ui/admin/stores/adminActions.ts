import * as axiosUtility from "../../utility/axiosInstance";
import { AxiosResponse } from "axios"

export const adminAction = {

	async requestGithubWorkflow({ userToken, repoUrl }: { userToken: string; repoUrl: string }): Promise<any> {
    const { djangoAxiosInstance } = axiosUtility.createAxiosInstances();
  
    try {
      console.log(`🔄 GitHub Workflow 요청: Repo=${repoUrl}`);
  
      const res: AxiosResponse = await djangoAxiosInstance.post(
        "/github-action-monitor/workflow",
        { userToken, repoUrl } // 🔥 userToken + repoUrl 함께 전송
      );
  
      console.log("✅ GitHub Workflow 응답:", res.data);

      const { workflowInfo } = res.data;
      console.log(`workflowInfo: ${workflowInfo}`);

      // 데이터 설정
      this.workflows = workflowInfo || [];        // workflows가 없으면 빈 배열
    } catch (error) {
      console.error("❌ requestGithubWorkflow() 오류:", error);
      throw new Error("Failed to fetch GitHub Workflow data");
    }
  },  
};