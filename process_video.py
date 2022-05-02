from concurrent.futures import process
from email import iterators
from genericpath import isfile
from ntpath import join
import re
from signal import valid_signals
from cv2 import boundingRect, cvtColor, dilate, threshold
import os
import numpy as np
import functions 
import constants
import cv2
import matplotlib.pyplot as plot

def process_frames(in_images,dilation_kernel,out_path):
    """Processes all frame pairs to find contours 
    of moving vehicles in the view and writes them in its folder

    Args:
        in_images (List): all images to process in order
        dilation_kernel (Any): a cv2 kernel to manage dilation of white area process
        out_path (string): the path to write each frame in
    """
    for i in range(len(in_images)-1):
        # Image difference
        grayA = cv2.cvtColor(in_images[i], cv2.COLOR_BGR2GRAY)
        grayB = cv2.cvtColor(in_images[i+1], cv2.COLOR_BGR2GRAY)
        image_diff = cv2.absdiff(grayA,grayB)
        
        # Binary threshold pixel filter
        ret, filtered_img = cv2.threshold(image_diff, 30, 255, cv2.THRESH_BINARY)
        # Dilate image white zones
        dilated_img = cv2.dilate(filtered_img, kernel, iterations=1)
        
        cv2.line(dilated_img, (0,60), (250,60), (100,0,0))
        
        # Find contours
        valid_contours = []
        contours, hierarchy = cv2.findContours(dilated_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        for contour in contours:
            x, y, wh, ht = cv2.boundingRect(contour)
            if y >= 60 and y <= 250 and cv2.contourArea(contour) >= 25:
                valid_contours.append(contour)
        # Draw contours on original image
        final_image = in_images[i+1].copy()
        cv2.drawContours(final_image, valid_contours,-1, (127,200,0), 2)
        cv2.imwrite(out_path+str(i)+'.png', final_image)

processed_path = 'processed_frames\\'
in_images = functions.read_images(constants.FRAME_PATH)
kernel = np.ones((4,4),np.uint8)
process_frames(in_images, kernel, processed_path)

path_video = 'result.mp4'
fps = 14
files = []
files = [f for f in os.listdir(processed_path) if isfile(join(processed_path,f))]

files.sort(key=lambda f: int(re.sub('\D', '', f)))

frame_array = []
for i in range(len(files)):
    filename= processed_path + files[i]
    
    #read frames
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    
    #inserting the frames into an image array
    frame_array.append(img)

out = cv2.VideoWriter(path_video,cv2.VideoWriter_fourcc(*'DIVX'), fps, size)

for i in range(len(frame_array)):
    # writing to a image array
    out.write(frame_array[i])

out.release()



    
    
    
    
    
    



