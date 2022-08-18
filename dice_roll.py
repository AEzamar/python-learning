import random
class Dice:
    def roll(self):
        l_die = random.randint(1, 10)
        r_die = random.randint(1, 10)
        return l_die, r_die

dice = Dice()
print(dice.roll())