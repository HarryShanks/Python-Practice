#Setting up While Loop
play = True
if 7>6:
    while play == True:
        #Intro 
        print("Quiz Bot: Hello and welcome to the Loser's Quiz")
        HOST_NAME = "Quiz Bot:" #Setting Host Name
        score = 0
        print(f"{HOST_NAME} You have been chosen by your peers to redeem your loserness and become an average person")
        PLAYER_NAME = input(f"{HOST_NAME} What is your name?").strip() #Setting Player Name
        print(PLAYER_NAME.strip()+":" +PLAYER_NAME) 
        print(f"{HOST_NAME} What an absolute loser name 'laughs'") 
        #Question 1
        print()
        print(f"{HOST_NAME} Question 1... What is 1 + 1")
        print(f"{HOST_NAME} Folks, I don't think they will get this one!")
        print(f"{HOST_NAME} Is it\nA.Macaroni\nB.Televison\nor\nC.2?") # The question
        answer1 = input(f"{PLAYER_NAME}: ").lower().strip()
        if answer1 in ["c", "2","c.2"]: # Right answers
            print(f"{HOST_NAME} Holy Smokes, You have a brain cell!") # If right answer
            score += 1
        else:
            print(f"{HOST_NAME} That went about as well as expected. The answer was 2") # If wrong answer
        #Question 2
        print()
        print(f"{HOST_NAME} Let's move straight on to the next question\nQuiz Bot:Let's amp it up a little")
        print(f"{HOST_NAME} Question 2: What's my favourite colour?")  # The Question
        print(f"{HOST_NAME} I really threw them a bone there")
        print(f"{HOST_NAME} No multiple choice here")
        answer2 = input(f"{PLAYER_NAME}:").upper().strip()
        if answer2 == "VERMILLION": #The Answer
            print(f"{HOST_NAME} Obviously you got that one,Whew") # If answer right
            score += 1
        else:
            print(f"{HOST_NAME} You really aren't doing well, are you? The answer was clearly Vermillion") #If answer wrong
        #Question 3
        print()
        print (f"{HOST_NAME}  2 questions down and lets go for a medium question")
        print (f"{HOST_NAME} Question 3: What is the captial of Mexico?")
        answer_3 = input(f"{PLAYER_NAME}:").upper().strip()
        if answer_3 == "MEXICO CITY":
            print (f"{HOST_NAME} At least you know your geography")
            score += 1
        else:
            print (f"{HOST_NAME} I hope I never go travelling with you. The answer was Mexico City")
        #Question 4 
        print()
        print (f"{HOST_NAME} Following up from Question 2, let's test you on some more colours")
        print (f"{HOST_NAME} Question 4: In the rainbow, what follows Red,Orange,Yellow,Green,Blue,? (if you have multiple answers just put a space between them)")
        answer4 = input(f'{PLAYER_NAME}:').upper().strip()
        if answer4 == "INDIGO":
            print (f"{HOST_NAME} It's not just Indigo that comes afterwards")
            score += 1
        elif answer4 == "VIOLET":
            print (f"{HOST_NAME} Nope,Loser, You forgot about Indigo")
        elif answer4 == "PURPLE":
            print (f"{HOST_NAME} Purple's not in the rainbow")
        elif answer4 == "INDIGO VIOLET":
            print (f"{HOST_NAME} WHAT! I didn't actually expect you to put two answers but you still got it right!")
            score += 1
        else: 
            print (f"{HOST_NAME}You probably shouldn't have come on this show, there is no hope for you")
        #Question 5
        print()
        print (f"{HOST_NAME} I think Qustion 1 was a fluke so let's test your math skills again")
        print (f"{HOST_NAME} Question 5:\n{HOST_NAME}What is 9999999991 + 1999999999 * 0 + 3455 + 2" )
        answer5 = input(f"{PLAYER_NAME}:").lower().strip()    
        if answer5 == "3457":
            print (f"{HOST_NAME} Math Genius over here! I mean yeah that's right")
            score += 1
        else:
            print (f"{HOST_NAME} Yup,It was a fluke alright")
        #Question 6
        print ()
        print (f"{HOST_NAME} No breaks,lets head on to Question 6")
        print (f"{HOST_NAME} Question 6:Is 6>7")
        answer6 = input(f"{PLAYER_NAME}:").upper().strip()
        if answer6 == ("NO"):
            print (f"{HOST_NAME} That is the correct answer")
            score += 1
        elif answer6 == ("YES"):
            print (f"{HOST_NAME} That is the wrong answer")
        else:
            print(f"{HOST_NAME} It was a yes or no question, Why didn't you put yes or no")
        #End of Quiz
        print()
        print (f"{HOST_NAME} Well you made it to the end of the quiz")
        print (f"{HOST_NAME} Your final score is, {score}/6")
        print (f"{HOST_NAME} Now, DON'T COME BACK!\nBye")
        print()
        #Asking if player wants to play again
        again = input("System: Do you want to play again?").lower().strip()
        if again == "yes":
            play = True
        else:
            play = False
