import cv2

# img = cv2.imread('images/coffee.png')
# cv2.imshow('coffee', img)

# cv2.waitKey(0)

#cap = cv2.VideoCapture('videos/video_2023-07-16_19-48-54.mp4')
cap = cv2.VideoCapture(0)
cap.set(3, 500)
cap.set(4, 500)
while True:
    success, img = cap.read()
    cv2.imshow('Video', img)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break


