# import the necessary packages
import numpy as np
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=False, default="lupi.jpg",
    help="Path to the image (default: lupi.jpg)")
args = vars(ap.parse_args())

# load the image, convert it to grayscale
image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# apply histogram equalization
eq = cv2.equalizeHist(image)

# show the original image and equalized image side by side
cv2.imshow("Histogram Equalization", np.hstack([image, eq]))
cv2.waitKey(0)
