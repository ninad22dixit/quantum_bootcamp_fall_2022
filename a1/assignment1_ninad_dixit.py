"""Develop ASCII-based function plotter"""

# Import relevant libraries

from numpy.typing import NDArray
import numpy as np
import math


def color(text: str, rgb: tuple):
    """
    Returns a colored string using ANSI codes.
    Parameters
    ----------
    :param text: The text to color
    :param rgb: The RGB color components
    """
    r, g, b = rgb
    return f"\033[38;2;{r};{g};{b}m{text}\033[m"

"""Part 1: Print multidimensional array to the standard output."""

canvas = [["+", "-", "-", "-", "+"], ["|", " ", " ", " ", "|"], ["|", " ", " ", " ", "|"], ["+", "-", "-", "-", "+"]]

def print_chart(canvas: NDArray) -> None:
    for array in canvas:
        print(''.join(array))

"""Part 2: Initializing the plot’s main canvas (the cartesian plane)"""

def draw_canvas(grid: int, height: int = 15, width: int = 100) -> None:

    # x-values -> width, y-values -> height

    array = np.empty((height, width), dtype="<U30")

    for h in range(height):
        for w in range(width):
            if (h == 0 and w == 0) or (h == 0 and w == width-1):
                array[h][w] = '+'
            elif (h == height-1 and w == 0) or (h == height-1 and w == width-1):
                array[h][w] = '+'
            elif (h == 0 or h == height-1):
                array[h][w] = '-'
            elif (w == 0 or w == width-1):
                array[h][w] = '|'
            else:
                if grid == 1:
                    array[h][w] = '.'
                else: array[h][w] = ' '

    print_chart(array)

"""Part 3: Normalize and scale the data points"""

def normalize_and_scale(x: list, y: list, height: int = 15, width: int = 100):

    # x-values -> width, y-values -> height

    x_axis = np.asarray(x)
    y_axis = np.asarray(y)

    min1, max1 = np.min(x_axis), np.max(x_axis)
    min2, max2 = np.min(y_axis), np.max(y_axis)

    for a in range(len(x_axis)):
        x_axis[a] = (x_axis[a]-min1)/(max1-min1)*width
        math.floor(x_axis[a])
        if x_axis[a] < min1:
            x_axis[a] = min1
        if x_axis[a] > max1:
            x_axis[a] = max1

    for b in range(len(y_axis)):
        y_axis[b] = height - (y_axis[b]-min2)/(max2-min2)*height
        math.floor(y_axis[b])
        if y_axis[b] < min2:
            y_axis[b] = min2
        if y_axis[b] > max2:
            y_axis[b] = max2

    return x_axis, y_axis

"""Part 4: Drawing the data points on the canvas"""

def draw_on_canvas(x1, y1, grid: int, height: int = 15, width: int = 100):

    # x-values -> width, y-values -> height

    array = np.empty((height, width), dtype="<U30")

    for h in range(height):
        for w in range(width):
            if (w == 0 and h == 0) or (w == width-1 and h == 0):
                array[h][w] = '+'
            elif (w == 0 and h == height-1) or (w == width - 1 and h == height - 1):
                array[h][w] = '+'
            elif (h == 0 or h == height - 1):
                array[h][w] = '-'
            elif (w == 0 or w == width - 1):
                array[h][w] = '|'
            else:
                if grid == 1:
                    array[h][w] = '.'
                else:
                    array[h][w] = ' '

    if grid == 1:
        array[height - y1][x1] = '*'
    else:
        array[height - y1][x1] = '.'

    print_chart(array)

    return array

"""Part 5: Adding the x and y axes"""

def add_axes(x1: int = 56, y1: int = 12, grid: int = 0, height: int = 15, width: int = 100):

    x_label = np.empty((width-2), dtype="<U30")
    y_label = np.empty((height-1), dtype="<U30")

    x_label = list(x_label)
    x_label.append('0')
    x_label[::-1]
    x_label.append('100')
    x_label = np.array(x_label).reshape(1,width)

    y_label = list(y_label)
    y_label.append('15')
    y_label[::-1]
    y_label.append('0')
    y_label = np.array(y_label).reshape(height+1,1)
    array = draw_on_canvas(x1,y1,0)
    print(x_label.shape)
    print(array.shape)

    mod_array = np.vstack((array,x_label))
    print(mod_array.shape)
    print(y_label.shape)

    mod_array = np.hstack((y_label,mod_array))

    print_chart(mod_array)
    #print(mod_array)

    print(x_label[0][0].dtype)


if __name__ == '__main__':

    scale = 0.1
    n = int(8 * math.pi / scale)
    x = [scale * i for i in range(n)]
    y = [math.sin(scale * i) for i in range(n)]
    height = 15
    width = 100
    title = "The sine function"
    legend = "f(x) = sin(x), where 0 <= x <= 8π"
    primary_color = (255, 0, 0)
    secondary_color = (200, 200, 200)
    grid = 0

    add_axes()



