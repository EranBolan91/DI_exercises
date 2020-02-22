import json

class Cart():
    def __init__(self):
        self.total = 0

    def add_to_cart(self,petDict):
        file = open('cart.json','r')
        data = json.load(file)
        file.close()
        if not data:
            data.append(petDict)
        else:
            data = self.check_if_exist(data,petDict)

        file = open('cart.json','w+')
        file.write(json.dumps(data,indent=4))
        file.close()
        print('Cart data has updated')

    def get_cart(self):
        file = open('cart.json', 'r')
        data = json.load(file)
        file.close()
        return data

    def remove_item(self,cartID):
        file = open('cart.json','r')
        data = json.load(file)
        file.close()
        id = int(cartID)
        counter = -1
        for cart in data:
            counter += 1
            if cart['id'] == id:
                del data[counter]

        #data.append(cartData)
        file = open('cart.json','w')
        file.write(json.dumps(data,indent=4))
        file.close()

    def get_total(self):
        file = open('cart.json', 'r')
        data = json.load(file)
        file.close()
        for item in data:
            self.total += 1
        return self.total

    def check_if_exist(self,pet_list,pet_check):
        for pet in pet_list:
            if pet['id'] == pet_check['id']:
                 pet['quantity'] += 1
                 return pet_list

        pet_list.append(pet_check)
        return pet_list

    def get_total_sum(self,pet_list):
        sum = 0
        for pet in pet_list:
            sum += pet['price']*pet['quantity']
        return sum
