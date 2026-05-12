#Information
STEPS_IN_KM = 1312
GOAL = 5.0
#User Facts
USER_NAME = input("Enter athlete name: ")  
steps = float(input("How many steps did you walk? "))  
#Math
km_walked = steps / STEPS_IN_KM
km_rounded = round(km_walked, 2) 
#Joining Together
print(USER_NAME + " walked " + str(km_rounded) + " km.")
goal_reached = km_rounded >= GOAL
#Final Facts
print("Daily 5km Goal Met:")
print(km_rounded)