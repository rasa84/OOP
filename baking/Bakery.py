from baking.Bread import Bread
from baking.BreadType import BreadType


class Bakery:

    def __init__(self, title, wheat_flour_kg, rye_flour_kg, barley_flour_kg, weight_kg_per_auto):
        self.title = title
        self.breads_info = {
            BreadType.WHITE: {
                "bread": Bread("wheat", 0.6, 1.3, 0.3),
                "flour_kg": wheat_flour_kg
            },
            BreadType.RYE: {
                "bread": Bread("rye", 0.4, 1.8, 0.2),
                "flour_kg": rye_flour_kg
            },
            BreadType.WHOLE_GRAIN: {
                "bread": Bread("barley", 0.8, 1.6, 0.1),
                "flour_kg": barley_flour_kg
            }
        }
        self.weight_kg_per_auto = weight_kg_per_auto

    def __str__(self):
        return f"pavadinimas - {self.title}, duonutės rūšys: {[key.value for key in self.breads_info.keys()]}"

    def calculate_shelf_space(self):
        spaces = []
        for type, value in self.breads_info.items():
            space = round(self.calculate_shelf_space_per_bread_type(type), 2)
            spaces.append({type.value: space})
        return spaces

    def calculate_shelf_space_per_bread_type(self, bread_type):
        bread_info = self.breads_info[bread_type]
        weight = bread_info["flour_kg"] // bread_info["bread"].weight
        bread_count = weight
        return bread_count * bread_info["bread"].space

    def calculate_ride_times(self):
        total_weight = 0
        for bi in self.breads_info.values():
            total_weight += bi["flour_kg"]
        print(total_weight)
        return round(total_weight / self.weight_kg_per_auto)
