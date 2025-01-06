from board.entity.board import Board
from board.repository.board_repository import BoardRepository


class BoardRepositoryImpl(BoardRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def list(self, page, perPage):
        offset = (page - 1) * perPage
        boards = Board.objects.all().order_by('-create_date')[offset:offset + perPage]
        totalItems = Board.objects.count()

        return boards, totalItems
    