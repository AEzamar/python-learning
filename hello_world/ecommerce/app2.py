import random
for i in range(3):
    print(random.random())
    print(random.randint(10, 20))


members = ["John", "Mary", "Mosh", "Bob"]
leader = random.choice(members)
print(leader)