from rest_framework import viewsets, status
from rest_framework.response import Response

from game.service.game_service_impl import GameServiceImpl


class GameController(viewsets.ViewSet):
    gameService = GameServiceImpl.getInstance()

    def requestCreateGame(self, request):
        requestGetData = request.GET
        playerCount = requestGetData.get('playerCount')
        game = self.gameService.createGame(playerCount)

        return Response(game, status=status.HTTP_200_OK)

    def requestCalculateWinner(self, request):
        requestGetData = request.GET
        gameId = requestGetData.get('gameId')

        info = self.gameService.calculateWinner(gameId)

        return Response(info, status=status.HTTP_200_OK)

    def requestGameInfo(self, request):
        requestGetData = request.GET
        gameId = requestGetData.get('gameId')

        info = self.gameService.requestInfo(gameId)

        return Response(info, status=status.HTTP_200_OK)
