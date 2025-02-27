import { defineStore } from "pinia";
import { boardState } from "./boardState";
import { boardAction } from "./boardActions";

export const useBoardStore = defineStore('boardStore', {
    state: boardState,
    actions: boardAction,
})