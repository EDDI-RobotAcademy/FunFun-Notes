class Buyer:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Buyer: {self.name}"
buyer = Buyer("부대찌개")