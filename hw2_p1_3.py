import numpy as np
import dip
import opener
import math

mat = opener.pgm2mat('dataset/Cross.pgm')
mat = np.lib.pad(mat, ((28,28),(28,28)), 'constant', constant_values=(255,255))

r = math.pi/6
A = np.array([[math.cos(r),-1*math.sin(r)],[math.sin(r),math.cos(r)]])
B = np.array([[0],[0]])
mat = dip.affine(mat, A, B, ori=[mat.shape[0]/2, mat.shape[1]/2], fill=255)
opener.mat2pgm('report/Cross_rotate.pgm', mat)

fmat = np.fft.fftshift(np.fft.fft2(mat))
amp = np.log(np.abs(fmat)+1)
phase = np.angle(fmat)

opener.mat2pgm('report/h2_p1_3_amp.pgm',dip.norm(amp))
opener.mat2pgm('report/h2_p1_3_phase.pgm',dip.norm(phase))
