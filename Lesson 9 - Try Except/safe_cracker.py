# =====================================================================
# PROGRAM: Safe Cracker (The Digital Vault)
# =====================================================================
import sys
# SETUP YOUR VARIABLES
# TODO: Create a variable for the correct vault combination (e.g., "742").
# TODO: Create a variable to keep track of how many attempts the player has used (start at 0).
correct_combination = ("666")
attempts = 0

# INTRODUCE THE GAME
# TODO: Print a cool message explaining they are trying to hack a safe.
# TODO: Let them know that typing 'exit' will quit the game entirely.
print()
print("Welcome Agent Hacker")
print("We are hoping you crack the safe")

print("You will be rewarded handsomly for completing this task")
print()
print("(Side Note, typing exit will have you fail your mission)")



# LOOP
# TODO: Create an infinite while loop
# Note: By using 'True', this loop will run forever unless we use 'break'!
while True:
    user_input = input ("Guess the safe number (All we know is that it's a three digit number)").strip()
    print()
    # TODO: Ask the user to enter the 3-digit combination (or type 'exit').
    #       Save their input into a variable called 'user_input'.
    


    # -----------------------------------------------------------------
    # SCENARIO A: The user wants to quit
    # -----------------------------------------------------------------
    # TODO: Check if 'user_input' is equal to the word 'exit'.
    #       If it is, print "Aborting mission..." and use 'break' to stop the loop!
    if user_input == ('exit'):
        print ("Aborting mission")
        attempts +=1
        print ("I knew you weren't cut out for this job, Agent Hacker")
        print ("Time for the death penalty")
        print(f"You took {attempts} attempts to crack the code")
        print("\n--- Game Over ---")
        print('(BAD ENDING)')
        break
    # -----------------------------------------------------------------
    # SCENARIO B: Invalid Input
    # -----------------------------------------------------------------
    # TODO: Check if their input is a valid number
    #       (Hint: use try except)
    #       If it's not, print "Error: Safe only accepts digits. Try again."
    #       Then, use 'continue' to skip the rest of the code and restart the loop.
    try:
        converted = int(user_input)
        if len(str(converted)) != 3:
            raise ValueError
    except: 
            print ("Safe only accepts three digit numbers,try again ")
            continue
    # -----------------------------------------------------------------
    # SCENARIO C: Processing a valid attempt
    # -----------------------------------------------------------------
    # If the code gets past Scenario B, it means they entered a valid 3-digit attempt!
    
    # TODO: Increase your attempts tracker variable by 1.
    attempts +=1



    # TODO: Check if 'user_input' matches the correct vault combination.
 
    #       If it does: Print "Vault unlocked! You found the treasure!" and 'break' out of the loop.
    #       If it doesn't: Print a message telling them the combination failed.
    if attempts == 3:
        print("Don't forget you can type exit to fail your mission")
    elif attempts == 10:
        print("COME ON AGENT HACKER YOU SAID YOU WERE GOOD AT THIS")
        print ("Never mind your job, you have bigger matters on your hand")
        print ("We have leaked information to the police about you trying to crack a safe so have fun in prison")
        print("\n--- Game Over ---")
        print ("(Alright ENDING)")
        sys.exit(0)
    
    if user_input == correct_combination:
        print("Wait... HOLEY MOLEY, YOU CRACKED THE CODE")
        print ("Ahem, Thank you for unlocking the vault. Now for your reward. Ah yes, you're fired")
        print(f"You took {attempts} attempts to crack the code")
        print("\n--- Game Over ---")
        print ("(GOOD ENDING)")
        break
    else:
        print ("Sorry,Not the correct number. Try again Agent Hacker.")


# GAME OVER
# ---------------------------------------------------------------------
