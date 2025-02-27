from rest_framework import viewsets, status
from rest_framework.response import Response
from dice_game.game_record.repository.game_record_repository_impl import gameRecordRepositoryImpl
from dice_game.game_record.entity.game_record_entity import GameRecord
from dice_game.game.service.game_service_impl import GameServiceImpl

class gameRecordController(viewsets.ViewSet):
    repository = gameRecordRepositoryImpl.get_instance()
    diceServiceRepository=GameServiceImpl()

    def roll_dice_and_save(self, request):
        # Determine the next game_id
        last_record = GameRecord.objects.order_by('-game_id').first()
        next_game_id = last_record.game_id + 1 if last_record else 1

        # Roll the dice using GameService
        game_service = GameServiceImpl.getInstance()
        rolled_dice = game_service.rollDice()

        # Split dice values for two players
        player1_dice = [dice['number'] for dice in rolled_dice[:2]]
        player2_dice = [dice['number'] for dice in rolled_dice[2:]]

        player1_total = sum(player1_dice)
        player2_total = sum(player2_dice)

        # Determine the winner
        if player1_total > player2_total:
            is_player1_winner = True
            is_player2_winner = False
        elif player2_total > player1_total:
            is_player1_winner = False
            is_player2_winner = True
        else:
            is_player1_winner = True
            is_player2_winner = True

        # Save records for both players
        GameRecord.objects.create(
            game_id=next_game_id,
            player_number=1,
            dice_values=",".join(map(str, player1_dice)),
            total_score=player1_total,
            is_winner=is_player1_winner
        )
        GameRecord.objects.create(
            game_id=next_game_id,
            player_number=2,
            dice_values=",".join(map(str, player2_dice)),
            total_score=player2_total,
            is_winner= is_player2_winner
        )

        return Response({
            
            "message": "Game record saved successfully",

            "game_id": next_game_id,
            "player1": {
                "dice_values": player1_dice,
                "total_score": player1_total,
                "is_winner": is_player1_winner
            },
            "game_id": next_game_id,
            "player2": {
                "dice_values": player2_dice,
                "total_score": player2_total,
                "is_winner": is_player2_winner
            }
        }, status=201)

    def get_records_by_gameId(self, request):
        # game_id 파라미터 추출
        game_id = request.GET.get('game_id')

        if not game_id:
            # game_id가 없으면 에러 메시지 반환
            return Response({"error": "game_id is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Repository를 통해 해당 game_id의 기록 조회
        records = self.repository.get_records_by_game(game_id)
        
        if not records.exists():
            # 해당 game_id에 대한 기록이 없으면 빈 리스트 반환
            return Response({"message": f"No records found for game_id {game_id}"}, status=status.HTTP_404_NOT_FOUND)
        
        # 조회한 기록을 JSON 형태로 변환
        data = [
            {
                "game_id": record.game_id,
                "player_number": record.player_number,
                "dice_values": record.dice_values,
                "total_score": record.total_score,
                "is_winner": record.is_winner
            }
            for record in records
        ]
        
        # 결과 반환
        return Response(data, status=status.HTTP_200_OK)


    def get_all_records(self, request):
        records = self.repository.get_all_records()

        if not records.exists():
            return Response([], status=status.HTTP_200_OK)

        data = [
            {
                "game_id": record.game_id,
                "player_number": record.player_number,
                "dice_values": record.dice_values,
                "total_score": record.total_score,
                "is_winner": record.is_winner
            }
            for record in records
        ]
        return Response(data, status=status.HTTP_200_OK)




    def getSumDice(self, request):
        dice=self.diceServiceRepository.checkWinner()

        return Response(dice, status=status.HTTP_200_OK)
