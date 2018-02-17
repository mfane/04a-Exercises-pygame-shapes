#!/usr/bin/env python
'''

For every line, please add a comment describing what it does. 

Try to describe each line within the context of the program as a whole, rather than just mechanically

Feel free to alter the parameters to see how things change. That can be a great way to be able to intuit what is supposed to be happening

I will do the first two lines for you as an example


'''

import sys, pygame	# imports the sys and pygame modules so they can be used in this program
assert sys.version_info >= (3,4), 'This script requires at least Python 3.4' # requires that the Python 3.4 (or higher version) interpreter is being used; i.e., not compatible with Python 2

screen_size = (800,600)  #creates a tuple called screen_size
FPS = 60  #creates a variable called fps

def main():  #defines a function called main that doesnt take any arguments
	pygame.init() #initializes pygame
	screen = pygame.display.set_mode(screen_size)  #makes a screen that is the size of the tuple screen_size
	clock = pygame.time.Clock() #creates a clock

	while True: #sets up an infinte loop
		clock.tick(FPS) #sets the cps to only go as fast as fps
		screen.fill((0,0,0))  #fills the screen with black

		for event in pygame.event.get(): #sets up a for loop to do something when an event happens
			if event.type == pygame.QUIT: #checks to see if the event is a quit event
				pygame.quit() #quits out of pygame
				sys.exit(0)  #exits out of the system

		pygame.display.flip()  #displays what we have created on the screen to the user all at once

if __name__ == '__main__': #checks to see if this is being run as the main program or is just being called by another .py file
	main() #runs the main function