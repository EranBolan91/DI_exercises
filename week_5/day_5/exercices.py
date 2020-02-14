import random
# Exercise1: Revision on list comprehension
# 1. Create a list of random numbers from 10 to 20
# 2. Create another list that will contain only the numbers divisible by 3
# 3. Create another list that will contain only the numbers divisible by the length of the original list
# 4. Create another list that will contain only the numbers bigger than 12
# 5. Create another list that will contain all the numbers squared
# 6. Create another list that will contain all the numbers that are not duplicates

#1)
list = []
for i in range(10):
    list.append(random.randint(10,21))
print(list)

#2)
divisible_by_three_list = []
for num in list:
    if num % 3 == 0:
        divisible_by_three_list.append(num)
print(divisible_by_three_list)

#3)
divisible_by_length_list = []
list_length = len(list)
for num in list:
    if num % list_length:
        divisible_by_length_list.append(num)
print(divisible_by_length_list)

#4)
higher_then_twelve = []
for num in list:
    if num > 12:
        higher_then_twelve.append(num)
print(higher_then_twelve)

#5)
squared_list = []
for num in list:
    pass
print(squared_list)

#6)
not_duplicate_list = {}
for num in list:
    not_duplicate_list.add(num)
print(not_duplicate_list)
