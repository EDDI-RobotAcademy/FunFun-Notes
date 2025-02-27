import { Cart } from "./cartType";

export const cartState = () => ({
    cartList: [] as Cart[],
    cart: null as Cart | null,

    currentPage: 1,
    totalPages: 0
  })