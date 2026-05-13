### Secret Agent Login
# Create a login process for a secret agent
print ('Hello Secret Agent')
# Ask for the user's name and save it in a variable
name = input ('What is your name?')
# Ask for the password and save it in a variable
password = input ('What is the secret password?\nHint: Falcon\n')

# Check if the password == 'Falcon'
if password == 'Falcon':
    # Ouput that access has been granted and welcome user using their name
    print ('Acess granted\nWelcome Agent' + name)
    # Ask for the user's age and save it in a variable
age = input ('What is your age?')
    # Change the age into an integer
age = int(age)
    # If the user's age is under 13, tell them they are a spy in training
if age < 13: 
    print (' You are a spy in training')
    # If their age is under 18, tell them they are a junior spy
if age < 18:
    print (' You are a junior spy')
    # If their age is 18 or over, tell them they are a Field Agent
if age >= 18:
    print ('You are a Field Agent')
# Output a goodbye
print ('You now know your role\nGoodbye')