import cv2 as cv
import webbrowser

if __name__ == '__main__':
    cap = cv.VideoCapture(1)
    detector = cv.QRCodeDetector()

    while cap.isOpened():
        print("capture running")
        _, img = cap.read()
        cv.imshow("QRCODEscanner", img)

        a, _, _ = detector.detectAndDecode(img)

        if a:
            print("received qr code")
            a, _, _ = detector.detectAndDecode(img)

            print(str(a))

        if cv.waitKey(1) == ord("q"):
            break
print("capture stopped")
cap.release()
cv.destroyAllWindows()
