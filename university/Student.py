import datetime


class Student:
    def __init__(self, name="", last_name="", birth_date=datetime.date(1900, 1, 1),
                 study=None):
        self.name = name
        self.last_name = last_name
        self.birth_date = birth_date
        self.study = study

    def __str__(self):
        line = "\n---------------------------------------------------------------------------------------------------\n"
        to_str = line
        to_str += f"Vardas, pavardė: {self.name.capitalize()} {self.last_name.capitalize()}, gimimo data: {self.birth_date}.\n"
        to_str += f"{self.study}\n"
        to_str += line
        return to_str

    def get_age(self):
        date1 = self.birth_date
        date2 = datetime.date.today()
        days_in_month = {
            1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
        }
        total_days = (date2 - date1).days

        if date1.year == date2.year:
            years = 0
            months = total_days / 30
            days = total_days % 30
        else:
            years = total_days / 365
            months = (total_days % 365) / 30

            if self.is_leap_year(date2.year):
                days_in_month[2] = 29

            if date2.day >= date1.day:
                days = date2.day - date1.day
            else:
                days = self.get_days(date1, date2, days_in_month)
        return datetime.date(int(years), int(months), int(days))

    @staticmethod
    def get_days(date1, date2, days_in_month):
        if date2.month == 1:
            prev_month = days_in_month[date2.month]
        else:
            prev_month = days_in_month[date2.month - 1]
        days = prev_month - date1.day + date2.day
        return days

    @staticmethod
    def is_leap_year(year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
