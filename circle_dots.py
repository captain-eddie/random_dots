
'''
Edward Abel-Guobadia
1-19-2023
'''

import pygame as pg
import constants

def main():
    pg.init()

    #   program window
    window = pg.display.set_mode((100, 100))

    #   draw circle
    pg.draw.circle(window, constants.WHITE, (50, 50), 10.0)

    #   main window loop
    while True:
        pg.display.update()

        #   window event handler
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()


if __name__ == "__main__":
    main()
