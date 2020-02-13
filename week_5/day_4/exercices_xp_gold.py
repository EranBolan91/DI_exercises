import menu_manager

def load_manager():
    menuManager = menu_manager.MenuManager()
    return menuManager

def show_user_menu():
    menu_string = """
    MENU
  (a) Add an item
  (b) Delete an item
  (c) View the menu
  (u) Update item
  (x) Exit 
    """
    print(menu_string)

def add_item_to_menu(menu):
    dish_name = input("Please enter the dish name ")
    dish_price = input("Please enter the dish price ")
    #menu.add_item(dish_name,dish_price)
    menu.save_to_file_decorator(add_item_to_menu)
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

def update_item(menu):
    name = input("Please enter the dish you want to update its price ")
    price = input("Enter the price of the item ")
    menu.update_item_price(name,price)

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
    if choose == 'u' or choose == 'U':
        update_item(menu)



menu = load_manager()
exit = ""
while exit != 'x':
    exit = main_menu(menu)