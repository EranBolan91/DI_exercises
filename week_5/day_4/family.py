class Family:

    def __init__(self, members, last_name):
        self.members = members
        self.last_name = last_name

    def born(self, **kwargs):
        self.members[kwargs["name"]] = kwargs
        print(f"Mazel tov for the birth of {kwargs.get('name')} !")

    def is_18(self, name):
        if self.members.get(name):
            member = self.members.get(name)
            return member["age"] >= 18
        else:
            raise KeyError(f"{name} was not found in family")


class Incredibles(Family):

    def use_power(self, name):
        member = self.members.get(name)
        if member:
            power = member.get('power')
            if self.is_18(name):
                print(f"{member['incredible_name']} uses {power} !!")
            else:
                raise Exception("You are not old enough to do this, go to your room")
        else:
            raise KeyError(f"{name} was not found in family")


if __name__ == '__main__':
    fam_dic = {
        'Michael': {'name': 'Michael', 'age': 35, 'sex': 'Male', 'is_child': False, },
        "Sarah": {'name': 'Sarah', 'age': 32, 'sex': 'Female', 'is_child': False},
        "Kevin": {'name': 'Kevin', 'age': 16, 'sex': 'Male', 'is_child': True}
    }
    family = Family(fam_dic, "Cohen")
    print(family.members)

    zach = {"name": "Zachariah", 'age': 0,
            'sex': 'Male', 'is_child': True,
            'eye_color': 'blue', 'hair_color': 'red'}
    family.born(**zach)
    print(family.members)

    print(family.is_18('Michael'))
    fam_dic = {
        'Michael': {'name': 'Michael', 'age': 35,
                    'sex': 'Male', 'is_child': False,
                    'incredible_name': 'Mr Michael', 'power': 'super-strength'},
        "Sarah": {'name': 'Sarah', 'age': 32, 'sex': 'Female', 'is_child': False},
        "Kevin": {'name': 'Kevin', 'age': 16, 'sex': 'Male', 'is_child': True}
    }

    inc = Incredibles(fam_dic, last_name='Smith')

    inc.born(name='Jack', age=0, sex="Male",
             is_child=True, incredible_name='SuperBabyJack',
             power='Unknown Power')

    print(inc.members)

    inc.use_power('Michael')
    inc.use_power('Jack')