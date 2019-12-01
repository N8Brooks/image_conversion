# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 16:54:26 2019

@author: Nathan
"""

import matplotlib.pyplot as plt
import multiprocessing as mp
import numpy as np

PARALLEL = 8

def read(file):
    """
    Arguments:
        file (int): path to image file to be read
    Returns
        numpy.ndarray: RGB array of image
    """
    im = plt.imread(file)
    return im

def show(im):
    """
    Arguments:
        im (numpy.ndarray): image array to display
    """
    plt.imshow(im)
    plt.show()

def invert(im):
    """
    Arguments:
        im (numpy.ndarray): image to invert
    Returns:
        numpy.ndarray: inverted image
    """
    return 255 - im

def grey_scale_row(row):
    """
    Arguments:
        row: (numpy.ndarray): row of rgb values
    Returns:
        numpy.ndarray: the greyscale of the row
    """
    return np.array([tuple([sum(x)//3]*3) for x in row])

def grey_scale(im):
    """
    Arguments:
        (numpy.ndarray): image to turn to grey
    Returns:
        numpy.ndarray: grey scale image
    """
    with mp.Pool(PARALLEL) as p:
        return np.array(list(p.imap(grey_scale_row, im)))

def black_white(im):
    """
    Arguments:
        (numpy.ndarray): image to turn to black and white
    Returns:
        numpy.ndarray: black and white image
    """
    im = im.copy()
    for y, row in enumerate(im):
        for x, rgb in enumerate(row):
            im[y][x].fill(rgb.sum() // 383 * 255)
    return im

if __name__ == '__main__':
    im = read('example.JPG')
    
    show(grey_scale(im))
    show(black_white(im))
    show(invert(im))

            