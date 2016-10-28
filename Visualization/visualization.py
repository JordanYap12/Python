from graphics import *
import random

txt_file = open('Data.txt', 'r+')
results = txt_file.read().split('\n')
txt_file.close()


for word in results: print("--- " + word ) # Prints out results in terminal 
window = GraphWin("Phonegap results", 600, 600)

for word in results:
    x = random.randrange(0,600)
    y = random.randrange(0,600) # circles positions 
    ball = Circle(Point(x,y), int(word)) # creates the circles 
    ball.setFill(color_rgb(148,0,211))
    ball.draw(window)
    
window.getMouse()