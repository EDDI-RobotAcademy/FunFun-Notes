import { defineStore } from "pinia";
import { cartState } from "./cartState";
import { cartAction } from "./cartActions";

export const useCartStore = defineStore('cartStore', {
    state: cartState,
    actions: cartAction,
})