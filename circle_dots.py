
'''
Edward Abel-Guobadia
1-19-2023
'''

import pygame as pg
import constants

def main():
    #   variables and things and stuff
    circle_pos = (250, 250)
    circle_radius = 150.0
    circle_width = 2

    #   initialize pygame window
    pg.init()

    #   program window
    window = pg.display.set_mode((500, 500))

    #   draw circle
    pg.draw.circle(window, constants.CIRCLE_COLOR, circle_pos, circle_radius, circle_width)

    #   main window loop
    while True:
        pg.display.update()

        #   window event handler
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()


if __name__ == "__main__":
    main()
