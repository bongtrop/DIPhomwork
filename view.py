import cv2
import sys

im = cv2.imread(sys.argv[1])
print im.shape
cv2.imshow('Image', im)
cv2.waitKey(0)
