import * as axiosUtility from "../../utility/axiosInstance"

export const blogPostAction = {
  async requestPostList(payload) {
    const { djangoAxiosInstance } = axiosUtility.createAxiosInstances();

    const { page, perPage } = payload

    try {
        const res = await djangoAxiosInstance.get(`/blog-post/list?page=${page}&perPage=${perPage}`);

        const { dataList, totalItems, totalPages } = res.data;
        console.log(`blogPostList: ${dataList}, totalItems: ${totalItems}, totalPages: ${totalPages}`)

        // 데이터 설정
        this.blogPostList = dataList || [];
        this.totalPages = totalPages || 0;
        this.totalItems = totalItems || 0;
        this.currentPage = page;
    } catch (error) {
        console.error("requestPostList() 중 에러:", error);

        // 에러가 발생하면 상태를 초기화
        this.blogPostList = [];
        this.totalPages = 0;
        this.totalItems = 0;
        this.currentPage = 1;
    }
  },

  async requestRegisterPost(payload) {
    const { djangoAxiosInstance } = axiosUtility.createAxiosInstances();

    const { title, content } = payload;
    const userToken = localStorage.getItem("userToken"); // ✅ userToken 가져오기

    if (!userToken) {
      console.error("❌ 사용자 토큰이 없습니다.");
      throw new Error("로그인이 필요합니다.");
    }

    try {
      const response = await djangoAxiosInstance.post(
        "/blog-post/create",
        {
          title,
          content, // ✅ S3에 저장된 HTML 콘텐츠를 서버로 전송
          userToken
        }
      );

      console.log("✅ 포스트 등록 성공", response.data);
    } catch (error) {
      console.error("❌ 포스트 등록 실패:", error);
      throw new Error("포스트 등록 실패");
    }
  }
}