from dataclasses import field


class Animal:
    height = None
    age = None
    hunger = 100
    thirst = 100
    health = 100

    def info(self):
        print("")
        print("---Your animal data---")
        print(f"Height : {self.height} cm")
        print(f"Age    : {self.age} years")
        print(f"Hunger : {self.hunger}%")
        print(f"Thirst : {self.thirst}%")
        print(f"Health : {self.health}%")
        print("")

    def eat(self):
        print("I am eating")
        self.hunger += 20

    def drink(self):
        print("I am drinking")
        self.thirst += 20

class Baby(Animal):
    def play(self):
        print("I am playing")
        self.hunger -= 10
        self.thirst -= 10
class Cat(Animal):
    def meow(self):
        print("Meow")

class Kitten(Cat, Baby):
    def baby_meow(self):
        print("Meeoow")
class Dog(Animal):
    def woof(self):
        print("Woof")

class Puppy(Dog, Baby):
    def baby_woof(self):
        print("Wooof")

#Cats

cat_doing = None
c = Cat()
c.age = 5
c.height = 120
c.info()
def doing_cat():
    cat_doing = input("What your cat will do? ")
    if cat_doing == "meow":
        c.meow()
        c.info()
    elif cat_doing == "eat":
        c.eat()
        c.info()
    elif cat_doing == "drink":
        c.drink()
        c.info()
doing_cat()

kit_doing = None
k = Kitten()
k.age = 1
k.height = 100
k.info()
def doing_kit():
    kit_doing = input("What your kitten will do? ")
    if kit_doing == "meow":
        k.baby_meow()
        k.info()
    elif kit_doing == "eat":
        k.eat()
        k.info()
    elif kit_doing == "drink":
        k.drink()
        k.info()
    elif kit_doing == "play":
        k.play()
        k.info()
doing_kit()

#Dogs

dog_doing = None
d = Dog()
d.age = 6
d.height = 110
d.info()
def doing_dog():
    dog_doing = input("What your dog will do? ")
    if dog_doing == "woof":
        d.woof()
        d.info()
    elif dog_doing == "eat":
        d.eat()
        d.info()
    elif dog_doing == "drink":
        d.drink()
        d.info()
doing_dog()

pup_doing = None
p = Puppy()
p.age = 1
p.height = 90
p.info()
def doing_pup():
    pup_doing = input("What your puppy will do? ")
    if pup_doing == "woof":
        p.baby_woof()
        p.info()
    elif pup_doing == "eat":
        p.eat()
        p.info()
    elif pup_doing == "drink":
        p.drink()
        p.info()
    elif pup_doing == "play":
        p.play()
        p.info()
doing_pup()