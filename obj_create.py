import cv2
import numpy as np

photo = np.zeros((450, 450, 3), dtype='uint8')

# BGR
# photo[100:150, 200:280] = 52, 155, 235
cv2.rectangle(photo, (photo.shape[1]//2, photo.shape[0]//2), (100, 100), (64, 235, 52), thickness=3)
cv2.putText(photo, 'Some Image', (210, 280), cv2.FONT_HERSHEY_TRIPLEX, 1, (64, 235, 52))

cv2.imshow('Photo', photo)
cv2.waitKey(0)
