export interface CartState {
  boardList: Cart[]
  board: Cart | null

  currentPage: Number
  totalPages: Number
}

export interface Cart {
  id: number
  title: string
  price: string
  description: string
  image: string
}
  