
import time

name = input("What is your name? ")

print("Hello, " + name, "time to play hangman!")

print(" ")

time.sleep(0.15)

print("Start guessing...")
time.sleep(0.15)

word = "extreme"

guesses = ''

turns = 5

while turns > 0:         
    failed = 0    

    for char in word:      
        if char in guesses:    
            print(char,)    
        else:
            print("_"),     
            failed += 1    
    if failed == 0:        
        print("You won... woohoo") 
        break              

    print()

    guess = input("guess a character:") 

    guesses += guess                    

    if guess not in word:  

        turns -= 1        

        print("you're completely wrong")

        print("You have", + turns, 'more guesses')

        if turns == 0:           
         print("You Lose!")
    