import cv2 as cv


def change_photo():
    # загружаем изображение, с помощью COLOR_BGR2GRAY делаем изображение черно-белым
    image = cv.imread(
        f"download_photo/AgACAgIAAxkBAAIWKWONO0LdcMjppmw3bF76vYvC7XAmAAIfxDEb6gNwSKMygFirIWenAQADAgADeQADKwQ.jpg",
        cv.COLOR_BGR2GRAY)

    # делаем изображение более контрастным
    # image = cv.equalizeHist(image)

    face_cascade = cv.CascadeClassifier("cascades/haarcascade_frontalface_default.xml")

    faces = face_cascade.detectMultiScale(image)
    for (x, y, w, h) in faces:
        center = (x + w // 2, y + h // 2)
        frame = cv.ellipse(image, center, (w // 2, h // 2), 0, 0, 360, (255, 0, 255), 4)

    cv.imwrite("save_photo/AgACAgIAAxkBAAIWKWONO0LdcMjppmw3bF76vYvC7XAmAAIfxDEb6gNwSKMygFirIWenAQADAgADeQADKwQ.jpg",
               img=frame)
    # cv.waitKey(0)


# change_photo()
