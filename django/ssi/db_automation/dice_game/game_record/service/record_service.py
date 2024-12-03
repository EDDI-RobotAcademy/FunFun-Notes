from game_record.repository.game_record_repository_impl import GameRecordRepositoryImpl

class GameRecordService:
    def __init__(self):
        self.repository = GameRecordRepositoryImpl()

    def save_game_record(self, game_id, player_data):
        """
        게임 기록 저장 로직
        - game_id: Game ID
        - player_data: 각 플레이어 데이터 리스트
        """
        for player in player_data:
            self.repository.save_record(
                game_id=game_id,
                player_number=player["player_number"],
                dice_values=",".join(map(str, player["dice"])),
                total_score=player["total_score"],
                is_winner=player["is_winner"]
            )

    def get_game_records(self, game_id):
        """
        특정 게임 기록 조회
        """
        return self.repository.get_records_by_game(game_id)
