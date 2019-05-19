#pip install opencv-python
import cv2

#reads img as greyscale, prints dimensions (2 = correct), then writes img
img = cv2.imread(input("Path >"), 0)
print(len(img.shape))
cv2.imwrite("grey.png", img)
