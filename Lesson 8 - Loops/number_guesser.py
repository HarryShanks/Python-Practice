
# IMPORTS
import random
# VARIABLES
secret_number = random.randint (1, 100)
guesses = 0
current_guess = 0

print ("Welcome to the Higher or Lower Number Guessing Game")
# START THE GAME
current_guess = int(input("Guess a number from 1 to 100\n"))
print ("Checking guess...")
guesses +=1
while current_guess != (secret_number):
    if secret_number < current_guess:
        print ()
        print ("Not Correct\nToo High")
        guesses +=1
        current_guess = int(input("Guess a number from 1 to 100\n"))
        print("Checking guess...")
    elif secret_number > current_guess:
        print ()
        print ("Not Correct\nToo Low")
        guesses +=1
        current_guess = int(input("Guess a number from 1 to 100\n"))
        print("Checking guess")
    else: 
        input ("I said guess a number from 1 to 100\n") 
        print ("Checking Guess")
if  current_guess == (secret_number):
    print ()
    print ("You got it correct!\nGood Job")
    print (f"It took you {guesses} tries to get in")
