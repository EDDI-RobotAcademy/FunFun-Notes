import { defineNuxtModule } from "@nuxt/kit"; // 모듈정의를 위한 함수
import { resolve } from "path"; // 파일 경로를 절대 경로로 변환하는 함수

export default defineNuxtModule({
  meta: {
    // 데이터를 정의할 곳곳
    name: "pandas_basic", // 모듈이름 정의
    configKey: "pandas_basic", // 모듈 설정 키 정의
  },

  setup(moduleOptions, nuxt) {
    // nuxt를 통해 다양한 기능에 접근 가능
    const themeDir = resolve(__dirname, "..");
    // __dirname은 현재 파일의 디렉토리이고, ..은 한단계 상위 디렉토리 의미
    // 이 경로가 themeDir에 저장

    nuxt.hook("pages:extend", (pages) => {
      // 페이지 설정을 확장
      pages.push({
        name: "pandas-basic-info", // 이름설정
        path: "/pandas-basic/info", // url 경로 지정
        file: resolve(themeDir, "pandas_basic/pages/PandasBasicInfo.vue"),
      });
    });

    nuxt.hook("imports:dirs", (dirs) => {
      dirs.push(resolve(__dirname, "store"));
    });
  },
});
