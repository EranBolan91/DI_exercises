
birthday = input("Please enter your birthday date in that format DD/MM/YYYY ")

year = int(birthday.split("/")[-1])
age = str(2020-year)
print(age)
candels = int(age[-1])
print(candels)


cake = f'''
      ___{"i"*candels}___
      |:H:a:p:p:y:|
    __|___________|__
   |^^^^^^^^^^^^^^^^^|
   |:B:i:r:t:h:d:a:y:|
   |                 |
   ~~~~~~~~~~~~~~~~~~~
'''
print(cake)
