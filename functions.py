import os
from pickle import FRAME
import re
import cv2
from cv2 import imshow # opencv library
import numpy as np
from os.path import isfile, join
import matplotlib.pyplot as  plot
import constants

def read_images(path):
    """Reads all images from frames folder and returns them in a sorted list

    Args:
        path (string): path to the folder that contains all frames.

    Returns:
        list: all images sorted by name.
    """
    # import video frames from the folder in a list
    # os.listdir returns all file names inside given folder
    col_frames = os.listdir(constants.FRAME_PATH) 

    # use a lambda to sort the file names (\D indicates a pattern with any int)
    col_frames.sort(key=lambda frame: int(re.sub('\D','', frame)))

    # fill a list with the images in frame_path
    col_images = []
    for frame in col_frames:
        img = cv2.imread(constants.FRAME_PATH+frame)
        col_images.append(img)
    return col_images
