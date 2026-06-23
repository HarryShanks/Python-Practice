#Intro
if 7>6:
    print("Quiz Bot: Hello and welcome to the Loser's Quiz")
HOST_NAME = "Quiz Bot:"
score = 0
print("Quiz Bot:You have been chosen by your peers to redeem your loserness and become an average person")
PLAYER_NAME = input("Quiz Bot: What is your name?").strip()
print(PLAYER_NAME.strip()+":" +PLAYER_NAME) 
print("Quiz Bot: What an absolute loser name 'laughs'") 
#Question 1
print()
print("Quiz Bot: Question 1... What is 1 + 1")
print("Quiz Bot: Folks, I don't think they will get this one!")
print("Quiz Bot: Is it\nA.Macaroni\nB.Televison\nor\nC.2?")
answer1 = input(f"{PLAYER_NAME}: ").lower().strip()
if answer1 == "c" or answer1 == "2" or answer1 == "c.2":
    print("Quiz Bot:Holy Smokes, You have a brain cell!")
    score += 1
else:
    print("Quiz Bot:That went about as well as expected. The answer was 2")
#Question 2
print()
print("Quiz Bot:Let's move straight on to the next question\n Quiz Bot:Let's amp it up a little")
print("Quiz Bot: Question 2: What's my favourite colour?")
print("Quiz Bot:I really threw them a bone there")
print("Quiz Bot:No multiple choice here")
answer2 = input(f"{PLAYER_NAME}:").upper().strip()
if answer2 == "VERMILLION":
    print("Quiz Bot:Obviously you got that one,Whew")
    score += 1
else:
    print("Quiz Bot:You really aren't doing well, are you? The answer was clearly Vermillion")
#Question 3
print()
print ("Quiz Bot:2 questions down and lets go for a medium question")
print ("Quiz Bot: Question 3: What is the captial of Mexico?")
answer_3 = input(f"{PLAYER_NAME}:").upper().strip()
if answer_3 == "MEXICO CITY":
    print ("Quiz Bot:At least you know your geography")
    score += 1
else:
    print ("Quiz Bot:I hope I never go travelling with you. The answer was Mexico City")
#Question 4 
print()
print (HOST_NAME "Following up from Question 2, let's test you on some more colours")
print ("Quiz Bot:Question 4: In the rainbow, what follows Red,Orange,Yellow,Green,Blue,? (if you have multiple answers just put a space between them)")
answer4 = input(f'{PLAYER_NAME}:').upper().strip()
if answer4 == "INDIGO":
    print ("Quiz Bot: It's not just Indigo that comes afterwards")
    score += 1
elif answer4 == "VIOLET":
    print ("Quiz Bot:Nope,Loser, You forgot about Indigo")
elif answer4 == "PURPLE":
    print ("Quiz Bot:Purple's not in the rainbow")
elif answer4 in ("INDIGO", "VIOLET"):
    print ("Quiz Bot:WHAT! I didn't actually expect you to put two answers but you still got it right!")
    score += 1
else: 
    print ("Quiz Bot:You probably shouldn't have come on this show, there is no hope for you")
#Question 5
print()
print ("Quiz Bot:I think Qustion 1 was a fluke so let's test your math skills again")
print ("Quiz Bot: Question 5:\nWhat is 9999999991 + 1999999999 * 0 + 3455 + 2" )
answer5 = input(f"{PLAYER_NAME}:").lower().strip()    
if answer5 == "3457":
    print ("Quiz Bot:Math Genius over here! I mean yeah that's right")
    score += 1
else:
    print ("Quiz Bot:Yup,It was a fluke alright")
#Question 6
print ()
print ("Quiz Bot:No breaks,lets head on to Question 6")
print ("Quiz bot:Question 6:Is 6>7")
answer6 = input(f"{PLAYER_NAME}:").upper().strip()
if answer6 == ("NO"):
    print ("Quiz Bot: That is the correct answer")
    score += 1
elif answer6 == ("YES"):
    print ("Quiz Bot: That is the wrong answer")
else:
    print("It was a yes or no question, Why didn't you put yes or no")
#Outro
print()
print ("Quiz Bot: Well you made it to the end of the quiz")
print ("Quiz Bot:Your final score is", score/6)
print ("Quiz Bot: Now, DON'T COME BACK!\n Bye")
