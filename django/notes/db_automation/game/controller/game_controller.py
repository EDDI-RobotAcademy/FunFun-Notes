from rest_framework import viewsets, status
from rest_framework.response import Response

from game.service.game_service_impl import GameServiceImpl


class GameController(viewsets.ViewSet):
    gameService = GameServiceImpl.getInstance()

    def requestCreateGame(self, request):
        game = self.gameService.createGame()

        return Response(game, status=status.HTTP_200_OK)

    def requestCheckWinner(self, request):
        requestGetData = request.GET
        gameId = requestGetData.get('gameId')

        winnerInfo = self.gameService.checkWinner(gameId)

        return Response(None, status=status.HTTP_200_OK)
