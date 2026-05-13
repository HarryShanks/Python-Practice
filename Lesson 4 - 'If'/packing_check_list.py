### Create a packing checklist based on input

# Tell the user what this program is about
print ("Hello, today we will be packing for an adventure")
# Ask the user for the current temperature and save it
tempreture = input ("What degrees celceius is it?\n")
# Change the temperature input into an integer
tempreture = int(tempreture)
# If the temperature is below 15, tell them to pack a jacket
if tempreture <= 15:
    print ("Bring a jacket, it might be chilly")
# If the temperature is above 15, tell them to pack sunscreen
if tempreture > 15: 
    print ("Get out the sunscreen, it will be scorchin outside")
# Ask the user their destination (beach or mountains)
place = input ("Where are you going? Beach or Mountains?\n")
# If beach, tell them to pack a towel
if place == "Beach":
    print("Pack a towel then")
# If mountains, tell them to pack hiking boots
if place == "Mountains":
    print ("Pack some hiking boots")
print ("Now go out and enjoy the day")