import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=False, default="lupi.jpg",
    help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

(h, w) = image.shape[:2]

cropped = image[int(h*0.55):int(h*0.85), int(w*0.35):int(w*0.65)]

cv2.imshow("Cropped (Lower Box)", cropped)
cv2.waitKey(0)
