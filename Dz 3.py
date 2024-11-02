class Student:

    def __init__(self, name):
        self.name = name
        self.gladness = 20
        self.progress = 0
        self.energy = 50
        self.money = 10
        self.alive = True

    def study(self):
        print(f"{self.name} навчається")
        self.progress += 2
        self.gladness -= 2
        self.energy -= 3

    def sleep(self):
        print(f"{self.name} спить")
        self.gladness += 2
        self.energy += 5

    def chill(self):
        print(f"{self.name} гуляє")
        self.gladness += 3
        self.energy -= 3
        self.progress -= 1
        self.money -= 2

    def work(self):
        print(f"{self.name} працює")
        self.gladness -= 3
        self.energy -= 3
        self.progress += 1
        self.money += 5

    def info(self):
        print(f"Сьогодні {self.name} має: ")
        print(f"Щастя    : {self.gladness}")
        print(f"Знання   : {self.progress}")
        print(f"Енергія  : {self.energy}")
        print(f"Гроші    : {self.money}")

    def is_alive(self):
        if self.progress < 0:
            print("Я занадто глупий щоб жити у цьому світі")
            self.alive = False
        if self.gladness < 0:
            print("У мене депресія на все життя...")
            self.alive = False
        if self.energy < 0:
            print("Я настілки втомлений що не можу жити...")
            self.alive = False
        if self.progress > 100:
            print(f"У {self.name} вибухнула голова!")
            self.alive = False
        if self.gladness > 100:
            print(f"{self.name} улетів в космос від такої радості!")
            self.alive = False
        if self.energy > 100:
            print(f"{self.name} перетворився у ядерну бомбу від такої eнергії")
            self.alive = False
        if self.money > 100:
            print(f"{self.name} занадто богатий")
            self.alive = False
        if self.money < 0:
            print(f"{self.name} залишився безгрошів...")
            self.alive = False

    def live(self,day):
        print(f"День №{day}  з життя {self.name}")
        print("-"*30)
        if self.progress < 6:
            self.study()
        elif self.progress > 94:
            self.chill()
        elif self.gladness < 6:
            self.chill()
        elif self.gladness > 94:
            self.study()
        elif self.energy < 6:
            self.sleep()
        elif self.energy > 94:
            self.chill
        elif self.money < 6:
            self.work()
        elif self.money > 94:
            self.chill()
        self.info()
        self.is_alive()
        print()

st = Student("Хасан")
for d in range(1, 366):
    if st.alive == False:
        break
    st.live(d)