print("Guess the number between 1 and 10, you only have 3 opportunities!")
se_number = 5
guess_count = 1
while guess_count <= 3:
    guess = int(input("Guess "))
    if guess == se_number:
        print("You got the number, you win!")
        break
    elif guess_count >= 3:
        print("Game over!")
    guess_count+=1
