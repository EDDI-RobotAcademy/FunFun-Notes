import { Order } from "./orderStore";

export const orderState = () => ({
    orderList: [] as Order[],
    order: null as Order | null,

    currentPage: 1,
    totalPages: 0,

    orderInfoId: null,
})