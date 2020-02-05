#Exercise 1
YEAR = 2020
MONTH = 10
day = 2

def get_age(year,month,day):
      if month > MONTH:
        age = YEAR - year - 1
      else:
        age = YEAR - year
      return age

def can_retire(sex,date_of_birth):
     args = list(map(int,date_of_birth.split('/')))
     month,day,year = args[0],args[1],args[2]
     age = get_age(year,month,day)
     if sex == 'm':
         if age > 67:
             return True
         else:
             return False

     else:
         if age > 62:
             return True
         else:
             return False

print(can_retire('f'),'1/5/1991')


#Exercise 3
contries = ()
def describe_city(city_name):

