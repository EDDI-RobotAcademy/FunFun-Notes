export interface GameSoftwareState {
  gameSoftwareList: GameSoftware[];
  gameSoftware: GameSoftware | null;

  currentPage: Number;
  totalPages: Number;
}

export interface GameSoftware {
  id: number;
  title: string;
  price: string;
  description: string;
  image: string;
}
