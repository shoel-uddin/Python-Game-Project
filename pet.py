
### Parent
class Pet:
    def __init__(self, name, fullness=50, happiness=50, hunger=5, mopiness=5):
        self.name = name
        self.fullness = fullness
        self.happiness = happiness
        self.hunger = hunger
        self.mopiness = mopiness
        self.toys=[]

    def eat_food(self):
        self.fullness += 30

    def get_love(self):
        self.happiness += 30
    
    def be_alive(self):
        self.fullness -= self.hunger
        self.happiness -= self.mopiness  
        for toy in self.toys:
            self.happiness += toy.use()
            
    def get_toy(self, toy):
        self.toys.append(toy)

    def __str__(self):
        return """
        %s:
        Fullness: %d
        Happiness: %d
        """ % (self.name, self.fullness, self.happiness)

#####Child
class CuddlyPet(Pet):
    def __init__(self, name, fullness=50, hunger=5, cuddle_level=1):
        super().__init__(name, fullness, 100, hunger, 1)
        self.cuddle_level = cuddle_level

    def be_alive(self):
        self.fullness -= self.hunger
        self.happiness -= self.mopiness/2
        for toy in self.toys:
            self.happiness += toy.use()
    
    def cuddle(self, other_pet):
        for i in range(self.cuddle_level):
            other_pet.get_love()


# ##Based of Primary
# print ("*********Parent********")
# cujo= Pet("Cujo")
# cujo.eat_food()
# print (cujo.fullness)
# #80
# print (cujo.happiness)
# #50

# benji = CuddlyPet("Benji", 50, 20)
# print(benji.fullness, benji.happiness)
# # 50 20
# benji.be_alive()
# print(benji.fullness, benji.happiness)
# # 30 19


# ##Based on Secondary 
# print ("********Child*******")
# benji = CuddlyPet("Benji", 50, 20)
# cujo = Pet("Cujo", 50, 10, 30, 10)
# print(cujo.happiness)
# # 10
# benji.cuddle(cujo)
# print(cujo.happiness)
# # 40