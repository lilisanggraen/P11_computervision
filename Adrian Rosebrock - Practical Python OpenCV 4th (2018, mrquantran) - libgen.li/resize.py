import numpy as np
import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=False, default="luppy.jpg",
                help="Path ke file gambar (default: luppy.jpg)")
args = vars(ap.parse_args())

# Baca dan tampilkan gambar asli
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# Resize berdasarkan width (150px)
r = 150.0 / image.shape[1]
dim = (150, int(image.shape[0] * r))
resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("Resized (Width = 150)", resized)

# Resize berdasarkan height (50px)
r = 50.0 / image.shape[0]
dim = (int(image.shape[1] * r), 50)
resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("Resized (Height = 50)", resized)

# Resize via fungsi imutils.resize
resized = imutils.resize(image, width=100)
cv2.imshow("Resized via Function (Width = 100)", resized)

cv2.waitKey(0)
cv2.destroyAllWindows()
