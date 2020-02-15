from game import Game

def get_user_menu_choice():
    menu_string = """
         Menu:
         (g) Play a new game
         (x) Show scores and exit
            """
    user_input = input(menu_string)
    if user_input == "g" or user_input == "G":
        return True
    elif user_input == "x" or user_input == "X":
        return False


def print_results(results):
    display_string = """"""
    for key,value in results.items():
        display_string += f"{key}: {value} \n"
    print(display_string)

win = 0
lose = 0
draw = 0
def play():
    game = Game()
    user_input = game.get_user_item()
    computer_input = game.get_computer_item()
    game_status = game.get_game_result(user_input,computer_input)
    if game_status == 'draw':
        print(f"You selected {user_input} , Computer select {computer_input}  - Its a draw!")
    elif game_status == 'win':
        print(f"You selected {user_input} , Computer select {computer_input}  - You win!")
    else:
        print(f"You selected {user_input} , Computer select {computer_input}  - You lose!")

def main():
    while exit:
       if get_user_menu_choice():
           play()

main()