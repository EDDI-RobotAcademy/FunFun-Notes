export interface BoardState {
    boardList: Board[]
    board: Board | null
  
    currentPage: Number
    totalPages: Number
  }
  
  export interface Board {
    id: number
    title: string
    price: string
    description: string
    image: string
  }
    