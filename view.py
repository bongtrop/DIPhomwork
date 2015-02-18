import cv2
import numpy as np

def pgm(filename, name):
  im = cv2.imread(filename)
  cv2.imshow('Image '+name, im)

def mat(mat, name):
  mat[mat>255] = 255
  mat[mat<0] = 0
  mat = mat.astype(np.uint8)

  cv2.imshow('Mat '+name, mat)

def hist(hist, name):
  hist[255] = 0
  m = np.max(hist)
  x = 255.0/m
  hist = hist * x

  im = np.zeros((256,512), dtype=np.uint8)
  for i in range(0, 512, 2):
    f = int(round(hist[i/2]))
    for j in range(255, 255-f, -1):
      im[j][i] = 255

  cv2.imshow('Histogram '+name, im)

def show():
  cv2.waitKey(0)
