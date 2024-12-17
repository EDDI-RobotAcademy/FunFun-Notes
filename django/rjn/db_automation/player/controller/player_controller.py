from rest_framework import viewsets, status
from rest_framework.response import Response

from player.service.player_service_impl import PlayerServiceImpl


class PlayerController(viewsets.ViewSet):
    playerService = PlayerServiceImpl.getInstance()

    def requestCreatePlayer(self, request):
        requestGetData = request.GET
        requestNickname = requestGetData.get('nickname')

        player = self.playerService.createPlayer(requestNickname)

        return Response(player, status=status.HTTP_200_OK)
