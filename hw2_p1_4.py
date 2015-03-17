import numpy as np
import dip
import opener

mat = opener.pgm2mat('dataset/Cross.pgm')
mat = np.lib.pad(mat, ((28,28),(28,28)), 'constant', constant_values=(255,255))

mat = dip.resize(mat, 0.5, 0.5)

opener.mat2pgm('report/Cross_ds.pgm', mat)

fmat = np.fft.fftshift(np.fft.fft2(mat))
amp = np.log(np.abs(fmat)+1)
phase = np.angle(fmat)

opener.mat2pgm('report/h2_p1_4_amp.pgm',dip.norm(amp))
opener.mat2pgm('report/h2_p1_4_phase.pgm',dip.norm(phase))
