import random


class Human:
    def __init__(self, name, car=None, job=None):
       self.name = name
       self.house = House()
       self.car = car
       self.job = job
       self.money = 100

    def work(self):
        self.money += 40
        print("Я сьогодгі працюю")

    def eat(self):
        self.house.food -= random.randint(1,10)
        self.house.pollution += random.randint(1,5)
        print("Я поїв")

    def shopping(self):
        self.money -= random.randint(1, 10)
        self.house.food += random.randint(1, 10)
        if self.car == None:
            print("Я пішов в магазин пішки")
        else:
            if self.car.drive(random.randint(1,10)*10):
                print("Ми поїхали в магазин")
            else:
                print("Я пішов в магазин пішки")


    def chill(self):
        self.money -= random.randint(10, 20)
        self.house.pollution += random.randint(1, 5)
        print("Я гарно відпочив")

    def cleaning(self):
        pass

    def info(self):
        print(f"Гроші - $ {self.money}")
        print(self.house)
        if self.car != None:
            print(self.car)

    def live(self, day):
        print(f"День №{day}")
        choice = random.randint(1, 4)
        if choice == 1:
            self.work()
        elif choice == 2:
            self.shopping()
        elif choice == 3:
            self.eat()
        elif choice == 4:
            self.chill()

        if self.money > 1000:
            print("Купляємо авто!")
            self.money -= 500
            self.car = Car("Lamborgini Urus 2022")

        self.info()
        print()

    def is_alive(self):
        if self.money < 0:
            return False
        else:
            return True

class House:
    def __init__(self):
        self.food = 0
        self.pollution = 0

    def __str__(self):
        return f"Інформація про будинок: їжа - {self.food}, забруднення - {self.pollution}"

class Car:
    def __init__(self, model):
        self.model = model
        self.fuel = 40    # l
        self.state = 100  # %

    def drive(self, length):
        rashod = length * 0.1
        if self.fuel - rashod < 0:
            print("Подорож не можлива, не вистачає пального")
            return False
        else:
            print(f"Ми проїхали {length} км, втратили {rashod} л пального")
            self.fuel -= rashod
            self.state -= length * 0.01
            return True

    def add_fuel(self, fuel):
        if self.fuel + fuel <= 40:
            self.fuel += fuel
        else:
            self.fuel = 40

    def __str__(self):
        return f"Авто {self.model}\nБензин - {self.fuel} л, стан - {int(self.state)} %"




class Job:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Професія: {self.name}, зарплатня - {self.salary}"



# car = Car("Lamborgini Urus 2022")
# print(car.drive(100))
# print(car.drive(10000))
# print(car)


job = Job("Programmer", 1000)
human = Human(input("Ім'я: "), job=job)
for day in range(366):
    if human.is_alive() == False:
        break
    human.live(day)