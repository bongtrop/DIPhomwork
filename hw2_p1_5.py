import numpy as np
import dip
import opener

mat = opener.pgm2mat('dataset/Cross.pgm')
mat = np.lib.pad(mat, ((28,28),(28,28)), 'constant', constant_values=(255,255))

fmat = np.fft.fft2(mat)
amp = np.abs(fmat)
phase = np.angle(fmat)

iamp = np.fft.ifft2(amp)
iphase = np.fft.ifft2(phase)

iamp = np.log(np.abs(iamp))
iphase = np.log(np.abs(iphase))

opener.mat2pgm('report/h2_p1_5_amp.pgm',dip.norm(iamp))
opener.mat2pgm('report/h2_p1_5_phase.pgm',dip.norm(iphase))
