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
					file: resolve(themeDir, "account/pages/login/AccountLoginPage.vue"),
				},
			);

			pages.push({
                name: 'GithubAdminLoginPage',
                path: '/account/admin-login',
                file: resolve(themeDir, 'account/pages/adminLogin/GithubAdminLoginPage.vue'),
            });

			pages.push({
                name: 'AdminCodeInputPage',
                path: '/account/admin-code',
                file: resolve(themeDir, 'account/pages/adminLogin/AdminCodeInputPage.vue'),
            });

			pages.push({
				name: 'AccountWithdrawPage',
				path: '/account/withdraw',
				file: resolve(themeDir, 'account/pages/withdraw/AccountWithdrawPage.vue'),
			});
		});

		nuxt.hook("imports:dirs", (dirs) => {
			dirs.push(resolve(__dirname, "store"));
		});
	},
});