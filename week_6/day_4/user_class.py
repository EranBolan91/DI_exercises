import random , string , json


class User():

    def save_user_in_db(self,name,email,password):
        id = self.id_generator(6)
        file = open('users.json', 'r')
        data = json.load(file)
        file.close()

        user_dic = {"id": id,
                    "name": name,
                    "email": email,
                    "password": password}
        data.append(user_dic)
        file = open('users.json', 'w+')
        file.write(json.dumps(data, indent=4))
        file.close()
        print("New user added")

    def login(self,email,password):
        file = open('users.json', 'r')
        data = json.load(file)
        file.close()

        for user in data:
            if user['email'] == email and user['password'] == password:
                return True
        return False



    def id_generator(self,size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))