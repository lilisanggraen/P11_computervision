import numpy as np
import cv2
import argparse
import time

# ==========================================================
# Argument parser (dengan default gambar)
# ==========================================================
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", default="lupi.jpg",
                help="Path ke file gambar (default: lupi.jpg)")
args = vars(ap.parse_args())

# ==========================================================
# Membaca gambar
# ==========================================================
image = cv2.imread(args["image"])
if image is None:
    raise ValueError(f"Gagal membaca gambar: {args['image']}")

# ==========================================================
# Konversi ke berbagai color space
# ==========================================================
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

# ==========================================================
# Tampilkan keempat jendela
# ==========================================================
cv2.imshow("Original", image)
cv2.imshow("Gray", gray)
cv2.imshow("HSV", hsv)
cv2.imshow("L*a*b*", lab)

print("🖼️ Tekan tombol apa saja untuk menutup semua jendela...")
cv2.waitKey(0)

cv2.destroyAllWindows()
time.sleep(0.5)

