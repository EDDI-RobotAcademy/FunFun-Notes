# Repository: DiceRepository (필요한 경우 저장소 역할)
class DiceRepository:
    @staticmethod
    def get_dice_sum(dice_list):
        """주사위 리스트의 합을 반환"""
        return sum(dice.number for dice in dice_list)