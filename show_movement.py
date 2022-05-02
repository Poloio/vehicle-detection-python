import functions 
import constants
import cv2
import matplotlib.pyplot as plot
# Read all frames
col_images = functions.read_images(constants.FRAME_PATH)
# Index frame nº 13 for testing purposes
position = 13

# Turn two frames to grayscale
grayA = cv2.cvtColor(col_images[position],cv2.COLOR_BGR2GRAY)
grayB = cv2.cvtColor(col_images[position+1],cv2.COLOR_BGR2GRAY)

# Calculate and show absolute diff between them
plot.imshow(cv2.absdiff(grayA, grayB), cmap='gray')
plot.show()
