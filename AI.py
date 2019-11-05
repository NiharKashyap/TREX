from numpy import *
from PIL import ImageGrab, ImageOps
import pyautogui as py


def pressSpace():
    py.keyDown('space')
    py.keyUp('space')


def IMG():
    Box = (190, 422, 245, 455)  # Use your own Coordinates here
    image = ImageGrab.grab(Box)
    image = ImageOps.grayscale(image)
    arr = array(image.getcolors())
    print(arr.sum())
    return (arr.sum())


def main():
    print("Starting Game.....")
    x = 0
    while (1):
        if (IMG() != 2062):
            pressSpace()
            x = x + 1
            print("     Jumping " + str(x) + " times")


main()