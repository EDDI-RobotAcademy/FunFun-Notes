import * as axiosUtility from "../../utility/axiosInstance";

export const boardAction = {
  async requestBoardList(page: number = 1, perPage: number = 8): Promise<void> {
    const { djangoAxiosInstance } = axiosUtility.createAxiosInstances();

    try {
      const res = await djangoAxiosInstance.get("/game-software/list", {
        params: { page, perPage },
      });
      console.log("Response Data:", res.data);

      this.gameSoftwareList = res.data.dataList;
      this.totalPages = res.data.totalPages;
      this.currentPage = page;
    } catch (error) {
      console.log("requestGameSoftwareList() 중 에러:", error);
    }
  },
};
