class MenuManager():
    def __init__(self):
        self.menu = {}

    def add_item(self,name,price,spice,gluten):
        self.menu[name] = {'name':name,'price':price,'spice':spice,'gluten':gluten}

    def update_item(self,name,price,spice,gluten):
        if name in self.menu:
            self.menu[name] = {'name':name,'price':price,'spice':spice,'gluten':gluten}
        else:
            print("Send message to the manager")

    def remove_item(self,name):
        if name in self.menu:
            del self.menu[name]
            print(self.menu)
        else:
            print("Send message to the manager")

menu = MenuManager()
# menu.add_item('fish',30,'A',True)
# menu.add_item('Pasta',55,'B',False)
# menu.add_item('Pizza',43,'C',True)
# menu.update_item('Hamburger',100,"B",False)
# menu.remove_item("fish")

#Exercice 2
class Farm():
        def __init__(self,farmName):
            self.farmName = farmName
            self.animals = {}

        def addAnimal(self,animal,num=1):
            self.animals[animal] = self.animals.get(animal,0) + num

        def getInfo(self):
            print(self.farmName +"'s farm")
            for key,value in self.animals.items():
                if value == 1:
                    print(key + " : " +str(value))
                else:
                    print(key + "s" + " : " + str(value))
            print("E-I-E-I-O!")

        def get_animal_type(self):
            animal_list = []
            for animal in self.animals.keys():
                animal_list.append(animal)
            animal_list.sort()
            return animal_list

        def get_short_info(self):
            animal_list = self.get_animal_type()
            str = ""
            for animal in animal_list:
                str += animal +","
            print(self.farmName +"'s farm has " + str)

farm = Farm("Macdonald")
farm.addAnimal("cow",4)
farm.addAnimal("sheep")
farm.addAnimal("sheep")
farm.addAnimal("sheep")
farm.addAnimal("horse")
farm.getInfo()
print(farm.get_animal_type())
farm.get_short_info()






