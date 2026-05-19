#Intro to Quiz
print ("Take this short test to find out what animal you are")
answer_1 = input("Do you prefer Land,Sea or Sky? (Case Sensitive)\n")
#Land Questions
if answer_1 == ("Land"):
    answer_2 = input("Do you like running? \n")
    if answer_2 == ("Yes"):
        print ("You are a Cheetah!")
    elif answer_2 == ("No"):
        print ("You are a sloth!")
    else:
        print ("Sorry,you didn't seem to put in an answer\n Do you like running? \n" )
#Sea Questions
elif answer_1 == ("Sea"):
    answer_3 = input("Do you want to harness the power of electricity?\n")
    if answer_3 == ("Yes"):
        print ("You are a jellyfish!")
    elif answer_3 == ("No"):
        answer_4 = input("Are you frail?\n")
        if answer_4 == "Yes":
            print ("You are a Crab!")
        elif answer_4 == ("No"):
            print ("You are a Seal!")
        else:
            print ("Sorry,you didn't seem to put in an answer\n Are you Frail?")    
    else:
        print ("Sorry,you didn't seem to put in an answer\n Do you want to harness the power of electricity?\n")  
#Sky Questions
elif answer_1 == ("Sky"):
    answer_5 = input ("Do you want to lay eggs (Are you female?)\n")
    if answer_5 == ("Yes"):
        print ("You are a Hen!")
    elif answer_5 == ("No"):
        print ("You are a Rooster!")
    else: 
        answer_5 = input("Sorry,you didn't seem to put in an answer\n Do you want to lay eggs (Are you female?)\n")
else:
    answer_1 == input ("Sorry,you didn't seem to put in an answer\n Do you prefer Land,Sea or Sky? \n")





   
