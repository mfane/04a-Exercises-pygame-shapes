#!/usr/bin/env python
'''

For this exercise, draw randomly-sized, randomly-colored, rectangles in random locations on the screen
It might be helpful to define a list of colors you want to use
hint: where you place the screen.fill(black) will affect whether or not the squares persist on the screen

'''
import sys, pygame, random

assert sys.version_info >= (3, 4), 'This script requires at least Python 3.4'

screen_size = (800, 600)
FPS = 60
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
dark_green = (0, 128, 0)
yellow = (255, 255, 0)


def main():
    pygame.init()
    screen = pygame.display.set_mode(screen_size)
    clock = pygame.time.Clock()
    screen.fill(black)
    while True:
        clock.tick(FPS)
        (x, y, width, height) = (
            random.randint(0, 800), random.randint(0, 600), random.randint(0, 400), random.randint(0, 300))
        c = random.randint(0, 4)
        if c == 0:
            color = red
        elif c == 1:
            color = green
        elif c == 2:
            color = white
        elif c == 3:
            color = dark_green
        else:
            color = yellow
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
        pygame.draw.rect(screen, color, (x, y, width, height))
        pygame.display.flip()


if __name__ == '__main__':
    main()
