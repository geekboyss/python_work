from random import randint

class Die():
    def __init__(self, sides = 6):
        self.sides = sides

    def roll_die(self):
        print(randint(1,self.sides))


d1 = Die(10)
d1.roll_die()
d1.roll_die()
d1.roll_die()
d1.roll_die()
d1.roll_die()
d1.roll_die()
d1.roll_die()
d1.roll_die()
d1.roll_die()
d1.roll_die()



