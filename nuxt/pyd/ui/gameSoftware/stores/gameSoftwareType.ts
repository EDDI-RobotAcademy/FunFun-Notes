export interface GameSoftwareState {
  gameSoftwareList: GameSoftware[]
  gameSoftware: GameSoftware | null
}

export interface GameSoftware {
  id: number
  title: string
  price: string
  description: string
  image: string
}
  