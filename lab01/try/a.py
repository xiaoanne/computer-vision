import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread('a.jpg', cv2.IMREAD_GRAYSCALE)

# cv2.imshow('image', img)
# cv2.waitKey(0)
# cv2.destroyWindow()

plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.show()


cap = cv2.VideoCapture('./a.webm')
while True:
    ret, frame = cap.read()
    # plt.imshow('frame', frame)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()