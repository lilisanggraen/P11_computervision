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

# 8.1 AVERAGING BLUR
# Gunakan cv2.blur() dengan berbagai ukuran kernel
blurred_avg = np.hstack([
    cv2.blur(image, (3, 3)),
    cv2.blur(image, (5, 5)),
    cv2.blur(image, (7, 7))
])
cv2.imshow("Averaging Blur", blurred_avg)
cv2.waitKey(0)

# 8.2 GAUSSIAN BLUR
# Gunakan cv2.GaussianBlur() — lebih natural karena berbobot
blurred_gaussian = np.hstack([
    cv2.GaussianBlur(image, (3, 3), 0),
    cv2.GaussianBlur(image, (5, 5), 0),
    cv2.GaussianBlur(image, (7, 7), 0)
])
cv2.imshow("Gaussian Blur", blurred_gaussian)
cv2.waitKey(0)

# 8.3 MEDIAN BLUR
# Gunakan cv2.medianBlur() — efektif untuk menghapus noise tipe "salt-and-pepper"
blurred_median = np.hstack([
    cv2.medianBlur(image, 3),
    cv2.medianBlur(image, 5),
    cv2.medianBlur(image, 7)
])
cv2.imshow("Median Blur", blurred_median)
cv2.waitKey(0)

cv2.destroyAllWindows()

# 8.4 BILATERAL BLUR
# ======================================================
# Parameter: diameter, sigmaColor, sigmaSpace
blurred_bilateral = np.hstack([
    cv2.bilateralFilter(image, 5, 21, 21),
    cv2.bilateralFilter(image, 7, 31, 31),
    cv2.bilateralFilter(image, 9, 41, 41)
])
cv2.imshow("Bilateral Blur", blurred_bilateral)
cv2.waitKey(0)

cv2.destroyAllWindows()
