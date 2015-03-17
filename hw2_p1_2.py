import numpy as np
import dip
import opener
import math
import cmath

mat = opener.pgm2mat('dataset/Cross.pgm')
mat = np.lib.pad(mat, ((28,28),(28,28)), 'constant', constant_values=(255,255))
fmat = np.fft.fftshift(np.fft.fft2(mat))

sx = 20.0
sy = 30.0

for i in range(0,fmat.shape[1]):
    for j in range(0,fmat.shape[0]):
        fmat[i,j] = fmat[i,j]*cmath.exp(-2j*math.pi*(i*sx/fmat.shape[1]+j*sy/fmat.shape[0]))


im = np.fft.ifft2(np.fft.ifftshift(fmat))
im = np.abs(im)
opener.mat2pgm('report/hw2_p1_2_sim.pgm', dip.norm(im))
