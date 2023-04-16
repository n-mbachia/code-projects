#!/usr/bin/python3
"""This code was adopted from Python Coding YouTube channel day 41..."""
import cv2

image1 = cd2.imread(users/mbachia/code-projects/learning/python-365/create.jpg)
window_name = 'Original image'

cv2.imshow(window_name, image1)
grey_img = cv2.cvtColor(image, cv2.COLOR_BRG2GRAY)
invert = cv2.bitwise_not(grey_img)

blur = cv2.GaussBlur(invert,(21, 21), 0)
invertblur = cv2.divide(grey_img, invertedblur, scale=256.0)

cv2.imwrite(users/mbachia/code-projects/python-365/sketch.png, sketch)

image = cv2.imread(user/mbachia/code-projects/python-365/sketch.png)

window_name = 'Sketch image'

cv2.imshow(window_name, image)

cv2.waitkey(0)

cv2.destroyAllWindows()
