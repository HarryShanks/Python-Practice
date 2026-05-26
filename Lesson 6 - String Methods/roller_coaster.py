# Create a roller coaster access screener (determine if the user is allowed to ride)
# Rules:    They must be over 150cm and over 10 years old
#           They must not have a heart condition
#           OR they can ride if they have a VIP pass

# Get input
print("Welcome to the Roller Coaster Access Screener")
print("Just have to check a few rules to make sure you are elligible to ride")
Vip_Pass = input("Do you have a Vip Pass? ")
if Vip_Pass == ("Yes"):
    print ("You can ride the rollercoaster,your highness")
else:
    height = int(input ("What height are you? (cm) "))
    if height > 150:
        age = int(input ("How old are you? "))
        if age > 10:
            heart_condition = input("Do you have a heart condition? ")
            if heart_condition == ("No"):
                print ("You can ride the Rollercoaster")
            else:
                print ("Sorry, you can't ride. You are too weak")
        else:
            print("Sorry, you can't ride. You are too young")
    else: 
        print("Sorry, you can't ride. You are too short")







# Check conditions and output verdict