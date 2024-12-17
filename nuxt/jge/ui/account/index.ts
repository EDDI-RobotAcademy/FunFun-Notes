import { defineNuxtModule } from "@nuxt/kit";
import { resolve } from "path";

export default defineNuxtModule({
	meta: {
		name: "account",
		configKey: "account",
	},

	setup(moduleOptions, nuxt) {
		const themeDir = resolve(__dirname, "..");

		nuxt.hook("pages:extend", (pages) => {
			pages.push(
				{
					name: "AccountLoginPage",
					path: '/account/login',
					file: resolve(themeDir, "account/pages/login/AccountLoginPage.vue"), //어카운트로그인페이지뷰 경로, url 들어오면 어떤 화면 그려질지 결정됨
				},
			);
		});

		nuxt.hook("imports:dirs", (dirs) => {
			dirs.push(resolve(__dirname, "store"));
		});
	},
});