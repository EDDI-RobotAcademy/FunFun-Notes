import * as axiosUtility from "../../utility/axiosInstance"

export const imageGalleryAction = {
  async requestImageList(payload) {
    const { djangoAxiosInstance } = axiosUtility.createAxiosInstances();

    const { page, perPage } = payload

    try {
        const res = await djangoAxiosInstance.get(`/image-gallery/list?page=${page}&perPage=${perPage}`);

        const { dataList, totalItems, totalPages } = res.data;
        console.log(`imageGalleryList: ${dataList}, totalItems: ${totalItems}, totalPages: ${totalPages}`)

        // 데이터 설정
        this.imageGalleryList = dataList || [];
        this.totalPages = totalPages || 0;
        this.totalItems = totalItems || 0;
        this.currentPage = page;
    } catch (error) {
        console.error("requestBoardList() 중 에러:", error);

        // 에러가 발생하면 상태를 초기화
        this.boardList = [];
        this.totalPages = 0;
        this.totalItems = 0;
        this.currentPage = 1;
    }
  },
}