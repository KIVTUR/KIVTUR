import cv2

cam = cv2.VideoCapture(0)

cv2.namedWindow("Python Webcam Screenshot App")

image_counter = 0

while True:

    check ,frame = cam.read()
    cv2.imshow("Python Webcam Screenshot App", frame)
    k = cv2.waitKey(1)

    if k == ord('s'):
        print("Escape hit, closing the app.")
        break

    elif k == ord('a'):
        image_name = "Rutvik{}.jpg".format(image_counter)
        cv2.imwrite(image_name, frame)
        print("Screenshohot taken.")
        image_counter += 1

cam.release()

cv2.destroyAllWindows()
