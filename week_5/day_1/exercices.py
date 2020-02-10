class Dog:
    def __init__(self,nameDog,heightDog):
        self.nameDog = nameDog
        self.heigthDog = heightDog

    def talk(self):
        print("Wouaffff")

    def jump(self):
        print(f"Dogs heigth: {self.heigthDog * 2}")

    def fight(self,anoterDog):
        if self.heigthDog > anoterDog.height:
            return self
        else:
            return anoterDog



davidDogs = Dog('Rex',50)
print(davidDogs.jump())

sarahDogs = Dog('Teacup',20)
print(sarahDogs.nameDog + " " + str(sarahDogs.heigthDog))

if davidDogs.heigthDog > sarahDogs.heigthDog:
    davidDogs.winner = True
else:
    sarahDogs.winner = True

winner = davidDogs.fight(sarahDogs)
print(f'The winner is {winner.nameDog}')


class Zero:
    def __init__(self,zooName):
        self.animals = []
        self.name

    def addAnimal(self,newAnimal):
        for animal in self.animals:
            if newAnimal != animal:
                self.animals.append(newAnimal)
            else:
                print(f'Animal {newAnimal} is already exist')

    def getAnimals(self):
        return self.animals

    def sellAnimal(self,nameAnimal):
        for index,animal in enumerate(self.animals):
            if animal == nameAnimal:
                self.animals.remove(index)
                print(f'Goodbye {nameAnimal}, You have been sold!')

    def sortAnimal(self,animals):
        sorted_animals = self.animals.sort()
        print(sorted_animals)
        temp = 0
        pen = {}
        for x,y in zip(animals[::],animals[1::]):
            if x[0] == y[0]:
                pen[temp] = [x,y]
            else:
                temp += 1
                pen[temp] = (x)
                pen[temp] = (y)
        print(pen)


