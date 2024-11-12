class Sweets:
    def __init__(self, weight, price, count):
        self.weight = weight
        self.price = price
        self.count = count

    def __str__(self):
        return f"Svoris: {self.weight}, kaina: {self.price}, kiekis: {self.count}"
