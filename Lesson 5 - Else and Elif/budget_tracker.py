### Budget Tracker ###
# Create a budget tracker that gives financial recommendation around an item

# Create a constant to hold your budget
BUDGET = int (1000)
# Create a constant to hold your savings (percentage) goal
SAVING_GOAL = int (300)
# Ask user for item name and save in variable
print ("Welcome to the Budget Tracker")
print ("You have a budget of 1000 and a savings goal of 30% (300)")
item = input("What item would you like to buy?\n")
# Ask user for cost and save in variable
cost = input ("How much does that cost?\n")
# Change the cost into an integer
cost = int(cost)
# Calculate the percentage of budget (cost / budget) * 100
# Tell your user the percentage of your budget
print (cost/BUDGET *100)
# Check if percentage is 0 and say it's free if it is
if cost == 0:
    print ("It's free")
# Check if the percentage is less then 10 and say it's a small treat so enjoy
elif cost >= 10:
    print ("It's a small treat, enjoy")
# Check if it is less than 50 percent and if it is tell them it's a major spend and should sleep on it
elif cost <10 & cost >50:
    print ("You should probobly sleep on it")
# Check if it's over 100 and if it is tell them they don't have enough money
elif cost >100:
    print ("You don't have enough money")
# Otherwise, tell them it costs way too much and isn't worth it
else:
    print ("It costs way too much money") 