import twitter, datetime
import urllib2
import sqlite3
import time 


while True:

#Load in my keys and secrets from the credentials file into a list (array
	file = open("TwitterCredentials.txt")
	creds = file.read().split('\n')


# View history
	console = sqlite3.connect("/Users/JordanYapp12/Library/Application Support/Google/Chrome/Default/History")
	cursor = console.cursor()

	cursor.execute("SELECT urls.title FROM urls")
	rows = cursor.fetchall()

	history_list = []

	for row in rows:
		history_list.append(row) # Adds row into the recent list above

	lastSite = str(history_list[-1]) # Gets the last site on the list and stores it into lastSite
	site = lastSite[3:-3] #Trims it so prints out the parts we need, takes the title 
	print(site)
	console.close
# Create a new API wrapper, passing in my credentials one at a time
	api = twitter.Api(creds[0],creds[1],creds[2],creds[3])

# Find out what time it is now (in Coordinated Universal Time)
	timestamp = datetime.datetime.utcnow()

# Post status update and get the response from Twitter
	response = api.PostUpdate("The page i just viewed was: " + site)
#response = api.PostUpdate("Whaaazzzuupppp")

# Print out response text (should be the status update if everything worked)
	print("Status updated to: " + "The page i just viewed was: " + site)

	time.sleep(300)
