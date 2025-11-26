import numpy as np
import argparse
import cv2
import time

# Argument parser dengan default gambar
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", default="lupi.jpg", help="Path ke file gambar (default: lupi.jpg)")
args = vars(ap.parse_args())

# Membaca gambar
image = cv2.imread(args["image"])
if image is None:
    raise ValueError(f"Gagal membaca gambar: {args['image']}")

# === BAGIAN 1: Split dan Merge Channel (grayscale) ===
(B, G, R) = cv2.split(image)  # <-- Tambahkan baris ini

cv2.imshow("Red Channel (Grayscale)", R)
cv2.imshow("Green Channel (Grayscale)", G)
cv2.imshow("Blue Channel (Grayscale)", B)
cv2.imshow("Merged Image", cv2.merge([B, G, R]))

print("Tekan tombol apa saja untuk lanjut ke versi berwarna...")
cv2.waitKey(0)

cv2.destroyAllWindows()
time.sleep(0.5)

# === BAGIAN 2: Visualisasi Channel Berwarna ===
zeros = np.zeros(image.shape[:2], dtype="uint8")

red_color = cv2.merge([zeros, zeros, R])
green_color = cv2.merge([zeros, G, zeros])
blue_color = cv2.merge([B, zeros, zeros])

cv2.imshow("Red Channel (Color)", red_color)
cv2.imshow("Green Channel (Color)", green_color)
cv2.imshow("Blue Channel (Color)", blue_color)

cv2.waitKey(0)
cv2.destroyAllWindows()
