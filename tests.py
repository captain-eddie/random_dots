
'''
testing probability stuff and things
'''

from matplotlib import pyplot as plt
import numpy as np
from circle_dots import circle_radius, circle_width, dot_radius

def main():
    #   vars and things and stuff
    r_values = np.random.uniform(low = 0, high = circle_radius - (circle_width * dot_radius) + 1, size = 1000)
    theta_values = np.random.uniform(low = 0, high = 360, size = 1000)
    x, y = [x for x in range(0, 1001)], [y for y in range(0, 361)]

    #   plot
    fig = plt.scatter(r_values, y)
    #fig = plt.scatter(theta_values, x)
    ax = plt.axes()
    ax.set_xlabel("Radius")
    #ax.set_ylabel("Theta")
    ax.set_ylabel("")

if __name__ == "__main__":
    main()
