import numpy as np
import argparse
import cv2

# Argument parser dengan default gambar
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", default="lupi.jpg",
    help="Path ke file gambar (default: lupi.jpg)")
args = vars(ap.parse_args())

# Membaca gambar
image = cv2.imread(args["image"])
if image is None:
    raise ValueError(f"Gagal membaca file gambar: {args['image']}")
cv2.imshow("Original", image)

# --- 8.1: AVERAGING BLUR ---
# Menggabungkan beberapa versi gambar dengan ukuran kernel berbeda
blurred = np.hstack([
    cv2.blur(image, (3, 3)),
    cv2.blur(image, (5, 5)),
    cv2.blur(image, (7, 7))
])

cv2.imshow("Averaged", blurred)
cv2.waitKey(0)
