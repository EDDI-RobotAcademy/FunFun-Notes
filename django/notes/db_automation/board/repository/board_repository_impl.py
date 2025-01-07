from django.db import IntegrityError

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

    def save(self, board):
        try:
            # Board 객체를 데이터베이스에 저장
            board.save()  # 새 객체를 저장하거나 기존 객체를 업데이트
            return board  # 저장된 Board 객체를 반환
        except IntegrityError as e:
            # 저장 중에 발생한 예외 처리
            print(f"Error saving board: {e}")
            raise Exception("Board 저장 중 오류가 발생했습니다.")