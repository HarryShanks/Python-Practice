# For Time

#import time
#print ("1")
#time.sleep (1)
#print ("2")

while True:
	guess = input('Guess a country: ')
	if guess.lower().strip() == 'malawi':
		break
	print('Try again.')
print('Well done!')



