import pywhatkit as kit 
import cv2

kit.text_to_handwriting("GOWRITHEERTHA", save_to="LOCAL.png")

img = cv2.imread("handwriting.png")
cv2.imgshow("text To Handwriting", img)

cv2.waitKey(0)
cv2.destroyAllWindows()