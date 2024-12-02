from abc import ABC, abstractmethod


class MartRepository(ABC):

    @abstractmethod
    def addFruit(self, fruitName, amount):
        pass

    def printCurrentStatus(self):
        pass

    # def remove_fruit(self, 필요하면_배치하거나_전달할_요소들_없어도됨):
    #     pass