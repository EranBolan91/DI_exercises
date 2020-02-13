import json

class MenuManager:
    def __init__(self):
         with open('restaurant_menu.json','r') as f:
             data = json.load(f)
             self.menu = data

    @save_to_file_decorator
    def add_item(self,name,price):
        newItemDic = {'name':name,'price':price}
        self.menu['items'].append(newItemDic)

    def remove_item(self,name):
        items = len(self.menu['items'])
        for index in range(items):
            if name == self.menu['items'][index]['name']:
                self.menu['items'].pop(index)
                return True
        return False

    def update_item_price(self,name,price):
        items = len(self.menu['items'])
        for index in range(items):
            if name == self.menu['items'][index]['name']:
                self.menu['items'][index]['price'] = price
                print(self.menu['items'][index])

    def save_to_file(self):
        with open('restaurant_menu.json', 'w') as f:
            json.dump(self.menu, f)

    def save_to_file_decorator(self, func):
        def wrapper():
            func()
            self.save_to_file()
            print('file saved')
        return wrapper

    def __repr__(self):
        text = """"""
        for index in self.menu['items']:
            for key,value in index.items():
                text += f"{key}: {value} \n"
        return text


