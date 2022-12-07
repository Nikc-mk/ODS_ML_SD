import cv2 as cv


def change_photo(image_name):
    # загружаем изображение, с помощью COLOR_BGR2GRAY делаем изображение черно-белым
    image = cv.imread(
        f"/home/Nikolay/PycharmProjects/ODS_ML_SD/models/download_photo/{image_name}",
        cv.COLOR_BGR2GRAY)

    # делаем изображение более контрастным
    # image = cv.equalizeHist(image)

    face_cascade = cv.CascadeClassifier(
        "/home/Nikolay/PycharmProjects/ODS_ML_SD/models/cascades/haarcascade_frontalface_default.xml")

    faces = face_cascade.detectMultiScale(image, scaleFactor=1.2, minSize=(100, 100))
    for (x, y, w, h) in faces:
        center = (x + w // 2, y + h // 2)
        frame = cv.ellipse(image, center, (w // 2, h // 2), 0, 0, 360, (255, 0, 255), 4)

    cv.imwrite(f"/home/Nikolay/PycharmProjects/ODS_ML_SD/models/save_photo/{image_name}-1.jpg",
               img=frame)
