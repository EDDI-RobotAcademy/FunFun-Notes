from django.db import models

class GameRecord(models.Model):
    id = models.AutoField(primary_key=True)  # Primary Key 추가
    game_id = models.IntegerField()  #게임 고유 id
    player_number = models.IntegerField()  # 플레이어 번호
    dice_values = models.CharField(max_length=255)  # 플레이어가 굴린 주사위 값 (예: "6,4")
    total_score = models.IntegerField(default=0)  # 주사위 값 총합
    is_winner = models.BooleanField(default=False)  # 승리 여부

    class Meta:
        db_table = 'game_record'  # 데이터베이스 테이블 이름 설정

    def __str__(self):
        return f"GameRecord {self.id} - Player {self.player_number} (Winner: {self.is_winner} (Game ID : {self.game_id}, Winner : {self.is_winner}))"