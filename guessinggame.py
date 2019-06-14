import random

number = random.randint(1, 100)

guesses = 0

while guesses < 7:
    guess = int(input("Enter an integer from 1 to 100: "))
    guesses +=1
    print("You've guessed", guesses ,"times")


    if guess < number:
        print ("guess is low")
    elif guess > number:
        print("guess is high")
    elif guess == number:
        break

if guesses == 1 and guess == number:
    print("thass crazy")

if guesses == 7 and guess == number:
    print("Lucky guess")

if guess == number:
    guesses = str(guesses)
    print("You got it in : ", guesses + " attempts")

    
if guess != number:
    number = str(number)
    print("The secret number was", number)