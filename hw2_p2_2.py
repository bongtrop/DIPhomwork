import opener
import cv2
import dip
import numpy as np
import view
import cal

nchess = opener.pgm2mat('dataset/Chess_noise.pgm')
nlenna = opener.pgm2mat('dataset/Lenna_noise.pgm')
chess = opener.pgm2mat('dataset/Chess.pgm')
lenna = opener.pgm2mat('dataset/Lenna.pgm')

fnchess = np.fft.fft2(nchess)
fnlenna = np.fft.fft2(nlenna)

print "(chess noise) no filter have rms = " + str(cal.rms(nchess, chess))
print "(lenna noise) no filter have rms = " + str(cal.rms(nlenna, lenna))

print "----------------------------------------------------------"

for s in range(5,100,10):
  gsmark = dip.filterdesign(fnchess.shape, 'gaussian', [s])
  inchess = np.fft.ifft2(dip.filter(fnchess, gsmark))
  #view.mat(inch)
  print "gaussian filter with s = " + str(s)
  print "(chess) have rms =" + str(cal.rms(dip.norm(np.abs(inchess)), chess))

  gsmark = dip.filterdesign(fnlenna.shape, 'gaussian', [s])
  ifnlenna = np.fft.ifft2(dip.filter(fnlenna, gsmark))
  print "(lenna) have rms = " + str(cal.rms(dip.norm(np.abs(ifnlenna)), lenna))

print "----------------------------------------------------------"

for n in range(3,10,1):
  print "median filter with n and m = " + str(n)
  print "(chess) have rms = " + str(cal.rms(dip.medianfilter(nchess,n,n), chess))
  print "(lenna) have rms = " + str(cal.rms(dip.medianfilter(nlenna,n,n), lenna))
