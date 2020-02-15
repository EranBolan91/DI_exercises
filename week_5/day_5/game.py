import random
class Game:
    def __init__(self):
        self.win = 0
        self.lose = 0
        self.draw = 0

    def get_user_item(self):
        while True:
           user_input = input("Choose your item - (r)ock (p)aper (s)cissors ")
           if user_input == "r" or user_input == "p" or user_input == "s":
              return user_input
           else:
             print("Invalid input - please enter only r / p / s letters")
             print('\n')

    def get_computer_item(self):
        list = ['r','p','c']
        rnd = random.choice(list)
        return rnd

    def get_game_result(self,user_item,computer_item):
        if user_item == computer_item:
            return "draw"
        elif user_item == 'r' and computer_item == 's':
            return 'win'
        elif user_item == 's' and computer_item == 'p':
            return 'win'
        elif user_item == 'p' and computer_item == 'r':
            return 'win'
        elif user_item == 'r' and computer_item == 'p':
            return 'lose'
        elif user_item == 's' and computer_item == 'r':
            return 'lose'
        elif user_item == 'p' and computer_item == 's':
            return 'lose'