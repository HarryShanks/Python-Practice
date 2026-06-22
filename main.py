# For Time

#import time
#print ("1")
#time.sleep (1)
#print ("2")
def check_play():
    play = input("Do you want to play again")
    if play.lower() in ["y", "yes"]:
        return True
    else:
        return False

print(check_play())














