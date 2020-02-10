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
menu.add_item('fish',30,'A',True)
menu.add_item('Pasta',55,'B',False)
menu.add_item('Pizza',43,'C',True)
menu.update_item('Hamburger',100,"B",False)
menu.remove_item("fish")







