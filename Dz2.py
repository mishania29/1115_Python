import random
class Cat:

    def __init__(self):
        self.name = input("What is your cat name? ")
        self.gladness = 20
        self.hunger = 20
        self.energy = 50
        self.alive = True

    def eat(self):
        print(f"{self.name} кушає")
        self.hunger += 8
        self.gladness += 2
        self.energy += 3

    def sleep(self):
        print(f"{self.name} спить")
        self.gladness += 2
        self.energy += 8
        self.hunger -= 8

    def chill(self):
        print(f"{self.name} гуляє")
        self.gladness += 3
        self.energy -= 3
        self.hunger -= 3

    def info(self):
        print(f"Данні {self.name}: ")
        print(f"Щастя    : {self.gladness}")
        print(f"Голод    : {self.hunger}")
        print(f"Енергія  : {self.energy}")

    def do(self):
        self.info()
        doing = input("What your cat will do? ")
        if doing == "eat":
            self.eat()
        elif doing == "sleep":
            self.sleep()
        elif doing == "chill":
            self.chill()

cat = Cat()
while True:
    cat.do()