from account.repository.account_repository_impl import AccountRepositoryImpl
from account_profile.repository.account_profile_repository_impl import AccountProfileRepositoryImpl
from board.entity.board import Board
from board.repository.board_repository_impl import BoardRepositoryImpl
from board.service.board_service import BoardService


class BoardServiceImpl(BoardService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__instance.__boardRepository = BoardRepositoryImpl.getInstance()
            cls.__instance.__accountRepository = AccountRepositoryImpl.getInstance()
            cls.__instance.__accountProfileRepository = AccountProfileRepositoryImpl.getInstance()

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
                "nickname": board.writer.nickname,  # writer 객체의 nickname 가져오기
                "createDate": board.create_date.strftime("%Y-%m-%d %H:%M"),
            }
            for board in paginatedBoardList
        ]

        return paginatedFilteringBoardList, totalItems, totalPages

    def requestCreate(self, title, content, accountId):
        if not title or not content:
            raise ValueError("Title and content are required fields.")
        if not accountId:
            raise ValueError("Account ID is required.")

            # 2. Account 조회
        account = self.__accountRepository.findById(accountId)
        if not account:
            raise ValueError(f"Account with ID {accountId} does not exist.")

        # 3. AccountProfile 조회
        accountProfile = self.__accountProfileRepository.findByAccount(account)
        if not accountProfile:
            raise ValueError(f"AccountProfile for account ID {accountId} does not exist.")

        # 4. Board 객체 생성 및 저장
        board = Board(
            title=title,
            content=content,
            writer=accountProfile)  # ForeignKey로 연결된 account_profile)
        savedBoard = self.__boardRepository.save(board)

        # 5. 응답 데이터 구조화
        return {
            "boardId": savedBoard.id,
            "title": savedBoard.title,
            "writerNickname": savedBoard.writer.nickname,
            "createDate": savedBoard.create_date.strftime("%Y-%m-%d %H:%M"),
        }
    