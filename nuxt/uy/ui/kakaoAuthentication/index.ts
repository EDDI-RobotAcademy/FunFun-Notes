//  url 매핑

import { defineNuxtModule } from '@nuxt/kit';
import { resolve } from 'path';

export default defineNuxtModule({
    meta: {
        name: 'pandas_basic',
        configKey: 'pandas_basic',
    },

    setup(moduleOptions, nuxt) {
        const themeDir = resolve(__dirname, '..');

        nuxt.hook('pages:extend', (pages) => {
            pages.push({
                name: 'kakaoRedirection',
                path: '/kakao-oauth/',
                file: resolve(themeDir, 'pandas_basic/pages/PandasBasicInfo.vue'),
            });
        });

        nuxt.hook('imports:dirs', (dirs) => {
            dirs.push(resolve(__dirname, 'store'));
        });
    },
});