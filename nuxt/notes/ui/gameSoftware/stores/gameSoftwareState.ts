import { Product } from "./gameSoftwareType";

export const gameSoftwareState = () => ({
    productList: [] as Product[],
    product: null as Product | null,
  })