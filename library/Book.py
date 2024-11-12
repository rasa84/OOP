class Book:
    def __init__(self, title = "", pages = 0 , release_year = 0):
        self.Title = title
        self.Pages = pages
        self.ReleaseYear = release_year

    def __str__(self):
        return (f"Knygos pavadinimas: {self.Title}, puslapių skaičius: {self.Pages}, "
                f"išleidimo metai: {self.ReleaseYear}") if self.Title else "Knygos nėra"

