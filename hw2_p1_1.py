import numpy as np
import dip
import opener

mat = opener.pgm2mat('dataset/Cross.pgm')
mat = np.lib.pad(mat, ((28,28),(28,28)), 'constant', constant_values=(255,255))
fmat = np.fft.fftshift(np.fft.fft2(mat))
amp = np.log(np.abs(fmat)+1)
phase = np.angle(fmat)

opener.mat2pgm('report/h2_p1_1_amp.pgm',dip.norm(amp))
opener.mat2pgm('report/h2_p1_1_phase.pgm',dip.norm(phase))
