from collections import defaultdict
from typing import Dict, Any, List

from dice.repository.dice_repository_impl import DiceRepositoryImpl
from game.entity.game_state import GameState
from game.repository.game_player_info_repository_impl import GamePlayerInfoRepositoryImpl
from game.repository.game_repository_impl import GameRepositoryImpl
from game.repository.game_winner_info_repository_impl import GameWinnerInfoRepositoryImpl
from game.service.game_service import GameService
from player.repository.player_repository_impl import PlayerRepositoryImpl


class GameServiceImpl(GameService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__instance.__gameRepository = GameRepositoryImpl.getInstance()
            cls.__instance.__gamePlayerInfoRepository = GamePlayerInfoRepositoryImpl.getInstance()
            cls.__instance.__gameWinnerInfoRepository = GameWinnerInfoRepositoryImpl.getInstance()

            cls.__instance.__diceRepository = DiceRepositoryImpl.getInstance()
            cls.__instance.__playerRepository = PlayerRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def createGame(self, playerCount):
        self.__gameRepository.create(playerCount)

    def __calculatePlayerScore(self, diceList):
        scoreDictionary = defaultdict(int)
        for dice in diceList:
            scoreDictionary[dice.player.id] += dice.number

        return scoreDictionary

    def __handleWin(self, game, winnerId, playerScoreDictionary):
        winner = self.__playerRepository.findById(winnerId)
        self.__gameWinnerInfoRepository.create(game=game, player=winner)

        playerList = [playerId for playerId in playerScoreDictionary.keys()
                      if playerId != winnerId]

        for playerId in playerList:
            player = self.__playerRepository.findById(playerId)
            self.__gamePlayerInfoRepository.create(game=game, player=player)

        self.__gameRepository.update(game=game, gameState=GameState.WIN.value)

        return f"승자: {winner}, 승자 점수: {playerScoreDictionary[winnerId]}"

    def __handleDraw(self, game, winnerList, playerScoreDictionary):
        for playerId in playerScoreDictionary.keys():
            player = self.__playerRepository.findById(playerId)
            self.__gamePlayerInfoRepository.create(game=game, player=player)

        self.__gameRepository.update(game=game, state=GameState.DRAW.value)

        scoreList = ", ".join([f"Player {playerId}: {playerScoreDictionary[playerId]}" for playerId in winnerList])
        return f"무승부: {scoreList}"

    def calculateWinner(self, gameId):
        game = self.__gameRepository.findById(gameId)
        if not game:
            raise ValueError(f"Game with ID {gameId} does not exist.")

        diceList = self.__diceRepository.findByGameId(game)
        if not diceList:
            raise ValueError(f"No dice rolls found for Game ID {gameId}.")

        playerScoreDictionary = self.__calculatePlayerScore(diceList)

        maxScore = max(playerScoreDictionary.values())
        winnerList = [playerId for playerId, score in playerScoreDictionary.items()
                      if score == maxScore]

        if len(winnerList) == 1:
            return self.__handleWin(game, winnerList[0], playerScoreDictionary)

        return self.__handleDraw(game, winnerList, playerScoreDictionary)

    def __buildPlayerData(self, player, role: str, game) -> Dict[str, Any]:
        playerDiceList = self.__diceRepository.findByGameAndPlayer(game, player)

        return {
            "role": role,
            "player": {
                "id": player.getId(),
                "nickname": player.getNickname(),
                "diceNumber": [dice.getNumber() for dice in playerDiceList],
            },
        }

    def requestInfo(self, gameId: int) -> List[Dict[str, Any]]:
        game = self.__gameRepository.findById(gameId)
        playerList = self.__gamePlayerInfoRepository.findPlayerListByGame(game)

        result = []

        gameState = game.getState()

        if gameState == GameState.WIN.value:
            winnerInfo = self.__gameWinnerInfoRepository.findByGame(gameId)
            winner = winnerInfo.getPlayer()

            result.append(self.__buildPlayerData(winner, "Winner", game))

            for player in playerList:
                if player != winner:
                    result.append(self.__buildPlayerData(player, "Loser", game))

            return result

        for player in playerList:
            result.append(self.__buildPlayerData(player, "Draw", game))

        return result
