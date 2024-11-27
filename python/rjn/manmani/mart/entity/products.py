class Products:
    def __init__(self, name: str, count: int):
        self.name = name
        self.count = count

    def __str__(self):
        return f"{self.name}: {self.count}개"

