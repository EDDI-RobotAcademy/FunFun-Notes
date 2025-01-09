import { NuxtModule, RuntimeConfig } from '@nuxt/schema'
declare module '@nuxt/schema' {
  interface NuxtOptions {
    /**
     * Configuration for `vuetify-nuxt-module`
     */
    ["vuetify"]: typeof import("vuetify-nuxt-module").default extends NuxtModule<infer O> ? O : Record<string, any>
    /**
     * Configuration for `@pinia/nuxt`
     */
    ["pinia"]: typeof import("@pinia/nuxt").default extends NuxtModule<infer O> ? O : Record<string, any>
    /**
     * Configuration for `C:/lecture/SK-Networks-8-Notes/nuxt/uy/ui/home/index`
     */
    ["home"]: typeof import("C:/lecture/SK-Networks-8-Notes/nuxt/uy/ui/home/index").default extends NuxtModule<infer O> ? O : Record<string, any>
    /**
     * Configuration for `C:/lecture/SK-Networks-8-Notes/nuxt/uy/ui/pandas_basic/index`
     */
    ["pandas_basic"]: typeof import("C:/lecture/SK-Networks-8-Notes/nuxt/uy/ui/pandas_basic/index").default extends NuxtModule<infer O> ? O : Record<string, any>
    /**
     * Configuration for `C:/lecture/SK-Networks-8-Notes/nuxt/uy/ui/account/index`
     */
    ["account"]: typeof import("C:/lecture/SK-Networks-8-Notes/nuxt/uy/ui/account/index").default extends NuxtModule<infer O> ? O : Record<string, any>
    /**
     * Configuration for `C:/lecture/SK-Networks-8-Notes/nuxt/uy/ui/kakaoAuthentication/index`
     */
    ["kakaoAuthentication"]: typeof import("C:/lecture/SK-Networks-8-Notes/nuxt/uy/ui/kakaoAuthentication/index").default extends NuxtModule<infer O> ? O : Record<string, any>
    /**
     * Configuration for `C:/lecture/SK-Networks-8-Notes/nuxt/uy/ui/gameSoftware/index`
     */
    ["gameSoftware"]: typeof import("C:/lecture/SK-Networks-8-Notes/nuxt/uy/ui/gameSoftware/index").default extends NuxtModule<infer O> ? O : Record<string, any>
    /**
     * Configuration for `C:/lecture/SK-Networks-8-Notes/nuxt/uy/ui/board/index`
     */
    ["board"]: typeof import("C:/lecture/SK-Networks-8-Notes/nuxt/uy/ui/board/index").default extends NuxtModule<infer O> ? O : Record<string, any>
    /**
     * Configuration for `C:/lecture/SK-Networks-8-Notes/nuxt/uy/ui/cart/index`
     */
    ["cart"]: typeof import("C:/lecture/SK-Networks-8-Notes/nuxt/uy/ui/cart/index").default extends NuxtModule<infer O> ? O : Record<string, any>
    /**
     * Configuration for `C:/lecture/SK-Networks-8-Notes/nuxt/uy/ui/order/index`
     */
    ["order"]: typeof import("C:/lecture/SK-Networks-8-Notes/nuxt/uy/ui/order/index").default extends NuxtModule<infer O> ? O : Record<string, any>
    /**
     * Configuration for `C:/lecture/SK-Networks-8-Notes/nuxt/uy/ui/payments/index`
     */
    ["payments"]: typeof import("C:/lecture/SK-Networks-8-Notes/nuxt/uy/ui/payments/index").default extends NuxtModule<infer O> ? O : Record<string, any>
    /**
     * Configuration for `@nuxt/devtools`
     */
    ["devtools"]: typeof import("@nuxt/devtools").default extends NuxtModule<infer O> ? O : Record<string, any>
    /**
     * Configuration for `@nuxt/telemetry`
     */
    ["telemetry"]: typeof import("@nuxt/telemetry").default extends NuxtModule<infer O> ? O : Record<string, any>
  }
  interface NuxtConfig {
    /**
     * Configuration for `vuetify-nuxt-module`
     */
    ["vuetify"]?: typeof import("vuetify-nuxt-module").default extends NuxtModule<infer O> ? Partial<O> : Record<string, any>
    /**
     * Configuration for `@pinia/nuxt`
     */
    ["pinia"]?: typeof import("@pinia/nuxt").default extends NuxtModule<infer O> ? Partial<O> : Record<string, any>
    /**
     * Configuration for `C:/lecture/SK-Networks-8-Notes/nuxt/uy/ui/home/index`
     */
    ["home"]?: typeof import("C:/lecture/SK-Networks-8-Notes/nuxt/uy/ui/home/index").default extends NuxtModule<infer O> ? Partial<O> : Record<string, any>
    /**
     * Configuration for `C:/lecture/SK-Networks-8-Notes/nuxt/uy/ui/pandas_basic/index`
     */
    ["pandas_basic"]?: typeof import("C:/lecture/SK-Networks-8-Notes/nuxt/uy/ui/pandas_basic/index").default extends NuxtModule<infer O> ? Partial<O> : Record<string, any>
    /**
     * Configuration for `C:/lecture/SK-Networks-8-Notes/nuxt/uy/ui/account/index`
     */
    ["account"]?: typeof import("C:/lecture/SK-Networks-8-Notes/nuxt/uy/ui/account/index").default extends NuxtModule<infer O> ? Partial<O> : Record<string, any>
    /**
     * Configuration for `C:/lecture/SK-Networks-8-Notes/nuxt/uy/ui/kakaoAuthentication/index`
     */
    ["kakaoAuthentication"]?: typeof import("C:/lecture/SK-Networks-8-Notes/nuxt/uy/ui/kakaoAuthentication/index").default extends NuxtModule<infer O> ? Partial<O> : Record<string, any>
    /**
     * Configuration for `C:/lecture/SK-Networks-8-Notes/nuxt/uy/ui/gameSoftware/index`
     */
    ["gameSoftware"]?: typeof import("C:/lecture/SK-Networks-8-Notes/nuxt/uy/ui/gameSoftware/index").default extends NuxtModule<infer O> ? Partial<O> : Record<string, any>
    /**
     * Configuration for `C:/lecture/SK-Networks-8-Notes/nuxt/uy/ui/board/index`
     */
    ["board"]?: typeof import("C:/lecture/SK-Networks-8-Notes/nuxt/uy/ui/board/index").default extends NuxtModule<infer O> ? Partial<O> : Record<string, any>
    /**
     * Configuration for `C:/lecture/SK-Networks-8-Notes/nuxt/uy/ui/cart/index`
     */
    ["cart"]?: typeof import("C:/lecture/SK-Networks-8-Notes/nuxt/uy/ui/cart/index").default extends NuxtModule<infer O> ? Partial<O> : Record<string, any>
    /**
     * Configuration for `C:/lecture/SK-Networks-8-Notes/nuxt/uy/ui/order/index`
     */
    ["order"]?: typeof import("C:/lecture/SK-Networks-8-Notes/nuxt/uy/ui/order/index").default extends NuxtModule<infer O> ? Partial<O> : Record<string, any>
    /**
     * Configuration for `C:/lecture/SK-Networks-8-Notes/nuxt/uy/ui/payments/index`
     */
    ["payments"]?: typeof import("C:/lecture/SK-Networks-8-Notes/nuxt/uy/ui/payments/index").default extends NuxtModule<infer O> ? Partial<O> : Record<string, any>
    /**
     * Configuration for `@nuxt/devtools`
     */
    ["devtools"]?: typeof import("@nuxt/devtools").default extends NuxtModule<infer O> ? Partial<O> : Record<string, any>
    /**
     * Configuration for `@nuxt/telemetry`
     */
    ["telemetry"]?: typeof import("@nuxt/telemetry").default extends NuxtModule<infer O> ? Partial<O> : Record<string, any>
    modules?: (undefined | null | false | NuxtModule<any> | string | [NuxtModule | string, Record<string, any>] | ["vuetify-nuxt-module", Exclude<NuxtConfig["vuetify"], boolean>] | ["@pinia/nuxt", Exclude<NuxtConfig["pinia"], boolean>] | ["~/home/index.ts", Exclude<NuxtConfig["home"], boolean>] | ["~/pandas_basic/index.ts", Exclude<NuxtConfig["pandas_basic"], boolean>] | ["~/account/index.ts", Exclude<NuxtConfig["account"], boolean>] | ["~/kakaoAuthentication/index.ts", Exclude<NuxtConfig["kakaoAuthentication"], boolean>] | ["~/gameSoftware/index.ts", Exclude<NuxtConfig["gameSoftware"], boolean>] | ["~/board/index.ts", Exclude<NuxtConfig["board"], boolean>] | ["~/cart/index.ts", Exclude<NuxtConfig["cart"], boolean>] | ["~/order/index.ts", Exclude<NuxtConfig["order"], boolean>] | ["~/payments/index.ts", Exclude<NuxtConfig["payments"], boolean>] | ["@nuxt/devtools", Exclude<NuxtConfig["devtools"], boolean>] | ["@nuxt/telemetry", Exclude<NuxtConfig["telemetry"], boolean>])[],
  }
}
declare module 'nuxt/schema' {
  interface NuxtOptions {
    /**
     * Configuration for `vuetify-nuxt-module`
     * @see https://www.npmjs.com/package/vuetify-nuxt-module
     */
    ["vuetify"]: typeof import("vuetify-nuxt-module").default extends NuxtModule<infer O> ? O : Record<string, any>
    /**
     * Configuration for `@pinia/nuxt`
     * @see https://www.npmjs.com/package/@pinia/nuxt
     */
    ["pinia"]: typeof import("@pinia/nuxt").default extends NuxtModule<infer O> ? O : Record<string, any>
    /**
     * Configuration for `C:/lecture/SK-Networks-8-Notes/nuxt/uy/ui/home/index`
     */
    ["home"]: typeof import("C:/lecture/SK-Networks-8-Notes/nuxt/uy/ui/home/index").default extends NuxtModule<infer O> ? O : Record<string, any>
    /**
     * Configuration for `C:/lecture/SK-Networks-8-Notes/nuxt/uy/ui/pandas_basic/index`
     */
    ["pandas_basic"]: typeof import("C:/lecture/SK-Networks-8-Notes/nuxt/uy/ui/pandas_basic/index").default extends NuxtModule<infer O> ? O : Record<string, any>
    /**
     * Configuration for `C:/lecture/SK-Networks-8-Notes/nuxt/uy/ui/account/index`
     */
    ["account"]: typeof import("C:/lecture/SK-Networks-8-Notes/nuxt/uy/ui/account/index").default extends NuxtModule<infer O> ? O : Record<string, any>
    /**
     * Configuration for `C:/lecture/SK-Networks-8-Notes/nuxt/uy/ui/kakaoAuthentication/index`
     */
    ["kakaoAuthentication"]: typeof import("C:/lecture/SK-Networks-8-Notes/nuxt/uy/ui/kakaoAuthentication/index").default extends NuxtModule<infer O> ? O : Record<string, any>
    /**
     * Configuration for `C:/lecture/SK-Networks-8-Notes/nuxt/uy/ui/gameSoftware/index`
     */
    ["gameSoftware"]: typeof import("C:/lecture/SK-Networks-8-Notes/nuxt/uy/ui/gameSoftware/index").default extends NuxtModule<infer O> ? O : Record<string, any>
    /**
     * Configuration for `C:/lecture/SK-Networks-8-Notes/nuxt/uy/ui/board/index`
     */
    ["board"]: typeof import("C:/lecture/SK-Networks-8-Notes/nuxt/uy/ui/board/index").default extends NuxtModule<infer O> ? O : Record<string, any>
    /**
     * Configuration for `C:/lecture/SK-Networks-8-Notes/nuxt/uy/ui/cart/index`
     */
    ["cart"]: typeof import("C:/lecture/SK-Networks-8-Notes/nuxt/uy/ui/cart/index").default extends NuxtModule<infer O> ? O : Record<string, any>
    /**
     * Configuration for `C:/lecture/SK-Networks-8-Notes/nuxt/uy/ui/order/index`
     */
    ["order"]: typeof import("C:/lecture/SK-Networks-8-Notes/nuxt/uy/ui/order/index").default extends NuxtModule<infer O> ? O : Record<string, any>
    /**
     * Configuration for `C:/lecture/SK-Networks-8-Notes/nuxt/uy/ui/payments/index`
     */
    ["payments"]: typeof import("C:/lecture/SK-Networks-8-Notes/nuxt/uy/ui/payments/index").default extends NuxtModule<infer O> ? O : Record<string, any>
    /**
     * Configuration for `@nuxt/devtools`
     * @see https://www.npmjs.com/package/@nuxt/devtools
     */
    ["devtools"]: typeof import("@nuxt/devtools").default extends NuxtModule<infer O> ? O : Record<string, any>
    /**
     * Configuration for `@nuxt/telemetry`
     * @see https://www.npmjs.com/package/@nuxt/telemetry
     */
    ["telemetry"]: typeof import("@nuxt/telemetry").default extends NuxtModule<infer O> ? O : Record<string, any>
  }
  interface NuxtConfig {
    /**
     * Configuration for `vuetify-nuxt-module`
     * @see https://www.npmjs.com/package/vuetify-nuxt-module
     */
    ["vuetify"]?: typeof import("vuetify-nuxt-module").default extends NuxtModule<infer O> ? Partial<O> : Record<string, any>
    /**
     * Configuration for `@pinia/nuxt`
     * @see https://www.npmjs.com/package/@pinia/nuxt
     */
    ["pinia"]?: typeof import("@pinia/nuxt").default extends NuxtModule<infer O> ? Partial<O> : Record<string, any>
    /**
     * Configuration for `C:/lecture/SK-Networks-8-Notes/nuxt/uy/ui/home/index`
     */
    ["home"]?: typeof import("C:/lecture/SK-Networks-8-Notes/nuxt/uy/ui/home/index").default extends NuxtModule<infer O> ? Partial<O> : Record<string, any>
    /**
     * Configuration for `C:/lecture/SK-Networks-8-Notes/nuxt/uy/ui/pandas_basic/index`
     */
    ["pandas_basic"]?: typeof import("C:/lecture/SK-Networks-8-Notes/nuxt/uy/ui/pandas_basic/index").default extends NuxtModule<infer O> ? Partial<O> : Record<string, any>
    /**
     * Configuration for `C:/lecture/SK-Networks-8-Notes/nuxt/uy/ui/account/index`
     */
    ["account"]?: typeof import("C:/lecture/SK-Networks-8-Notes/nuxt/uy/ui/account/index").default extends NuxtModule<infer O> ? Partial<O> : Record<string, any>
    /**
     * Configuration for `C:/lecture/SK-Networks-8-Notes/nuxt/uy/ui/kakaoAuthentication/index`
     */
    ["kakaoAuthentication"]?: typeof import("C:/lecture/SK-Networks-8-Notes/nuxt/uy/ui/kakaoAuthentication/index").default extends NuxtModule<infer O> ? Partial<O> : Record<string, any>
    /**
     * Configuration for `C:/lecture/SK-Networks-8-Notes/nuxt/uy/ui/gameSoftware/index`
     */
    ["gameSoftware"]?: typeof import("C:/lecture/SK-Networks-8-Notes/nuxt/uy/ui/gameSoftware/index").default extends NuxtModule<infer O> ? Partial<O> : Record<string, any>
    /**
     * Configuration for `C:/lecture/SK-Networks-8-Notes/nuxt/uy/ui/board/index`
     */
    ["board"]?: typeof import("C:/lecture/SK-Networks-8-Notes/nuxt/uy/ui/board/index").default extends NuxtModule<infer O> ? Partial<O> : Record<string, any>
    /**
     * Configuration for `C:/lecture/SK-Networks-8-Notes/nuxt/uy/ui/cart/index`
     */
    ["cart"]?: typeof import("C:/lecture/SK-Networks-8-Notes/nuxt/uy/ui/cart/index").default extends NuxtModule<infer O> ? Partial<O> : Record<string, any>
    /**
     * Configuration for `C:/lecture/SK-Networks-8-Notes/nuxt/uy/ui/order/index`
     */
    ["order"]?: typeof import("C:/lecture/SK-Networks-8-Notes/nuxt/uy/ui/order/index").default extends NuxtModule<infer O> ? Partial<O> : Record<string, any>
    /**
     * Configuration for `C:/lecture/SK-Networks-8-Notes/nuxt/uy/ui/payments/index`
     */
    ["payments"]?: typeof import("C:/lecture/SK-Networks-8-Notes/nuxt/uy/ui/payments/index").default extends NuxtModule<infer O> ? Partial<O> : Record<string, any>
    /**
     * Configuration for `@nuxt/devtools`
     * @see https://www.npmjs.com/package/@nuxt/devtools
     */
    ["devtools"]?: typeof import("@nuxt/devtools").default extends NuxtModule<infer O> ? Partial<O> : Record<string, any>
    /**
     * Configuration for `@nuxt/telemetry`
     * @see https://www.npmjs.com/package/@nuxt/telemetry
     */
    ["telemetry"]?: typeof import("@nuxt/telemetry").default extends NuxtModule<infer O> ? Partial<O> : Record<string, any>
    modules?: (undefined | null | false | NuxtModule<any> | string | [NuxtModule | string, Record<string, any>] | ["vuetify-nuxt-module", Exclude<NuxtConfig["vuetify"], boolean>] | ["@pinia/nuxt", Exclude<NuxtConfig["pinia"], boolean>] | ["~/home/index.ts", Exclude<NuxtConfig["home"], boolean>] | ["~/pandas_basic/index.ts", Exclude<NuxtConfig["pandas_basic"], boolean>] | ["~/account/index.ts", Exclude<NuxtConfig["account"], boolean>] | ["~/kakaoAuthentication/index.ts", Exclude<NuxtConfig["kakaoAuthentication"], boolean>] | ["~/gameSoftware/index.ts", Exclude<NuxtConfig["gameSoftware"], boolean>] | ["~/board/index.ts", Exclude<NuxtConfig["board"], boolean>] | ["~/cart/index.ts", Exclude<NuxtConfig["cart"], boolean>] | ["~/order/index.ts", Exclude<NuxtConfig["order"], boolean>] | ["~/payments/index.ts", Exclude<NuxtConfig["payments"], boolean>] | ["@nuxt/devtools", Exclude<NuxtConfig["devtools"], boolean>] | ["@nuxt/telemetry", Exclude<NuxtConfig["telemetry"], boolean>])[],
  }
  interface RuntimeConfig {
   app: {
      buildId: string,

      baseURL: string,

      buildAssetsDir: string,

      cdnURL: string,
   },

   nitro: {
      envPrefix: string,
   },
  }
  interface PublicRuntimeConfig {
   MAIN_API_URL: string,

   AI_BASE_URL: string,

   TOSS_CLIENT_KEY: string,

   TOSS_SECRET_KEY: string,
  }
}
declare module 'vue' {
        interface ComponentCustomProperties {
          $config: RuntimeConfig
        }
      }