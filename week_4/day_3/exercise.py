#Exercise 1
#Given two variables a and b that you need to define, make a program that print Hello World only if a is greater than b
# a = 5
# b = 3
# if(a > b):
#     print("Hello world")


#Exercise 2
#Take three numbers from the user and print the greatest number.
# num1 = input("Please enter the first number ")
# num2 = input("Please enter the second number ")
# num3 = input("Please enter the third number ")
#
# list = [num1,num2,num3]
# list.sort()
# print("The greatest number is: " + list[-1])

#Exercise 3
#Ask to the user to insert a month (from 1 to 12) and display the season of the month inserted

# month = int(input("Please enter the number of month (1-12) "))
# spring = [3,4,5]
# summer = [6,7,8]
# autumn = [9,10,11]
# winter = [12,1,2]
#
# if month in spring:
#     print("Spring runs from March (3) to May (5)")
# elif month in summer:
#     print("Summer runs from June (6) to August (8)")
# elif month in autumn:
#     print("Autumn runs from September (9) to November (11)")
# elif month in winter:
#     print("Winter runs from December (12) to February (2)")


#Exercise 4
#Write a Python program to check whether an alphabet is a vowel or consonant.

#Exercise 5
#Write a Python program to guess a number between 1 to 9.

#Exercise 6
#Use a for loop to print the numbers from 1 to 20, inclusive.

# for i in range(1,21):
#     print(i)

#Exercise 7
# Make a list of the numbers from one to one million, and then use a for loop to print the numbers.
# (If the output is taking too long, stop it by pressing ctrl-C or by closing the output window.)
# numbers = []
# for i in range(0,100000000):
#     numbers.append(i)
#
# for j in numbers:
#     print(j)

#Exercise 8
# Make a list of the numbers from one to one million, and then use min() and max()
# to make sure your list actually starts at one and ends at one million
# Also, use the sum() function to see how quickly Python can add a million numbers .


# Exercise 9
#Draw the following pattern using for loops:
# star = ""
# for i in range(0,5):
#     star = star + "*"
#     print(star)

# Exercise 10
# Write a program that returns the index of the first occurrence of an item in a list.
# list = [4,5,6,6,3,4,2]
# for index, value in enumerate(list):
#     print(index)
#     break

# Exercise 11
# Write a little program that concatenate two lists together without using the + sign.
# list1 = [34,3423,'hello','world',56]
# list2 = [34,3423,'you','are',56,'my']
# joined = [*list1,*list2]
# print(joined)

#Exercise 12
#Write a loop that prompts the user to enter a series of pizza toppings until they enter a ‘quit’ value .
#As they enter each topping, print a message saying you’ll add that topping to their pizza .

# while 6:
#     user_input = input("Please enter your topping for the pizza, if you want to end - type 'quit' ")
#     if(user_input == 'quit'):
#         print("Bye bye")
#         break
#     print("You have added " + user_input +" To your pizza")

#Exercise 13
#A movie theater charges different ticket prices depending on a person’s age .
#If a person is under the age of 3, the ticket is free; if they are between 3 and 12,
#the ticket is $10; and if they are over age 12, the ticket is $15 .
#Write a loop in which you ask users their age, and then tell them the cost of their movie ticket
# while 1:
#     age = int(input("Pleaser enter your age - to end the progrem - enter '-1' "))
#     if age == -1:
#         break
#     if 3 < age and age < 12:
#         print("Your ticket will be 10$")
#     elif age > 12:
#         print("Your ticket will be 15$")


# Exercise 14
# Given a list, use a while loop to print out every elements from the end to the beginning.
# list = [324,5645,342,55,34,'asds','23222','bioo',222]
# index = 0
# line = ""
# while index < len(list):
#     line += str(list[index])
#     index +=1
# print(line)

#Exercice 15
#1) Create a dictionary call store. Inside this variable, translate this information into keys and values

store ={
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women","children", "home"],
    "international_competitors":[ "Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {"France": ["blue"], "Spain": ["red"], "US":["pink", "green"]}
}

#2)Change the number of stores to 2
# store["number_stores"] = 2

#3)Print a sentence that explains who the clients of Zara are
# print(store["type_of_clothes"])

#4) Add this information country_creation: Spain
#store.update({"country_creation":"spain"})

#5)If the key international_competitors is in the dictionary, add the store Desigual
# if "international_competitors" in store:
#     store["international_competitors"] = [store['international_competitors'],'Desigual']
print(store)

#6)Delete the information about the date of creation
store[creation_date]