from time import sleep
import cv2 as cv
import csv


if __name__ == '__main__':
    cap = cv.VideoCapture(1)
    detector = cv.QRCodeDetector()

    while cap.isOpened():
        _, img = cap.read()
        cv.imshow("QRCODEscanner", img)

        a, _, _ = detector.detectAndDecode(img)

        if a:
            print("received qr code")
            dat = a.split("\t")

            print(str(dat))

            cv.putText(img, "Detected QR Code!", (200, 200),
                       cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255))

            cv.imshow("QRCODEscanner", img)

            with open('current.csv', 'a') as f:
                writer = csv.writer(f)

                writer.writerow(dat)

            sleep(7.5)

            print("Starting cap again")

        if cv.waitKey(1) == ord("q"):
            break
print("capture stopped")
cap.release()
cv.destroyAllWindows()
