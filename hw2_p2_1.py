import opener
import cv2
import dip
import numpy as np

mat = opener.pgm2mat('dataset/Cross.pgm')
fmat = np.fft.fft2(mat)

idmark = dip.filterdesign(fmat.shape, 'ideal', [10])
imat = np.fft.ifft2(dip.filter(fmat, idmark))
opener.mat2pgm('report/h2_p2_1_ideal10.pgm', dip.norm(np.abs(imat)))

idmark = dip.filterdesign(fmat.shape, 'ideal', [50])
imat = np.fft.ifft2(dip.filter(fmat, idmark))
opener.mat2pgm('report/h2_p2_1_ideal50.pgm', dip.norm(np.abs(imat)))

idmark = dip.filterdesign(fmat.shape, 'ideal', [100])
dip.filter(fmat, idmark)
imat = np.fft.ifft2(dip.filter(fmat, idmark))
opener.mat2pgm('report/h2_p2_1_ideal100.pgm', dip.norm(np.abs(imat)))


idmark = dip.filterdesign(fmat.shape, 'gaussian', [10])
imat = np.fft.ifft2(dip.filter(fmat, idmark))
opener.mat2pgm('report/h2_p2_1_gs10.pgm', dip.norm(np.abs(imat)))

idmark = dip.filterdesign(fmat.shape, 'gaussian', [50])
imat = np.fft.ifft2(dip.filter(fmat, idmark))
opener.mat2pgm('report/h2_p2_1_gs50.pgm', dip.norm(np.abs(imat)))

idmark = dip.filterdesign(fmat.shape, 'gaussian', [100])
imat = np.fft.ifft2(dip.filter(fmat, idmark))
opener.mat2pgm('report/h2_p2_1_gs100.pgm', dip.norm(np.abs(imat)))
