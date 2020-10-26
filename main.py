from subprocess import call 
import os 
def clear(): 
    call('clear' if os.name =='posix' else 'cls') 
clear()
#######################

from pet import Pet, CuddlyPet
from toy import Toy
### allows for information to be imported from the other pages so can be 
    ### used on this main page

# Begin with no pets.
pets = []
### main menu where it starts 
main_menu = [
    "Adopt a Pet",
    "Play with Pet",
    "Feed Pet",
    "View status of pets",
    "Give a toy to all your pets",
    "Do nothing",
    "Exit\n"
]
### after adoption it allows you to pick type of pet
adoption_menu = [
    "Pet",
    "Cuddly Pet"
]

### Catching Error, lets the user know if their seltions were not correct 
def print_menu_error():
    print("That was not a valid choice. Try again.\n\n\n")    

def choices_to_string(choice_list):
    choice_string = ""
    num = 1
    for choice in choice_list:
        choice_string += "%d: %s\n" % (num, choice)
        num += 1
    choice_string += "Please choose an option: "
    return choice_string

def get_user_choice(choice_list):
    choice = -1
    choice_string = choices_to_string(choice_list)
    while choice == -1:
        try:
            choice = int(input(choice_string))
            if choice <= 0 or choice > len(choice_list):
                raise ValueError
        except ValueError:
            print_menu_error()
    return choice

### Choose options to adopt and raise your pets
def main():    
    while True:
        choice = get_user_choice(main_menu)
        if choice == 1:
            pet_name = input("What would you like to name your pet? ")
            print("Please choose the type of pet:")
            type_choice = get_user_choice(adoption_menu)
            if type_choice == 1:
                pets.append(Pet(pet_name))
                print ("Good choice, these pets are great to start your journey as pet owner.\n")
            elif type_choice == 2:
                pets.append(CuddlyPet(pet_name))
                print ("Great choice, these pets are great for one's mental health and great anxiety reducers. But they do require lots of attention.\n")
            print("You now have %d pets.\n" % len(pets))
### first part of the main menu
    #### when a choice is made it starts the loop of choices 

        elif choice == 2:
            for pet in pets:
                pet.get_love()
                if pet.happiness >= 8 and pet.happiness <10:
                    print (f"{pet_name}, is very happy, may want rest a bit. \n")
                elif pet.happiness >= 10:
                    print (f"{pet_name} is very tired and needs to rest. \n")
                
        elif choice == 3:
            for pet in pets:
                pet.eat_food()
                if pet.fullness >= 8 and pet.fullness < 10:
                    print (f"{pet_name}, is statisfied, you can stop feeding it. \n")
                elif pet.fullness >= 10:
                    print (f"{pet_name} has over eatten, and now needs to sleep. \n")

        elif choice == 4:
            for pet in pets:
                print(pet)

        elif choice == 5:
            for pet in pets:
                pet.get_toy(Toy())

        elif choice == 6:
            # Pet levels naturally lower.
            for pet in pets:
                pet.be_alive()
                if pet.happiness <= 3 and pet.happiness > 0:
                    print(f"{pet_name} is sad, you may want to play with your pet.\n")
                elif pet.fullness <= 3 and pet.fullness > 0:
                    print(f"{pet_name} is hungry, you may want to feed your pet.\n")
                elif pet.fullness <= 0:
                    print (f"{pet_name}, has died of hunger. Expect a call from the authorities!!!\n")
                    break
                elif pet.happiness <= 0:
                    print (f"{pet_name}, has run away, you may want to reflect of your life choices!\n")
                    break
            ### when this choice is made, depending on the level pet is already, parameter is set to notify the user of pets health and happiness.

        elif choice == 7:
            print ("Thanks for playing, tell your friends! \n")
            break
        #### Allows for the program to end, without going back to endless loop of the main menu.
    
main()