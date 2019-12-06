# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 16:54:26 2019
@author: Nathan and Curtis
"""

import argparse
import matplotlib.pyplot as plt
import multiprocessing as mp
import numpy as np

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
    plt.axis('off')
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
    return np.array([(sum(rgb) // 3,)*3 for rgb in row])

def grey_scale(im):
    """
    Arguments:
        (numpy.ndarray): image to turn to grey
    Returns:
        numpy.ndarray: grey scale image
    """
    with mp.Pool(PARALLEL) as p:
        return np.array(list(p.imap(grey_scale_row, im)))

def black_white_row(row):
    """
    Arguments:
        row: (numpy.ndarray): row of rgb values
    Returns:
        numpy.ndarray: the black and white of the row
    """
    return np.array([(sum(rgb) // 383 * 255,)*3 for rgb in row])

def black_white(im):
    """
    Arguments:
        (numpy.ndarray): image to turn to black and white
    Returns:
        numpy.ndarray: black and white image
    """
    with mp.Pool(PARALLEL) as p:
        return np.array(list(p.imap(black_white_row, im)))

def red_shift_row(row):
    """
    Arguments:
        row: (numpy.ndarray): row of rgb values
    Returns:
        numpy.ndarray: the red shifted of the row
    """
    return np.array([rgb //4*(4,1,1) for rgb in row])


def red_shift(im):
    """
    Arguments:
        (numpy.ndarray): red shifted image
    Returns:
        numpy.ndarray: red shifted image
    """
    with mp.Pool(PARALLEL) as p:
        return np.array(list(p.imap(red_shift_row, im)))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Convert image colors")
    parser.add_argument('--conversion_type', '-C', metavar= '-C', default= 'G',
                        help = ('options are R for red_scale\n G for grayscale'
                                '\n B for black and white \n and I for invet'))
    parser.add_argument('--image_path','-I', metavar= 'I', required = True,
                        help = 'path to jpg image')
    parser.add_argument('--threads', '-T', default = 4, type=int,
                        help = 'number of parallel threads')
    args = parser.parse_args()

    im = read(args.image_path)

    PARALLEL = args.threads

    if args.conversion_type == 'R':
        show(red_shift(im))
    elif args.conversion_type == 'G':
        show(grey_scale(im))
    elif args.conversion_type == 'B':
        show(black_white(im))
    elif args.conversion_type == 'I':
        show(invert(im))
    else:
        print("Invalid conversion variable")