#Intro
if 7>6:
    print("Quiz Bot: Hello and welcome to the Loser's Quiz")
print("Quiz Bot:You have been chosen by your peers to redeem your loserness and become an average person")
PLAYER_NAME = input("Quiz Bot: What is your name?").strip()
print(PLAYER_NAME.strip()+":" +PLAYER_NAME) 
print("Quiz Bot: What an absolute loser name 'laughs'") 
#Question 1
print("Quiz Bot: Anyway, your first question is... What is 1 + 1")
print("Quiz Bot: Folks, I don't think they will get this one!")
print("Quiz Bot: Is it\nA.Macaroni\nB.Televison\nor\nC.2?")
answer1 = input(f"{PLAYER_NAME}: ").lower().strip()
if answer1 == "c" or answer1 == "2" or answer1 == "c.2":
    print("Quiz Bot:Holy Smokes, You have a brain cell!")
else:
    print("Quiz Bot:That went about as well as expected. The answer was 2")
#Question 2
print("Quiz Bot:Let's move straight on to the next question\n Quiz Bot:Let's amp it up a little")
print("Quiz Bot:What's my favourite colour?")
print("Quiz Bot:I really threw them a bone there")
print("Quiz Bot:No multiple choice here")
answer2 = input(f"{PLAYER_NAME}:").upper().strip()
if answer2 == "VERMILLION":
    print("Quiz Bot:Obviously you got that one,Whew")
else:
    print("Quiz Bot:You really aren't doing well, are you? The answer was clearly Vermillion")
#Question 3
print ("Quiz Bot:2 questions down and lets go for a medium question")
print ("Quiz Bot:What is the captial of Mexico?")
answer_3 = input(f"{PLAYER_NAME}:").upper().strip()
if answer_3 == "MEXICO CITY":
    print ("Quiz Bot:At least you know your geography")
else:
    print ("Quiz Bot:I hope I never go travelling with you")
#Question 4 
print ("Quiz Bot: Following up from Question 2, let's test you on some more colours")
print ("Quiz Bot:In the rainbow, what follows Red,Orange,Yellow,Green,Blue,? (if you have multiple answers just put a space between them)")
answer4 = input(f'{PLAYER_NAME}:').upper().strip()
if answer4 == ("INDIGO"):
    print ("Quiz Bot:Fine,you got it right 'hmph'")
elif answer4 == ("VIOLET"):
    print ("Quiz Bot:Nope,Loser, You forgot about Indigo")
elif answer4 == ("PURPLE"):
    print ("Quiz Bot:Purple's not in the rainbow")
elif answer4 == ("INDIGO" and "VIOLET"):
    print ("Quiz Bot:WHAT! I didn't actually expect you to put two answers but you still got it right!")
else: 
    print ("Quiz Bot:You probably shouldn't have come on this show, there is no hope for you")
#Question 5
print ("Quiz Bot:I think Qustion 1 was a fluke")
print ("Quiz Bot:What is 9999999991 + 1999999999 * 0 + 3455 + 2" )
answer5 = input(f"{PLAYER_NAME}:").lower().strip()    
if answer5 != 9999999991 + 1999999999 * 0 + 3455 + 2:
    print ("Quiz Bot:Yup, It was a fluke alright")
elif answer5 == 9999999991 + 1999999999 * 0 + 3455 + 2:
    print ("Quiz Bot:Math Genius over here! I mean yeah that's right")
#Question 6
print ("Quiz Bot:No breaks,lets head on to Question 6")
print ("Quiz bot:Is 6>7")
answer6 = input(f"{PLAYER_NAME}:").upper().strip()
if answer6 == ("NO"):
    print ("Quiz Bot: Don't you mean yes because that's the correct answer")
elif answer6 == ("YES"):
    print ("Quiz Bot: Don't you mean no because that's the wrong answer")
else:
    print("It was a yes or no question, Why didn't you put yes or no")
#Outro

