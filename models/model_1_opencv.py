import cv2 as cv

# загружаем изображение, с помощью COLOR_BGR2GRAY делаем изображение черно-белым
image = cv.imread("photo_2022.jpg", cv.COLOR_BGR2GRAY)


def change_photo(image):
    # делаем изображение более контрастным
    # image = cv.equalizeHist(image)

    face_cascade = cv.CascadeClassifier("cascades/haarcascade_frontalface_default.xml")

    faces = face_cascade.detectMultiScale(image)
    for (x, y, w, h) in faces:
        center = (x + w // 2, y + h // 2)
        frame = cv.ellipse(image, center, (w // 2, h // 2), 0, 0, 360, (255, 0, 255), 4)


    cv.imshow('Capture - Face detection', frame)
    cv.waitKey(0)


change_photo(image=image)
