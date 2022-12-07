import cv2 as cv
import numpy as np



def change_photo_2(image_name, alpha=1.0, beta=0.7):
    # загружаем изображение, с помощью COLOR_BGR2GRAY делаем изображение черно-белым
    image = cv.imread(
        f"/home/Nikolay/PycharmProjects/ODS_ML_SD/models/download_photo/{image_name}")
    img_gray = cv.imread(
        f"/home/Nikolay/PycharmProjects/ODS_ML_SD/models/download_photo/{image_name}",
        cv.COLOR_BGR2GRAY)


    image_sketch = cv.pencilSketch(image)[1]

    face_cascade = cv.CascadeClassifier(
        "/home/Nikolay/PycharmProjects/ODS_ML_SD/models/cascades/haarcascade_frontalface_default.xml")
    height, width, depth = image.shape
    circle_mask = np.zeros((height, width), np.uint8)

    faces = face_cascade.detectMultiScale(img_gray, scaleFactor=1.2, minSize=(100, 100))
    for (x, y, w, h) in faces:
        center = (x + w // 2, y + h // 2)
        mask = cv.circle(circle_mask, center, h // 2, (255, 0, 255), -1)

    inv_mask = (mask == 0).astype("int8")
    face_inner = cv.bitwise_and(image_sketch, image_sketch, mask=mask)
    face_outer = cv.bitwise_and(image, image, mask=inv_mask)


    image_out = cv.addWeighted(face_inner, alpha, face_outer, beta, 0)

    cv.imwrite(f"/home/Nikolay/PycharmProjects/ODS_ML_SD/models/save_photo/out{image_name}",
               img=image_out)


# change_photo()