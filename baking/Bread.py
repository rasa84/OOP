class Bread:
    def __init__(self, flour, weight, price, space):
        self.space = space
        self.flour = flour
        self.weight = weight
        self.price = price

    def __str__(self):
        return f"miltai: {self.flour}, svoris: {self.weight}, kaina: {self.price}, plotas: {self.space}"
