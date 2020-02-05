#Exercise 1 – Temperature Advice
#1. Create a function called get_random_temp()
import random

#this func i dont need because i use get_rnd_temp (because the user input is fall,summer,winter,spring)
# def check_the_season(degrees):
#     if degrees > -10 and degrees < 7:
#         return 'winter'
#     if degrees > 16 and degrees < 23:
#         return 'spring'
#     if degrees > 23 and degrees < 40:
#         return "summer"
#     if degrees > 7 and degrees < 16:
#         return 'fall'

# def get_rnd_temp(season):
#     if season == 'summer':
#         temp = get_rnd_num(25,40)
#     elif season == 'winter':
#         temp = get_rnd_num(-10, 7)
#     elif season == 'fall':
#         temp = get_rnd_num(7,16)
#     elif season == 'spring':
#         temp = get_rnd_num(16, 23)
#     return temp
#
# def get_rnd_num(degri1,degri2):
#        rnd = random.randrange(degri1,degri2)
#        return rnd
#
# def main():
#     season_input = input("Please enter the season (winter,summer,fall or spring) ")
#     temp = get_rnd_temp(season_input)
#     print(f"The temperature right now is {temp} degrees Celsius.")
    # if temp < 0:
    #     print("Brrr, that’s freezing! Wear some extra layers today")
    # elif temp > 0 and temp < 16:
    #     print("Quite chilly! Don’t forget your coat")
    # elif temp > 16 and temp < 23:
    #     print("Getting worm")
    # elif temp > 24 and temp < 32:
    #     print("Its hot! get your self a shirt")
    # elif temp > 32 and temp < 40:
    #     print("Guys its very hot, better go to the sea")
#main()


#Exercise 2 – Double Dice
# def throw_dice():
#     return random.randrange(1,6)
#
# def throw_until_doubles():
#     times = 1
#     cube1 = throw_dice()
#     cube2 = throw_dice()
#     while cube1 != cube2:
#         cube1 = throw_dice()
#         cube2 = throw_dice()
#         times += 1
#
#     return times
#
# def main():
#     list = []
#     sum = 0
#     for i in range(0,20):
#         list.append(throw_until_doubles())
#     for num in list:
#         sum = sum + num
#     avg = sum/20
#     print(f"Total throws: {sum}")
#     print(f"Average throws to reach doubles: {avg}")
#
# main()