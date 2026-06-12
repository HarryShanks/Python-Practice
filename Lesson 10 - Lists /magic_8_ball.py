# =====================================================================
# PROJECT: The Magic 8-Ball Fortune Teller
# Create a program that gives random responses to yes/no questions
# =====================================================================

# TOOLS
import random


# RESPONSES
# TODO: Create a list called 'responses' that contains at least 8 different 
#       8-ball answers (strings). There should be positive answers, negative answers and neutral answers.
#       Examples: "Yes, definitely!", "Ask again later.", "Outlook not so good."
responses = ['Yes','No','Try again later','Not Now', "I'm sleeping", 'You know the answer to that', 'How dare you ask me that', 'Maybe', 'Ask the gruffalo if you really want to know', "I'm not doing this today I QUIT"]
# MAIN LOOP
# TODO Create an infinite loop
while True:
    print ()
    eight_ball_answer = input("Ask a yes or no question about your future (or press quit to leave)\n")
    
    # TODO: Ask the user to type in a Yes/No question about their future and save it in a variable.
    #       (Or tell them to type 'quit' to leave).
    if eight_ball_answer == quit:
        break
    else:
        random_index = responses[random.randint(0,9)]
        chosen_fortune = print(random_index)
    print("Goodbye")
    break
    # Check if the user wants to exit and break from the loop if they do.
        
    # RANDOM REPSONSE
    # TODO: Step A: Calculate the last valid index of your list.
    #       (Remember: If a list has 5 items, the indexes are 0, 1, 2, 3, 4).
    #       Use random.randint() to get a number between 0 and that last index.
    #       Save it in a variable called 'random_index'.
    
    
    # TODO: Step B: Use your 'random_index' to grab the matching answer 
    #       out of your 'responses' list.
    #       Save it in a variable called 'chosen_fortune'.

    # TODO Print the result

# TODO Say goodbye to let them know the program has ended.