
### Parent
class Pet:
    def __init__(self, name, fullness=5, happiness=5, hunger=3, mopiness=2):
        self.name = name
        self.fullness = fullness
        self.happiness = happiness
        self.hunger = hunger
        self.mopiness = mopiness
        self.toys=[]
        #### Attributes = sillmilar to keys, its able to be pulled later on.
    def eat_food(self):
        self.fullness += 2
    #### when pet is fed the points will increase by 2
    def get_love(self):
        self.happiness += 2
    #### when pet is played with the points will increase by 2
    def be_alive(self):
        self.fullness -= self.hunger
        self.happiness -= self.mopiness  
        for toy in self.toys:
            self.happiness += toy.use()
    #### when pet is ignored the points will decrease by the pre-determined amount       
    def get_toy(self, toy):
        self.toys.append(toy)
        for toy in self.toys:
            self.happiness += toy.use()
    #### when pet is given a toy the points will increase the pre-determined amount
    def __str__(self):
        return """
        %s:
        Fullness: %d
        Happiness: %d
        """ % (self.name, self.fullness, self.happiness)
    #### will display the stats of the pets
    
#####Child
class CuddlyPet(Pet):
    def __init__(self, name, fullness=5, hunger=3, cuddle_level=1, mopiness= 3):
        super().__init__(name, fullness, 5, hunger, mopiness)
        self.cuddle_level = cuddle_level

    def be_alive(self):
        self.fullness -= self.hunger
        self.happiness -= self.mopiness
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