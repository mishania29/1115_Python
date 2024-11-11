from dataclasses import field
import random

class Animal:
    height = None
    age = None
    hunger = int(100)
    thirst = int(100)
    healthy = int(100)

    def info(self):
        print("")
        print("---Your animal data---")
        print(f"Height : {self.height} cm")
        print(f"Age    : {self.age} years")
        print(f"Hunger : {self.hunger}%")
        print(f"Thirst : {self.thirst}%")
        print(f"Health : {self.healthy}%")
        print("")

    def eat(self):
        print("I am eating")
        self.hunger += 20

    def drink(self):
        print("I am drinking")
        self.thirst += 20

#Others

class ReptilesIMammals(Animal):
    def run(self):
        print("I am running")
        self.hunger -= 5
        self.thirst -= 10

    def walk(self):
        print("I am walking")
        self.hunger -= 2.5
        self.thirst -= 5

class Poisony(Animal):
    poisoned = 0
    def Poison(self):
        print("I am poisoning someone")
        self.poisoned += 1
        self.healthy -= 2.5

#Fishes

class Fish(Animal):
    def swim(self):
        print("I am swimming")
        self.hunger -= 10
        self.thirst -= 10

    def BoolBool(self):
        print("Bool bool bool...")


class GoldenFish(Fish):
    wishes = 0
    def spent_wishes(self):
        print("Your wish is... Granted!")
        self.wishes += 1

class FuguFish(Fish, Poisony):
    def pout(self):
        print("I am pouting!")
        self.height += 20

#Reptiles

class Reptile(Animal, ReptilesIMammals):
    def DropTail(self):
        print("I droped my tail")
        self.healthy -= 10


class Salamandra(Reptile, Poisony):
    pass

class Chameleon(Reptile):
    color = "Green"
    def ChangeColor(self):
        ch = random.randint(1, 5)
        if ch == 1:
            self.color == "Green"
        elif ch == 2:
            self.color == "Yellow"
        elif ch == 3:
            self.color == "Red"
        elif ch == 4:
            self.color == "Blue"
        elif ch == 5:
            self.color == "Brown"

#Mammals
class Mammal(Animal, ReptilesIMammals):
    def DrinkMilk(self):
        print("I am drinking milk")
        self.hunger -= 10
        self.thirst -= 30


class Bear(Mammal):
    def EatHoney(self):
        print("I am eating honey")
        self.hunger -= 20
        self.thirst += 5

class Human(Mammal):
    def Talk(self):
        print("Bla bla bla...")
