import { defineStore } from "pinia";
import { gameSoftwareState } from "./gameSoftwareState";
import { gameSoftwareAction } from "./gameSoftwareActions";

export const useGameSoftwareStore = defineStore('gameSoftwareStore', {
    state: gameSoftwareState,
    actions: gameSoftwareAction,
})