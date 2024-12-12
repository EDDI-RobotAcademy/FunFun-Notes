import { defineNuxtConfig } from "nuxt/config"

export default defineNuxtConfig({
  compatibilityDate: '2024-11-01',
  devtools: { enabled: true },
  extends: ['./pandas_basic/nuxt.config.ts'],

  css: [
    'vuetify/styles',
    '@mdi/font/css/materialdesignicons.min.css',
  ],

  build: {
    transpile: ['vuetify']
  },

  vite: {
    ssr: {
      noExternal: ['vuetify'],
    },
  },

  modules: [
    'vuetify-nuxt-module',
    '@pinia/nuxt',
    '~/pandas_basic/index.ts'
  ],

  imports: {
    dirs: ['./stores']
  }
})