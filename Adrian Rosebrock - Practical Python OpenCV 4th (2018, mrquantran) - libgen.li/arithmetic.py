from __future__ import print_function
import numpy as np
import argparse
import cv2

# Argument parser dengan default file gambar
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=False, default="lupi.jpg",
    help="Path to the image")
args = vars(ap.parse_args())

# Baca gambar
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# Contoh operasi penjumlahan dan pengurangan pixel
print("max of 255: {}".format(cv2.add(np.uint8([200]), np.uint8([100]))))
print("min of 0: {}".format(cv2.subtract(np.uint8([50]), np.uint8([100]))))
print("wrap around (NumPy +): {}".format(np.uint8([200]) + np.uint8([100])))
print("wrap around (NumPy -): {}".format(np.uint8([50]) - np.uint8([100])))

# Tambahkan nilai pada seluruh pixel (lebih terang)
M = np.ones(image.shape, dtype="uint8") * 100
added = cv2.add(image, M)
cv2.imshow("Added", added)

# Kurangi nilai pada seluruh pixel (lebih gelap)
M = np.ones(image.shape, dtype="uint8") * 50
subtracted = cv2.subtract(image, M)
cv2.imshow("Subtracted", subtracted)

cv2.waitKey(0)
cv2.destroyAllWindows()
