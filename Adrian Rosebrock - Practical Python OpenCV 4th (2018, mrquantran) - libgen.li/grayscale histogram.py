from matplotlib import pyplot as plt
import argparse
import cv2

# Argument parser (dengan default gambar)
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", default="lupi.jpg",
    help="Path ke file gambar (default: lupi.jpg)")
args = vars(ap.parse_args())

# Membaca dan konversi gambar ke grayscale
image = cv2.imread(args["image"])
if image is None:
    raise ValueError(f"Gagal membaca gambar: {args['image']}")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", gray)

# Hitung histogram grayscale
hist = cv2.calcHist([gray], [0], None, [256], [0, 256])

# Tampilkan histogram menggunakan Matplotlib
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(hist, color='blue')
plt.xlim([0, 256])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

