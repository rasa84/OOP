class Sugar:
    def __init__(self, weight, price_kg, manufacture_date):
        self.weight = weight
        self.price_kg = price_kg
        self.manufacture_date = manufacture_date

    def calculate_total_price(self):
        return self.weight * self.price_kg

    def __repr__(self):
        return f"Cukrus(mase={self.weight}, kg_kaina={self.price_kg}, pagaminimo_data = '{self.pagaminimo_data}')"

    def __str__(self):
        return f"Cukraus maišas: {self.weight} kg, 1 kg kaina: {self.price_kg} EUR, Pagaminimo data: {self.manufacture_date}"
