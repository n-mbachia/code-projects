import pywhatkit as kit
import cv2

Handwritten = input("Enter your text to convert in Hnadwriting : ")
kit.text_to_handweriting(Handwritten, save_to="mncapital.png")
img = cv2.imread("mncapital.pgn")
cv2.imshow("mn Capital", img)
cv2.waitkey(0)
cv2.destroyAllWindows()

