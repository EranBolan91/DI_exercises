import json

class Pet():
    def getAllPets(self):
        with open('pets.json','r') as f:
            data = json.load(f)
            petLists = []
            for pet in data['pets']:
                petLists.append(pet)
        return petLists

    def getPet(self,id):
        pets = self.getAllPets()
        for pet in pets:
           if pet['id'] == int(id):
               return pet
        return False