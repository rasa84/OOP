import datetime

from baking.Bakery import Bakery
from baking.Bread import Bread
from baking.BreadType import BreadType
from book.AnotherBook import AnotherBook
from confection.SweetTooth import SweetTooth
from confection.Sweets import Sweets
from garden.Plant import Plant
from library.Book import Book
from traveling.Car import Car
from traveling.Train import Train
from university.Discipline import Discipline
from university.Student import Student
from university.Study import Study

book1 = Book()
book1.Title = "Triušio klajonės"
book1.Pages = 100
book1.ReleaseYear = 1951

book2 = Book()
book2.Title = "Sapnininkas"
book2.Pages = 200
book2.ReleaseYear = 1985

book3 = Book()
book3.Title = "Tikras pasaulis"
book3.Pages = 350
book3.ReleaseYear = 2020

book4 = Book("Tikros istorijos", 150, 1999)
book5 = Book("Pingvinukas Lolo", 250, 1988)
book6 = Book("Bembio nuotykiai", 130, 2015)

books = [book1, book2, book3, book4, book5, book6]

for b in books:
    print(b)

print("***************************************************************************************************************")

plant1 = Plant()
plant1.Title = "Kaktusas"
plant1.Latin_title = "Cactaceae"
plant1.Annual_plant = False
plant1.Continent = "Amerika"
plant1.Height = 1
plant1.Edible = False

plant2 = Plant()
plant2.Title = "Obelis"
plant2.Latin_title = "Malus"
plant2.Annual_plant = False
plant2.Continent = "Europa"
plant2.Height = 3
plant2.Edible = True

plant3 = Plant("Kriaušė", "Pyrus", False, "Azija", 4, True)
plant4 = Plant("Žiedinis kopūstas", "Brassica oleracea", True, "Australija", 0.5, True)

plants = [plant1, plant2, plant3, plant4]
for p in plants:
    print(p)

statistics = Discipline("statistika", [8, 7, 4, 5, 8])
algorithms = Discipline("algoritmai ir struktūros", [8, 7, 9])
programming = Discipline("programavimas", [7, 5, 6, 10, 8, 9, 9])

study = Study("informatika", [statistics, algorithms, programming])

student = Student("petras", "PETRAUSKAS", datetime.date(2000, 4, 24), study)
print(student)
s_birth_date = student.get_age()

print("Studento amžius: ", int(s_birth_date.year), "metai ", s_birth_date.month, "mėnesiai ", int(s_birth_date.day),
      "dienų.")
print("Studento disciplinos vidurkis: ",
      student.study.get_discipline_by_title("algoritmai ir struktūros").get_grades_average())
print("Studento vidurkių vidurkis: ", student.study.get_average())

print("---------------------------------1 uzd.------------------------------------------------")
book1 = AnotherBook("Tikros istorijos", 30, 350)
book2 = AnotherBook("Pingvinukas Lolo", 15, 150)
book3 = AnotherBook("Bembio nuotykiai", 25, 80)

books = [book1, book2, book3]
for b in books:
    print(b)
for b in books:
    count = b.count_times_of_100_pages_in_book()
    expensive = b.is_more_expensive_than_20()
    print(f"Knygoje 100 puslapių telpa {count} kartų")
    print(f"Ar knyga yra brangesnė už 20 eur? {"Taip" if expensive else "Ne"}")

print("---------------------------------2 uzd.------------------------------------------------")
bread1 = Bread("kvietiniai", 0.6, 1.3, 0.3)
bread2 = Bread("ruginiai", 0.5, 1, 0.2)
bread3 = Bread("miežiniai", 0.8, 1.8, 0.4)

breads = [bread1, bread2, bread3]
min_weight_bread = breads[0]
max_price_bread = breads[0]
for b in breads:
    if b.weight < min_weight_bread.weight:
        min_weight_bread = b
    if b.price > max_price_bread.price:
        max_price_bread = b

print(f"Mažiausiai sveriančios duonos info: {min_weight_bread}")
print(f"Daugiausiai kainuojančios duonos info: {max_price_bread}")

bakery = Bakery("Danutės duonutė", 200, 250, 80, 200)
print(f"Kepyklėlės info: {bakery}")
print(f"Ruginės duonos užimas lentynos plotas: {bakery.calculate_shelf_space_per_bread_type(BreadType.RYE)}")
print("Shelf Space Information:")
shelf_spaces = bakery.calculate_shelf_space()
for ss in shelf_spaces:
    for bread_type, space in ss.items():
        print(f"  - {BreadType(bread_type).value} requires {space} square meters of shelf space.")

print(f"Automobilis, kad nuvežti duoną, turės važiuoti: {bakery.calculate_ride_times()} kartus")

print("---------------------------------3 uzd.------------------------------------------------")
distance = 300
fuel_price = 1.5
train_ticket_price = 6

car1 = Car(5, 5.7, distance)
car2 = Car(10, 9.5, distance)
car3 = Car(7, 7.4, distance)

cars = [car1, car2, car3]
min_fuel_car = cars[0]
min_car = cars[0]
for c in cars:
    fuel_per_passenger = c.fuel_per_100km / c.num_passengers
    min_fuel_per_passenger = min_fuel_car.fuel_per_100km / min_fuel_car.num_passengers
    if fuel_per_passenger < min_fuel_per_passenger:
        min_fuel_car = c
    if c.num_passengers > min_car.num_passengers:
        min_car = c
print(f"Pigiausia kelionė su šiuo atomobiliu, kurio duomenys: {min_fuel_car}")
print(f"Didžiausiame automobilyje telpa: {min_car.num_passengers}")

train = Train(distance, train_ticket_price)
for car in cars:
    if train.distance < car.distance:
        print(f"Ilgesnį atstumą nuvažiuos automobilis, kurio duomenys: {car}")
min_car = cars[0]
for c in cars:
    if c.num_passengers < min_car.num_passengers:
        min_car = c
car_price_per_person = (min_car.fuel_per_100km * (distance / 100) * fuel_price) / min_car.num_passengers
print(f"Mažiausio automobilio kelionės kaina: {car_price_per_person}")
print(f"Ar apsimoka juo važiuoti: {"Taip" if car_price_per_person < train.ticket_price else "Ne"}")

print("---------------------------------4 uzd.------------------------------------------------")

sweet_bag1 = Sweets(4, 10.5, 5)
sweet_bag2 = Sweets(5, 11.6, 4)
sweet_bag3 = Sweets(2, 8.2, 3)
sweet_bags = [sweet_bag1, sweet_bag2, sweet_bag3]

max_weight_sweet_bag = sweet_bags[0]
min_weight_sweet_bag = sweet_bags[0]
for s in sweet_bags:
    if s.weight > max_weight_sweet_bag.weight:
        max_weight_sweet_bag = s
    if s.weight < min_weight_sweet_bag.weight:
        min_weight_sweet_bag = s
print(f"Sunkiausias maišelis sveria: {max_weight_sweet_bag.weight}, kainuoja: {max_weight_sweet_bag.price} eur.")
print(f"Lengviausias maišelis kainuoja: {min_weight_sweet_bag.price} eur.")

sweet_tooth = SweetTooth(10.6)

for bag in sweet_bags:
    if sweet_tooth.money > bag.price:
        print(f"Samguris gali pirkti saldainius, kurių duomenys: {bag}")

sweet_tooth.money = sweet_tooth.money * 2

for bag in sweet_bags:
    if sweet_tooth.money > bag.price:
        print(f"Padvigubėjus kainai, samguris gali pirkti saldainius, kurių duomenys: {bag}")
