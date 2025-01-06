from account.repository.account_repository_impl import AccountRepositoryImpl
from board.repository.board_repository_impl import BoardRepositoryImpl
from board.service.board_service import BoardService


class BoardServiceImpl(BoardService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__instance.__boardRepository = BoardRepositoryImpl.getInstance()
            cls.__instance.__accountRepository = AccountRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def requestList(self, page, perPage):
        paginatedBoardList, totalItems = self.__boardRepository.list(page, perPage)

        totalPages = (totalItems + perPage - 1) // perPage

        paginatedFilteringBoardList = [
            {
                "boardId": board.id,
                "title": board.title,
                "writerNickname": board.writer.nickname,  # writer 객체의 nickname 가져오기
                "createDate": board.create_date.strftime("%Y-%m-%d %H:%M"),
            }
            for board in paginatedBoardList
        ]

        return paginatedFilteringBoardList, totalItems, totalPages

    def requestCreate(self, title, content, accountId):
        pass
    