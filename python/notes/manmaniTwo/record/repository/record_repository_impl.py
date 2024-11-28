from record.entity.record import Record
from record.repository.record_repository import RecordRepository


class RecordRepositoryImpl(RecordRepository):
    __instance = None
    __recordList = []

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def getRecordList(self):
        return self.__recordList

    def create(self, accountId, turnCountNumber, isWin):
        record = Record(accountId, turnCountNumber, isWin)

        self.__recordList.append(record)
