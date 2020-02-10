#Exercice1
class Family():
    def __init__(self):
        self.members = [
            {'name': 'Michael', 'age': 35, 'sex': 'Male', 'is_child': False},
            {'name': 'Sarah', 'age': 32, 'sex': 'Female', 'is_child': False},
            {'name': 'Kevin', 'age': 16, 'sex': 'Male', 'is_child': True}
        ]
        self.last_name = ""

    def born(self,**kwargs):
            dic = {}
            for key,value in kwargs.items():
               dic.update(kwargs.items())
            self.members.append(dic)
            print("Mazal TOV!!")

    def is_18(self,name):
        for dic in self.members:
            if name in dic.values():
                if dic.get('age') > 18:
                    return True
                else:
                    return False

    def __repr__(self):
        for dic in self.members:
            print(dic.get('name') + " is " + str(dic.get('age')) + ' years old.' +
                  'Sex ' + dic.get('sex') + ' and his child type is: ' + str(dic.get('is_child')))


family = Family()
family.born(name='eran',age=1,sex='Male',is_child=True)
big = family.is_18('Sarah')
#family.__repr__()
#print(family.members)


#Exercice2

class IncredibleFamily(Family):
    def born(self,**kwargs):
        dic = {}
        for key, value in kwargs.items():
            dic.update(kwargs.items())
        self.members.append(dic)

    def user_power(self):
        for dic in self.members:
            if 'power' in dic.keys() and dic.get('age') > 18 :
                print(dic.get('name') + " has Power: " + dic.get('power'))
            else:
                print("You have no power here!!")

    def incredible_presentation(self):
        for dic in self.members:
            if 'power' in dic.keys():
                print(dic.get('name') + " is " + str(dic.get('age')) + ' years old.' +
                      'Sex ' + dic.get('sex') + ' and his child type is: ' + str(dic.get('is_child'))
                      + " And his super power is: " + dic.get('power')
                      + " And for the ending, the Incredible name: " + dic.get('incredible_name'))
            else:
                self.__repr__()

incredMember = IncredibleFamily()
incredMember.born(name='Bob',age=43,sex='Male',is_child=False,power='Strong',incredible_name='Mr.Incredible')
incredMember.born(name='Helen',age=40,sex='Female',is_child=False,power='Stretch ',incredible_name='Elastigirl')
incredMember.born(name='Dash',age=16,sex='Female',is_child=True,power='Stretch ',incredible_name='Dashiell')

# incredMember.user_power()
# incredMember.incredible_presentation()
#
# incredMember.born(name='Baby Jack',age=0,sex='Male',is_child=True,power='UnKnown power ',incredible_name='Baby Jack')
# incredMember.incredible_presentation()

#Exercise 3

class BankAccount():
    def __init__(self):
        self.owner = " "
        self.balance = 0

    def deposit(self,money_deposite):
        if money_deposite > 0:
            self.balance += money_deposite

    def withdraw(self,get_money):
        if get_money < self.balance:
            self.balance -= get_money


class Owner(BankAccount):
    def __init__(self,credit_card,password):
        self.credit_card = credit_card
        self.password = password
        self.password_times = 0

    def check_owner_info(self,creadit_num,password):
        if creadit_num == self.credit_card and password == self.password:
            print("Do you want to deposit or withdraw?")
        elif self.password_times == 2 :
            print("Sorry, the card is no longer for use, please contact your bank")
        else:
            print("Incorrect password, please try again")
            self.password_times += 1

    def deposit(self,money_deposite):
        if money_deposite >= 20 and money_deposite <= 100:
            self.balance += money_deposite
            print(f"You have deposite {money_deposite}, now you have {self.balance}")

    def withdraw(self,get_money):
        if get_money % 50 == 0 or get_money % 20 == 0:
            self.balance -= get_money
            print(f'Take your {get_money}, now you have left {self.balance}')

owner = Owner("4580",'123')
owner.check_owner_info("4580","123")
owner.deposit(100)
