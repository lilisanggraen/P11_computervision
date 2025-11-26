import cv2
import numpy as np

image = cv2.imread("lupi.jpg")
cv2.imshow("Original", image)

# Buat mask hitam dengan ukuran sama seperti gambar
mask = np.zeros(image.shape[:2], dtype="uint8")

# Gambar lingkaran putih di tengah
(cX, cY) = (image.shape[1] // 2, image.shape[0] // 2)
cv2.circle(mask, (cX, cY), 100, 255, -1)
cv2.imshow("Mask", mask)

# Terapkan mask pada gambar
masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Mask Applied to Image", masked)

cv2.waitKey(0)
