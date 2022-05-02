import functions 
import constants
import cv2
import matplotlib.pyplot as plot
# Read all frames
col_images = functions.read_images(constants.FRAME_PATH)
# Index frame nº 13 for testing purposes
position = 13

for frame in [position,position+1]:
    # plots the frame to show
    plot.imshow(cv2.cvtColor(col_images[frame],cv2.COLOR_BGR2RGB))
    plot.title('frame: '+str(frame))
    # show the frame in a plot window
    plot.show()