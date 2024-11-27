from enum import Enum

class ConsoleUiMessageState(Enum):
    MAIN = 1
    REGISTER = 2
    LOGIN = 3

    LOBBY = 10
    BATTLE_START = 11
    BATTLE_HISTORY = 12
    BACK_TO_MAIN = 13

    DRAW_DECK = 20
    GIVE_UP = 21

    FINISH = 4444
