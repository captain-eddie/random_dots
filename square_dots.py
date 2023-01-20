
'''
Edward Abel Guobadia
1-20-2023
'''

import pygame as pg
import constants
from random import uniform
from time import sleep


#   variables and stuff
window_size = (500, 500)
side_length = 300.0
square_pos = (100, 100)
square_width = 2
dot_radius = 2.0


def draw_dots(window):
    '''
        given the region of the window that is enclosed by the square
        draw BLUE dots at random locations in the square using cartesian coordinates
    '''
    x = uniform(square_pos[1] + square_width * dot_radius, window_size[1] - square_pos[1] - square_width * dot_radius)
    y = uniform(square_pos[1] + square_width * dot_radius, window_size[1] - square_pos[1] - square_width * dot_radius)
    pg.draw.circle(window, constants.BLUE, (x, y), dot_radius)

    #   to keep track of each dot
    return 1

def main():
    #   initialize pygame window
    pg.init()

    #   program window
    window = pg.display.set_mode(window_size)

    #   draw square
    square = pg.Rect(square_pos, (side_length, side_length))
    pg.draw.rect(window, constants.SQUARE_COLOR, square, square_width)

    num_dots = 0
    #   main window loop
    while True:
        pg.display.update()

        #   draws the random points
        num_dots += draw_dots(window)
        #   if there are 1000 dots stop making new dots then terminate program
        if num_dots == 1000:
            sleep(30.0)
            exit()

        #   window event handler
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()



if __name__ == "__main__":
    main()
