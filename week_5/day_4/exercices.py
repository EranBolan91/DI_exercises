import random
import menu_manager
def get_words_from_file():
    text = open("sowpods.txt","r")
    newText = text.read().split('\n')
    return newText

def get_random_sentence(length):
    sentence = []
    words_list = get_words_from_file()
    for x in range(length):
        rnd = random.randrange(1,len(words_list))
        sentence.append(words_list[rnd].lower())
    space = " "
    return space.join(sentence)

def main():
    print("Hello and welcome to RANDOM SENTENCE GENERATOR!")
    print("The computer creates for you sentences by telling him how many words you want")
    leng = int(input("Please enter a number between 2 - 20, this number will be the length of the sentence "))
    if leng > 20 or leng < 2:
        print("Incorrect length, BYE BYE ")
    else:
        sentence = get_random_sentence(leng)
        print(sentence)

#main()

#Exercise 2 – Restaurant Menu Manager

def load_manager():
    menuManager = menu_manager.MenuManager()
    return menuManager

def show_user_menu():
    menu_string = """
    MENU
  (a) Add an item
  (b) Delete an item
  (c) View the menu
  (x) Exit 
    """
    print(menu_string)

def add_item_to_menu(menu):
    dish_name = input("Please enter the dish name ")
    dish_price = input("Please enter the dish price ")
    #menu_manager.menu.add_item(dish_name,dish_price)
    menu.add_item(dish_name,dish_price)
    print("Item has added successfully")


def remove_item_from_menu(menu):
    dish_name = input("Please enter the dish name you want to remove from the menu ")
    isDeleted = menu.remove_item(dish_name)
    if isDeleted:
        print(f"{dish_name} has deleted")
    else:
        print(f"Some problem has occurred, {dish_name} has not deleted")

def show_restaurant_menu(menu):
    print(menu.__repr__())

def saveChanges(menu):
    menu.save_to_file()


def main_menu(menu):
    show_user_menu()
    choose = input("What you wish to do ")
    if choose == 'a' or choose == 'A':
        add_item_to_menu(menu)
    if choose == 'b' or choose == 'B':
        remove_item_from_menu(menu)
    if choose == 'c' or choose == 'C':
        show_restaurant_menu(menu)
    if choose == 'x' or choose == 'X':
        saveChanges(menu)
        return 'x'


# menu = load_manager()
# exit = ""
# while exit != 'x':
#     exit = main_menu(menu)


#Exercice 3

class Currency:
    def __init__(self,currency,label):
        self.currency = currency
        self.label = label

    def str(self,currency):
        pass
    def repr(self,currency):
        pass
    def int(self,currency):
        pass