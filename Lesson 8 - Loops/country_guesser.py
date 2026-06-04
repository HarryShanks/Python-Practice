
# VALUES
correct_country = "SCOTLAND"
current_guess = ""
guesses = 0

# LOOP
current_guess = input("Guess the secret country\n").upper().strip()
print ("Checking guess...")
while current_guess != (correct_country).upper():
    print()
    print("Not Correct")
    guesses +=1
    if guesses == 1:
      print ("Feeling magical?(Hint 1)")
    elif guesses == 2: 
        print ("My ancestors are from this place(Hint 2)")
    elif guesses == 3:   
        print ("One of the many lands of the world (Ends with land) (Hint 3)")
    else:
        print ("Too many incorrect guesses!\nSystem Overheating\nSystem Shutdown")
        break
    current_guess = input("Guess the secret country\n").upper().strip()
    print ("Checking Guess...")
if current_guess == (correct_country).upper():
    guesses +=1
    print ("Welcome to the country of Haggis")
    print (f"It took you {guesses} guesses to get in")
