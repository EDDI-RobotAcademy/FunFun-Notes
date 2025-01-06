import { defineStore } from "pinia";
import { orderState } from "./orderState";
import { orderAction } from "./orderActions";


export const useCartStore = defineStore('cartStore', {
    state: orderState,
    actions: orderAction,
})