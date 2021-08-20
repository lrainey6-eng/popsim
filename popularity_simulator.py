import time
import random

print ("""


Welcome to the Popularity Simulator, written by Levin Rainey. Go on, tell a joke!

(P.S. for help type 'help' and for copyright type 'cr' at any time)
(P.P.S type 'quit' to exit)


""")


time.sleep(0.5)

joke = input(">>> ").lower()

possRes = ['ha', 'ah', 'aa', 'hh']
playing = True


while playing == True:
	if joke != 'help' and joke != 'cr' and joke != 'quit' and joke != '' and joke != ' ':
		x = random.randint(1,5)
		rand1 = random.choice(possRes)
		rand2 = random.choice(possRes)
		rand3 = random.choice(possRes)
		rand4 = random.choice(possRes)
		rand5 = random.choice(possRes)
		rand6 = random.choice(possRes)
		response = rand1 + rand2 + rand3 + rand4 + rand5 + rand6
		time.sleep(0.5)
		print(response + '!'*x + ' That was so funny! Please tell another one!!!')
		joke = input(">>> ").lower()
	elif joke == 'help':
		print ("Jesus, it's not that complicated. Type in a joke, press enter, and I'll laugh at your (probably lame) joke. ")
		joke = input(">>> ").lower()
	elif joke == 'cr':
		print ("Copyright 2021 Levin Rainey")
		joke = input(">>> ").lower()
	elif joke == 'quit':
		print ("Finally, I'm done with your absolutely awful jokes. ")
		time.sleep(1)
		playing = False
	elif joke == '' or joke == ' ':
		print ("Are you going to tell a joke or just stare at me? ")
		joke = input(">>> ").lower()
	else:
		print ("what")
		joke = input(">>> ").lower()
	