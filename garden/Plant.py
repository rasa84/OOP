class Plant:
    def __init__(self, title = "", latin_title = "", annual_plant = False, continent = "", height = 0, edible = False):
        self.Title = title
        self.Latin_title = latin_title
        self.Annual_plant = annual_plant
        self.Continent = continent
        self.Height = height
        self.Edible = edible

    def __str__(self):
        return (f"Augalas: {self.Title}, lotyniškas pavadinimas: {self.Latin_title}, ar metinis? {"Taip" if self.Annual_plant else "Ne"}"
                f", žemynas = {self.Continent}, ar valgomas? {"Taip" if self.Edible else "Ne"}")



