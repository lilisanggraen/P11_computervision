from matplotlib import pyplot as plt
import numpy as np
import argparse
import cv2

# --- Parsing argumen gambar dengan default lupi.jpg ---
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", default="lupi.jpg",
    help="Path ke file gambar (default: lupi.jpg)")
args = vars(ap.parse_args())

# --- Baca gambar ---
image = cv2.imread(args["image"])
if image is None:
    raise ValueError(f"Gagal membaca gambar: {args['image']}")

# --- Resize otomatis agar mirip ukuran contoh di buku ---
max_width = 300
if image.shape[1] > max_width:
    scale = max_width / image.shape[1]
    image = cv2.resize(image, (int(image.shape[1]*scale), int(image.shape[0]*scale)))

cv2.imshow("Original", image)

# --- Pisahkan channel warna ---
chans = cv2.split(image)
colors = ("b", "g", "r")

# --- Tampilkan 1D color histogram ---
plt.figure()
plt.title("‘Flattened’ Color Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")

for (chan, color) in zip(chans, colors):
    hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
    plt.plot(hist, color=color)
    plt.xlim([0, 256])

# --- Tampilkan 2D color histogram (mirip buku) ---
fig = plt.figure(figsize=(9, 3))

# Green & Blue
ax = fig.add_subplot(131)
hist = cv2.calcHist([chans[1], chans[0]], [0, 1], None, [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation="nearest", cmap="jet", vmin=0, vmax=4000)
ax.set_title("2D Color Histogram for G and B")
plt.colorbar(p)

# Green & Red
ax = fig.add_subplot(132)
hist = cv2.calcHist([chans[1], chans[2]], [0, 1], None, [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation="nearest", cmap="jet", vmin=0, vmax=4000)
ax.set_title("2D Color Histogram for G and R")
plt.colorbar(p)

# Blue & Red
ax = fig.add_subplot(133)
hist = cv2.calcHist([chans[0], chans[2]], [0, 1], None, [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation="nearest", cmap="jet", vmin=0, vmax=4000)
ax.set_title("2D Color Histogram for B and R")
plt.colorbar(p)

# --- Tampilkan semua plot ---
plt.tight_layout()
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
