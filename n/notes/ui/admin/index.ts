import { defineNuxtModule } from "@nuxt/kit";
import { resolve } from "path";

export default defineNuxtModule({
	meta: {
		name: "admin",
		configKey: "admin",
	},

	setup(moduleOptions, nuxt) {
		const themeDir = resolve(__dirname, "..");

		nuxt.hook("pages:extend", (pages) => {
			pages.push({
                name: 'AdminDefaultPage',
                path: '/admin/default',
                file: resolve(themeDir, 'admin/pages/default/AdminDefaultPage.vue'),
            });

			pages.push({
                name: 'GithubActionsPage',
                path: '/admin/monitoring',
                file: resolve(themeDir, 'admin/pages/githubActions/GithubActionsPage.vue'),
            });

			pages.push({
				name: 'WorkflowSettingsPage',
				path: '/admin/workflow-settings',
				file: resolve(themeDir, 'admin/pages/githubActions/WorkflowSettingsPage.vue'),
			});
		});

		nuxt.hook("imports:dirs", (dirs) => {
			dirs.push(resolve(__dirname, "store"));
		});
	},
});