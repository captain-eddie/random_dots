
'''
Edward Abel-Guobadia
1-19-2023
'''

import pygame as pg
import constants
from random import uniform
from time import sleep
from math import sqrt, pow, acos as arccos, pi, cos, sin


#   variables and things and stuff
circle_center = (250, 250)
circle_radius = 150.0
circle_width = 2
window_size = (500, 500)
dot_radius = 2.0
square_left_top = (circle_center[1] - circle_radius, circle_center[1] - circle_radius)
square_width_height = (2 * circle_radius, 2 * circle_radius)

def draw_dots_cartesian(window):
    '''
        given the region of the window that is enclosed by the circle
        draw BLUE dots at random locations in the circle using cartesian coordinates
    '''
    #   inscribe circle in square
    #   sqaure = pg.Rect(square_left_top, square_width_height)
    #   pg.draw.rect(window, constants.WHITE, sqaure, circle_width)

    #   random variables
    x = uniform(square_left_top[0], square_left_top[0] + square_width_height[0])
    y = uniform(square_left_top[1], square_left_top[1] + square_width_height[1])
    dot_center = (x, y)


    #   dot = pg.draw.circle(window, constants.BLUE, (x, y), dot_radius)
    #   collide = region.collidepoint(dot.center)
    #   if not collide:
    #       #   need to find a better way to undo circle draw
    #       #   this just changes the radius of the dot to 0
    #       dot = pg.draw.circle(window, constants.BLACK, (x, y), 0.0)

    distance_vector = (x - circle_center[0], y - circle_center[1])
    distance = sqrt(pow(distance_vector[0], 2) + pow(distance_vector[1], 2))
    if distance > circle_radius - dot_radius - circle_width:
        dot = pg.draw.circle(window, constants.BLACK, (x, y), 0.0)
    else:
        dot = pg.draw.circle(window, constants.BLUE, (x, y), dot_radius)

    #   to keep track of each dot
    return 1

def draw_dots_polar(window):
    '''
        given the region of the window that is enclosed by the circle
        draw RED dots at random locations in the circle using polar coordinates
    '''
    r = uniform(0, circle_radius - (circle_width * dot_radius))
    theta = uniform(0, 360)

    dot_pos = polar_to_rect((r, theta))
    dot = pg.draw.circle(window, constants.RED, dot_pos, dot_radius)

    #   to keep track of each dot
    return 1

def polar_to_rect(polar_coordinate):
    '''
        given polar convert coordinate convert to polar coordinate
    '''
    x = polar_coordinate[0] * cos(polar_coordinate[1])
    y = polar_coordinate[0] * sin(polar_coordinate[1])

    rect_coordinate = (x, y)

    return rect_coordinate

def rect_to_polar(rect_coordinate):
    '''
        given cartestian coordinate convert to polar coordinate
    '''
    x = rect_coordinate[0]
    y = rect_coordinate[1]

    r = sqrt(pow(x, 2) + pow(y, 2))
    theta = radians_to_deg(arccos(x / r))

    polar_coordinate = (r, theta)

    return polar_coordinate

def radians_to_deg(angle):
    deg_angle = angle * (180 / pi)

    return deg_angle

def main():
    #   initialize pygame window
    pg.init()

    #   program window
    window = pg.display.set_mode(window_size)

    #   draw circle
    region = pg.draw.circle(window, constants.CIRCLE_COLOR, circle_center, circle_radius, circle_width)
    #   circle hitbox
    pg.Rect(circle_center[0], circle_center[1], circle_width, circle_radius)


    num_dots = 0
    #   main window loop
    print(rect_to_polar((10, 3)))
    while True:
        pg.display.update()

        #   draws the random points
        num_dots += draw_dots_polar(window)
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
