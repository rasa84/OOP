class AnotherBook:
    def __init__(self, title, price, pages_count):
        self.title = title
        self.price = price
        self.pages_count = pages_count

    def __str__(self):
        return f"Pavadinimas: {self.title}, kaina: {self.price}, puslapių skaičius: {self.pages_count}"

    def count_times_of_100_pages_in_book(self):
        return round(self.pages_count // 100)

    def is_more_expensive_than_20(self):
        return self.price > 20
