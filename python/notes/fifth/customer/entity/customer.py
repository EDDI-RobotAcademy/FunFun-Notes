class Customer:
    __counter = 1

    def __init__(self, name):
        self.__id = Customer.__counter
        Customer.__counter += 1
        self.__name = name

    def getId(self):
        return self.__id

    def getName(self):
        return self.__name
