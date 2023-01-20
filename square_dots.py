
'''
Edward Abel Guobadia
1-20-2023
'''

import pygame as pg
import constants

def main():
    #   variables and stuff
    window_size = (500, 500)
    side_length = 300.0
    square_pos = (100, 100)
    square_width = 2

    #   initialize pygame window
    pg.init()

    #   program window
    window = pg.display.set_mode(window_size)

    #   draw square
    square = pg.Rect(square_pos, (side_length, side_length))
    pg.draw.rect(window, constants.SQUARE_COLOR, square, square_width)

    #   main window loop
    while True:
        pg.display.update()

        #   window event handler
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()



if __name__ == "__main__":
    main()
