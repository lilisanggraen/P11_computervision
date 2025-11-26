import argparse
import cv2

# Membuat argument parser dengan default image
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=False, default="lupi.jpg",
    help="Path ke file gambar (default: lupi.jpg)")
args = vars(ap.parse_args())

# Membaca gambar
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# Flip horizontal (sekitar sumbu Y)
flipped = cv2.flip(image, 1)
cv2.imshow("Flipped Horizontally", flipped)

# Flip vertikal (sekitar sumbu X)
flipped = cv2.flip(image, 0)
cv2.imshow("Flipped Vertically", flipped)

# Flip horizontal & vertikal
flipped = cv2.flip(image, -1)
cv2.imshow("Flipped Horizontally & Vertically", flipped)

cv2.waitKey(0)
cv2.destroyAllWindows()
