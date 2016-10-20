import random
import time
"""link = open("stopwords.txt")
lines = link.readlines()"""

txt_file = open('stopwords.txt','r')
stopwords = txt_file.read()
txt_file.close()

happy_file = open('PositiveWords.txt', 'r')
happyWords = happy_file.read()
happy_file.close()

sad_file = open('NegativeWords.txt', 'r')
sadWords = sad_file.read()
sad_file.close()



# The user starts convo with a greetings
greetings = ['hola', 'hello', 'hi', 'Hi', 'hey!','hey', 'Sup', 'sup']

# The bot will reply with a greeting and instantly ask a question
random_greeting = random.choice(greetings)
question = ['You okay?', 'How are you?', 'You alright?', 'You good?', 'hows it going']
random_question = random.choice(question)

# The user with reply with either happy or sad response
firstHappyResponse = ['I\'m good', 'Not to bad', 'Yeah I\'m good', 'Good', 'I\'m feeling awesome']
firstSadResponse = ['Not good', 'Not feeling to good today', 'I\'m sad today']

# The bot with reply depending on the users response 
chatHappyResponse = ['Thats good', 'Good I\'m glad', 'That is wonderful']
random_happyResponse = random.choice(chatHappyResponse)
chatSadResponse = ['Oh no that\'s not good', 'Oh that sucks', 'Thats a bummer']
random_SadResponse = random.choice(chatSadResponse)

# User response to bots question - is it okay to ask you some questions?
secondUserResponse = ['Yeah sure', 'Sure', 'Okay', 'Yeah', 'Sure why not']
awksUserResponse = ['Nah', 'Nope', ' Rather not', 'no']

# The bots response to the question before 
continueResponse = ['Awesome, so...', 'Sweet, so...', 'good I\'m glad, so...', 'Thats cool, so...']
random_continueResponse = random.choice(continueResponse)
awksBotResponse = 'Oh this is awks...... I\'ll just leave'

# Bots colour question response
colourResponse = [' nice choice', ' awesome choice', ' sorry not a fan of that one', 'sweeeeet']
random_colorResponse = random.choice(colourResponse)

def getInterestingWord(words):
	for word in words:
		if word.lower() not in stopwords:return word

def getHappyWord(happy):
	for word in happy:
		if word.lower() in happyWords:
			print(random_happyResponse)

def getSadWord(sad):
	for word in sad:
		if word.lower() in sadWords:
			print(random_SadResponse)



bot_greeting = raw_input("Hello whats is your name?")

# Using the getInterestingWord function to get the stopwords to work 
indivdual_word = bot_greeting.split(" ")
interesting_word = getInterestingWord(indivdual_word)
print (random_greeting + " " + interesting_word)
time.sleep(1)
print "I\'m the awesome chat bot called Javascript"
time.sleep(1)
#print(random_question)

bot_feelingQuestion = raw_input("How are you?")
indivdual_word = bot_feelingQuestion.split(" ")

feeling_word = [getHappyWord(indivdual_word), getSadWord(indivdual_word)]


while True:
	if getHappyWord in feeling_word:
		print(random_happyResponse)

	elif getSadWord in feeling_word:
		print(random_SadResponse)





"""
while True:
	userInput = raw_input(">>> ")
	if userInput in greetings:
		print(random_greeting)
		time.sleep(1)
		name = raw_input("What is your name?")
		print "Ahhhh, Hello %s, I\'m the awesome chat bot called Javascript" % (name)
		time.sleep(2)
		print(random_question)

	elif userInput in firstHappyResponse:
		print(random_happyResponse)
		time.sleep(1)
		print "Soooooooo %s, is it okay to ask you some questions?" % (name)
	elif userInput in firstSadResponse:
		print(random_SadResponse)
		time.sleep(1)
		print "Soooooooo %s, is it okay to ask you some questions?" % (name)

	elif userInput in awksUserResponse:
		print(awksBotResponse)


	elif userInput in secondUserResponse:
		print(random_continueResponse)
		time.sleep(2)
		colour = raw_input('What is your favourite colour?')
		print "Oh so it\'s %s?" % (colour)
		time.sleep(1)
		print(random_colorResponse)  




	
	else:
		print("I did not understand what you said") 
		"""

