
'''
Edward Abel-Guobadia
1-19-2023
'''

import pygame as pg
import constants
from random import uniform
from time import sleep


#   variables and things and stuff
circle_center = (250, 250)
circle_radius = 150.0
circle_width = 2
window_size = (500, 500)
dot_radius = 2.0

def draw_dots_cartesian(window):
    '''
        given the region of the window that is enclosed by the circle
        draw BLUE dots at random locations in the circle using cartesian coordinates
    '''
    x = uniform(circle_radius + circle_width * dot_radius, circle_center[1] + circle_radius - circle_width * dot_radius)
    y = uniform(circle_radius + circle_width * dot_radius, circle_center[1] + circle_radius - circle_width * dot_radius)
    
    pg.draw.circle(window, constants.BLUE, (x, y), dot_radius)

    #   to keep track of each dot
    return 1

def draw_dots_polar():
    '''
        given the region of the window that is enclosed by the circle
        draw RED dots at random locations in the circle using polar coordinates
    '''
    pass

def main():
    #   initialize pygame window
    pg.init()

    #   program window
    window = pg.display.set_mode(window_size)

    #   draw circle
    pg.draw.circle(window, constants.CIRCLE_COLOR, circle_center, circle_radius, circle_width)
    #   circle hitbox
    pg.Rect(circle_center[0], circle_center[1], circle_width, circle_radius)


    num_dots = 0
    #   main window loop
    while True:
        pg.display.update()

        #   draws the random points
        num_dots += draw_dots_cartesian(window)
        #   if there are 1000 dots stop making new dots then terminate program
        if num_dots == 1000:
            sleep(10.0)
            exit()

        #   window event handler
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()


if __name__ == "__main__":
    main()
