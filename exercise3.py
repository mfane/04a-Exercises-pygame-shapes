#!/usr/bin/env python
'''

For this exercise, create a digital clock display on the screen

'''
import sys, pygame
from datetime import datetime

assert sys.version_info >= (3, 4), 'This script requires at least Python 3.4'

screen_size = (800, 600)
FPS = 60
black = (0, 0, 0)
white = (255, 255, 255)


def main():
    pygame.init()
    screen = pygame.display.set_mode(screen_size)
    font = pygame.font.SysFont("arial", 64)
    clock = pygame.time.Clock()
    (x, y) = (100, 100)
    while True:
        clock.tick(FPS)
        screen.fill(black)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
        text = str(datetime.now().time())
        f = font.render(text, True, white)
        (fwidth, fheight) = font.size(text)
        screen.blit(f, (x, y))
        pygame.display.flip()


if __name__ == '__main__':
    main()
