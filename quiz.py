#Intro
print ("Quiz Bot: Hello and welcome to the Loser's Quiz")
print ("Quiz Bot:You have been chosen by your peers to redeem your loserness and become an average person")
name = input ("Quiz Bot: What is your name?")
print(name + ":" +name) 
print ("Quiz Bot: What an absolute loser name 'laughs'") 
#Question 1
print ("Quiz Bot: Anyway, your first question is... What is 1 + 1")
print ("Quiz Bot: Folks, I don't think they will get this one!")
print ("Quiz Bot: Is it\nA.Macaroni\nB.Televison\nor\nC.2?")
answer1 = input(f"{name}: ")
if answer1 in ("C", "2"):
    print("Quiz Bot:Holy Smokes, You have a brain cell!")
else:
    print("Quiz Bot:That went about as well as expected. The answer was 2")
#Question 2
print ("Quiz Bot:Let's move straight on to the next question\n Let's amp it up a little")
print ("Quiz Bot:What's my favourite colour?")
print ("Quiz Bot:I really threw them a bone there")
print ("Quiz Bot:No multiple choice here")
answer2 = input(f"{name}: ")
if answer2 == ("Vermillion"):
    print ("Quiz Bot:Obviously you got that one,Whew")
else:
    print ("Quiz Bot:You really aren't doing well, are you? The answer is clearly vermillion")
