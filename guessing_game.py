print("Guess the number between 1 and 10, you only have 3 opportunities!")
se_number = 5
i = 1
while i <= 3:
    guess = int(input("Guess "))
    if guess == se_number:
        print("You got the number, you win!")
        break
    elif i >= 3:
        print("Game over!")
    i+=1
