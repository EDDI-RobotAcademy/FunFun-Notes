import * as axiosUtility from "../../utility/axiosInstance"

export const dataAnalysisAction = {
  async requestDataAnalysis(excelFile) {
    const { fastapiAxiosInst } = axiosUtility.createAxiosInstances();

    if (!excelFile) {
      alert("Please select a file first.");
      return;
    }
    try {
      const formData = new FormData();
      formData.append("file", excelFile);

      const response = await fastapiAxiosInst.post("/game-software-data/analysis", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
        responseType: "blob",
      });

      console.log(`response.data: ${response.data}`)
      console.log(`JSON.stringify(response.data): ${JSON.stringify(response.data)}`)

      if (response.headers["content-type"].startsWith("image/")) {
        console.log('condition satisfy')
        const imageURL = URL.createObjectURL(response.data);
        console.log(`Generated image URL: ${imageURL}`);
        return imageURL;
      } else {
        throw new Error("Unexpected response type");
      }
    } catch (error) {
      console.error("Error uploading file:", error);
      alert("File upload failed.");
      throw error
    }
  },
}