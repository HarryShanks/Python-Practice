# =====================================================================
# PROJECT: Wordle
# Create a program where the user must guess the 5 letter word.
# =====================================================================

# TOOLS
# TODO Import random so you can randomise the word
import random
# VALUES
words = ["Apple", "Beard", "Crust", "Dingo", "Eagle", "Fluke", "Green", "Hairy", "Igloo", "Joker", "Koala", "Laser", "Macho"]
# TODO Create a variable called play and set it to True
play = True
# INTRODUCTION
# TODO Tell your user how to play wordle (make sure they know they must input 5 letter words)
print()
print("Welcome to Wordle")
print ("Guess a five letter word and wordle will decide whether the letter is in the word, in the wrong spot or not in the word at all")
# MAIN
# TODO Create a while loop that runs if play is true
while play == True:

    # TODO Create word variable and store a random word from your list (using random.choice)
    secret_word = random.choice
    # USER INPUT
    
    guess = input("What is your first guess?").lower().strip()
    # TODO Get user's first guess and save it into a variable
    while guess != len(5):
        print()
        print("The guess needs to be 5 letters")
        print ("Try again")
        print ("What is your first guess?")
    # TODO Create a while loop if the guess is not 5 characters long
        # TODO Tell them it's not 5 letters and to try again
    while guess == len(5):
    # TODO Check if they got it correct and if they did, tell them so and then break the loop
        if guess == secret_word:
            print("You got it correct!")
            break
    # TODO Create a for loop that loops 5 times
    for i in range(5):
        input("What is your next guess?").lower().strip()
        while guess != len(5):
            print()
            print("The guess needs to be 5 letters")
            print ("Try again")
            print ("What is your next guess?")
        while guess == len(5):
             if guess == secret_word:
                print()
                print("You got it correct!")
                break

        # TODO Check if the current letter of user_input (user_input[i]) is the same as the i letter of the word and if it is tell them they got that letter correct
        for j in range(5):
            if guess[j] == secret_word[j]:
                print()
                print(f"{guess[j]} is in the right spot")
        # TODO Otherwise check if the current letter of user_input is in the word and if it is, tell them that letter is in the wrong position
            elif guess[j] in secret_word:
                print()
                print(f"{guess[j]} is in the word but is in the wrong spot")
        # TODO Else tell them that letter is wrong
            else:
                print()
                print (f"{guess[j]} is not in the word ")
# TODO Ask if they want to play again. If they don't, set play to false.
again = input("Do you want to play again?").lower().strip()
if again in "yes":
    play = True
else:
    play = False