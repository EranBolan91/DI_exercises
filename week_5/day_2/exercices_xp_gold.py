import random
class ForceWielder():
    def __init__(self,name):
        self.power = random.randint(1,16)
        self.wisdom = random.randint(1, 16)

    def train(self):
        pass
    def fight(self,fighter1,fighter2):
          pass
          #TODO: need to check what is the meaning of "highest harmonic mean between power and wisdom"
    def isJedi(self):
        pass

class Jedi(ForceWielder):
    lightsaber = ""
    def set_light_saber_color(self):
        if self.wisdom > self.power:
            self.lightsaber = "Green Saber"
        elif self.wisdom < self.power:
            self.lightsaber = "Blue Saber"
        elif self.wisdom == self.power:
            self.lightsaber = "Violet Saber"
        print(self.lightsaber)

    def train(self):
        self.wisdom += random.randint(10,21)
        self.power += random.randint(5,15)

    def isJedi(self):
        return True

class Sith(ForceWielder):
    lightsaber = "RED"

    def train(self):
        self.wisdom += random.randint(5,15)
        self.power += random.randint(10,20)

    def isJedi(self):
        return False




