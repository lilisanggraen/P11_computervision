import cv2

image = cv2.imread(r"C:\Computer Vision\tss.png")
if image is None:
    print("Gambar tss.png tidak ditemukan!")
    exit()

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

max_width = 800
max_height = 600
height, width = image.shape[:2]
scale = min(max_width / width, max_height / height, 1)
new_size = (int(width * scale), int(height * scale))
image_resized = cv2.resize(image, new_size)

cv2.imshow("Detected Faces", image_resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

