class Discipline:
    def __init__(self, title="", grades=[]):
        self.title = title
        self.grades = grades

    def __str__(self):
        return f"{self.title}: {self.grades}\n"

    def get_grades_average(self):
        return round(sum(self.grades) / len(self.grades))
