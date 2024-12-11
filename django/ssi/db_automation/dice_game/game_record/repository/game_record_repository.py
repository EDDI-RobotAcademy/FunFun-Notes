from abc import ABC, abstractmethod

class gameRecordRepository(ABC):
    @abstractmethod
    def save_record(self, game_id, player_number, dice_values, total_score, is_winner):
        pass

    @abstractmethod
    def get_all_records(self):
        pass

    @abstractmethod
    def get_records_by_game(self, game_id):
        pass