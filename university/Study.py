class Study:
    def __init__(self, title="", disciplines=[]):
        self.title = title
        self.disciplines = disciplines

    def __str__(self):
        to_string = f"Studijų pavadinimas: {self.title}\n"
        to_string += f"Dalykai: \n"
        for d in self.disciplines:
            to_string += f" - {d}"
        return to_string

    def get_discipline_by_title(self, title):
        for d in self.disciplines:
            if d.title == title:
                return d
        return None

    def get_average(self):
        averages = []
        for d in self.disciplines:
            averages.append(d.get_grades_average())
        return round(sum(averages) / len(averages), 2)
