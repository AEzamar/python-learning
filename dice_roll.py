import random
class Dice:
    def roll():
        l_die = random.randint(1, 10)
        r_die = random.randint(1, 10)
        return l_die, r_die

print(Dice.roll())