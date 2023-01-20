
'''
Edward Abel-Guobadia
1-19-2023
'''

import pygame as pg
import constants
from sys import exit

def draw_dots_cartesian():
    '''
        given the region of the window that is enclosed by the circle
        draw BLUE dots at random locations in the circle using cartesian coordinates
    '''
    pass

def draw_dots_polar():
    '''
        given the region of the window that is enclosed by the circle
        draw RED dots at random locations in the circle using polar coordinates
    '''
    pass

def main():
    #   variables and things and stuff
    circle_pos = (250, 250)
    circle_radius = 150.0
    circle_width = 2
    window_size = (500, 500)

    #   initialize pygame window
    pg.init()

    #   program window
    window = pg.display.set_mode(window_size)

    #   draw circle
    pg.draw.circle(window, constants.CIRCLE_COLOR, circle_pos, circle_radius, circle_width)
    #   circle hitbox
    pg.Rect(circle_pos[0], circle_pos[1], circle_width, circle_radius)


    #   main window loop
    while True:
        pg.display.update()

        #   window event handler
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()


if __name__ == "__main__":
    main()
