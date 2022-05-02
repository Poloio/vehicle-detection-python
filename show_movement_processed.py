from email import iterators
from signal import valid_signals
from cv2 import dilate, threshold
import numpy as np
import functions 
import constants
import cv2
import matplotlib.pyplot as plot

# Read all frames
col_images = functions.read_images(constants.FRAME_PATH)
# Index frame nº 13 for testing purposes
position = 13

# Show original image
plot.imshow(col_images[position])
plot.title("Original frame")
plot.show()

# Turn two frames to grayscale
grayA = cv2.cvtColor(col_images[position],cv2.COLOR_BGR2GRAY)
grayB = cv2.cvtColor(col_images[position+1],cv2.COLOR_BGR2GRAY)

# Proccess movement between frames
diff_image = cv2.absdiff(grayA, grayB)

# *Using two variables because threshold() returns two values
# Divides the image in clearer white and black zones
ret, thresh_img = cv2.threshold(diff_image,30,255,cv2.THRESH_BINARY)
plot.imshow(thresh_img, cmap='gray')
plot.title("Without dilation")
plot.show()

# Create numpy 3x3 int8 matrix/array for image dilation
# Kernel represents the binary matrix that will ocupy every white pixel's position
kernel = np.ones((3,3),np.uint8)
dilated_img = cv2.dilate(thresh_img, kernel, iterations=1)
plot.imshow(dilated_img,cmap="gray")
plot.title("After dilation")
plot.show()

# Draws line to separate detection zone
# line(img, coordinate1, coordinate2, rgb)
cv2.line(dilated_img, (0, 80),(256,80),(100,0,0))
plot.imshow(dilated_img)
plot.title("Zone definition")

plot.show()

# Now to find vehicle contours in the detection zone
# findcontours(img, mode, method)
contours, hierarchy = cv2.findContours(dilated_img,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

valid_contours = []
# Filter valid contours that are in the zone
for i, contour in enumerate(contours):
    x,y,wt,ht = cv2.boundingRect(contour) # Get contour's rectangle dimensions and position
    if x <= 200 and y >= 80 and cv2.contourArea(contour) >= 25:
        valid_contours.append(contour)
print ("Cars found: "+str(len(valid_contours)))

# Plot contours over the original image
result_img = col_images[position+1].copy()
cv2.drawContours(result_img,valid_contours,-1,(127,200,0), 2)
plot.imshow(result_img)
plot.title("Plotted contour")
plot.show()



    
    
