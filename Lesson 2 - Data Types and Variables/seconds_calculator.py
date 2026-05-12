# Create a calculator that asks the user for a number (of days)
# and outputs how many seconds in that number of days

# Values - start by writing constants to hold:
# The number of seconds in a minute
NUMBER_OF_SECONDS_IN_A_MINUTE = 60
# The number of minutes in an hour
NUMBER_OF_MINUTES_IN_A_HOUR = 60
# The number of hours in a day
NUMBER_OF_HOURS_IN_A_DAY = 24

# Get input from the user and save it in a variable
print("Give me a number of days and I will tell you how many seconds are in that day")
days = input("Give me a number of days.")
print (days)

# Change the value into an integer and resave in the variable
days = int (days)

# Calculate the number of seconds using * with the input and your constants. 
# Save it in a new variable.
total = days * NUMBER_OF_HOURS_IN_A_DAY * NUMBER_OF_MINUTES_IN_A_HOUR * NUMBER_OF_SECONDS_IN_A_MINUTE
# Output the answer
print ("Here is that number of days in seconds")
print(total)
# ---------------------------------

# EXTENSION 1
# Also output how many total hours and how many total minutes in the days

# ---------------------------------
# EXTENSION 2
# Create another calculator that does the opposite (input is seconds, output is days)

# ---------------------------------

# EXPERT (for those who already know some Python)
# Create the calculator above, but...
#   allow your user to choose the input and output type (seconds, minutes, hours, days)
#   Loop the calculator so they can do it again with having to reopen the program.
