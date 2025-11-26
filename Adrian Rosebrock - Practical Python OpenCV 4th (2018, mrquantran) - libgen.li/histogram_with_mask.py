from matplotlib import pyplot as plt
import numpy as np
import argparse
import cv2

# Fungsi untuk menampilkan histogram RGB
def plot_histogram(image, title, mask=None):
    chans = cv2.split(image)
    colors = ("b", "g", "r")
    plt.figure()
    plt.title(title)
    plt.xlabel("Bins")
    plt.ylabel("# of Pixels")

    for (chan, color) in zip(chans, colors):
        hist = cv2.calcHist([chan], [0], mask, [256], [0, 256])
        plt.plot(hist, color=color)
        plt.xlim([0, 256])

# Argument parser (dengan default = lupi.jpg)
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", default="lupi.jpg",
    help="Path ke file gambar (default: lupi.jpg)")
args = vars(ap.parse_args())

# Baca gambar
image = cv2.imread(args["image"])
if image is None:
    raise ValueError(f"Gagal membaca file gambar: {args['image']}")
cv2.imshow("Original", image)

# Histogram untuk gambar asli
plot_histogram(image, "Histogram for Original Image")

# Membuat mask (hitam) lalu isi persegi putih
mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.rectangle(mask, (15, 15), (130, 100), 255, -1)
cv2.imshow("Mask", mask)

# Terapkan mask ke gambar
masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Applying the Mask", masked)

# Histogram untuk area yang dimask
plot_histogram(image, "Histogram for Masked Image", mask=mask)

plt.show()
cv2.waitKey(0)
