#Vatsal Savani
#Creating Sierpinski Triangle from Chaos

import time, math, pygame, sys, random
from pygame.locals import *

# Set constants
SIZE = 500
COLOUR = (255,255,255)
START = (0, SIZE)

# Set up pygame
pygame.init()
# 	Set up window	
screen = pygame.display.set_mode((SIZE, SIZE), 0, 32)
pygame.display.set_caption('Fractal_Sierpinski Triangle')

# Set vertexes
lv = (0, SIZE) # Left Vertex
rv = (SIZE, SIZE) # Right Vertex
tv = (SIZE/2, SIZE - (3**0.5) * (rv[1] - lv[1] / 2 )) # Top Vertex

# Plot point
def plotPixel (pos) :
	screen.fill(COLOUR, (pos, (1, 1)))
	pygame.display.update()

def drawLine (pos1, pos2) :
	pygame.draw.line(screen, COLOUR, pos1, pos2)
	pygame.display.update()

running = True 

# Draw Triangle
drawLine (lv, rv)
drawLine (lv, tv)
drawLine (tv, rv)

# Set start point
point = START
plotPixel (point)

#Number of points to be plotted (change 30000 to number of points to be plotted)
for i in range(0, 30000) :

	if (i % 100) == 0 :
		print(i) 

	#Randomly choose vertex
	pick = random.randint(1,3)

	if pick == 1 :
		#Midpoint between lv and Point
		point = ((point[0] + lv[0])/2, (point[1] + lv[1])/2)

	elif pick == 2 :
		#Midpoint between tv and Point
		point = ((point[0] + tv[0])/2, (point[1] + tv[1])/2)

	else :
		#Midpoint between rv and Point
		point = ((point[0] + rv[0])/2, (point[1] + rv[1])/2)

	#Plot point
	plotPixel(point)

print(i)


while running :
	for event in pygame.event.get ():
		if event.type == 12 :
			running = False

pygame.QUIT()










