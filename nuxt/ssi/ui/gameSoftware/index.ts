import { defineNuxtModule } from '@nuxt/kit';
import { resolve } from 'path';

export default defineNuxtModule({
    meta: {
        name: 'gameSoftware',
        configKey: 'gameSoftware',
    },

    setup(moduleOptions, nuxt) {
        const themeDir = resolve(__dirname, '..');

        nuxt.hook('pages:extend', (pages) => {
            pages.push({
                name: 'GameSoftwareList',
                path: '/game-software/list',
                file: resolve(themeDir, 'gameSoftware/pages/list/List.vue'),
            });

            pages.push({
                name: 'GameSoftwareRegister',
                path: '/game-software/register',
                file: resolve(themeDir, 'gameSoftware/pages/register/Register.vue'),
            });
        });

        nuxt.hook('imports:dirs', (dirs) => {
            dirs.push(resolve(__dirname, 'store'));
        });
    },
});