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
      });

      alert("File uploaded successfully!");
      console.log(response.data);
    } catch (error) {
      console.error("Error uploading file:", error);
      alert("File upload failed.");
    }
  },
}