import opener
import dip
import numpy as np
import cv2

mat = opener.pgm2mat('dataset/scaled_shapes.pgm')
hist = dip.mat2hist(mat)
print hist
dip.plothist(hist);
