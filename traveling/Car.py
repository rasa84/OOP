class Car:
    def __init__(self, num_passengers, fuel_per_100km, distance):
        self.num_passengers = num_passengers
        self.fuel_per_100km = fuel_per_100km
        self.distance = distance

    def __str__(self):
        return f"keleivių skaičius: {self.num_passengers}, suvartojimas 100 km: {self.fuel_per_100km}"




