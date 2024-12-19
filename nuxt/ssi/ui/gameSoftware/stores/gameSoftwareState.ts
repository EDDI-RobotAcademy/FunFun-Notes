import { GameSoftware } from "./gameSoftwareType";

export const gameSoftwareState = () => ({
    gameSoftwareList: [] as GameSoftware[],
    gameSoftware: null as GameSoftware | null,
  })