import * as axiosUtility from "../../utility/axiosInstance";

export const gameSoftwareAction = {
  async requestGameSoftwareList(
    page: number = 1,
    perPage: number = 8
  ): Promise<void> {
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
  async requestCreateGameSoftware(imageFormData: FormData): Promise<void> {
    console.log(`requestCreateGameSoftware(): ${imageFormData}`);
    const { djangoAxiosInstance } = axiosUtility.createAxiosInstances();

    try {
      const res = await djangoAxiosInstance.post(
        "/game-software/create",
        imageFormData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      );
      console.log("Response Data:", res.data);
    } catch (error) {
      console.log("requestCreateGameSoftware() 중 에러:", error);
    }
  },
  async requestGameSoftwareById(id: string): Promise<any> {
    const { djangoAxiosInstance } = axiosUtility.createAxiosInstances();

    try {
      const res = await djangoAxiosInstance.get(`/game-software/read/${id}`);
      console.log("Response Data:", res.data);
      return res.data;
    } catch (error) {
      console.log("requestGameSoftwareById() 중 에러:", error);
      throw error;
    }
  },
};
