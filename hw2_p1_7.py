import numpy as np
import dip
import opener
import view


mat = opener.pgm2mat('dataset/Cross.pgm')
mat = np.lib.pad(mat, ((28,28),(28,28)), 'constant', constant_values=(255,255))

G = np.array([[0, 0, 1, 0, 0],
              [0, 1, 1, 1, 0],
              [1, 1, -5, 1, 1],
              [0, 1, 1, 1, 0],
              [0, 0, 1, 0, 0]
             ])

R = dip.convolute(mat, G, [2,2])

G = np.lib.pad(G, (((mat.shape[1]-G.shape[1])/2 +1,(mat.shape[1]-G.shape[1])/2),((mat.shape[0]-G.shape[0])/2 +1,(mat.shape[0]-G.shape[0])/2)), 'constant', constant_values=(0,0))

fmat = np.fft.fftshift(np.fft.fft2(mat))
fG = np.fft.fftshift(np.fft.fft2(G))

opener.mat2pgm('report/h2_p1_7_amp_bfilter.pgm', dip.norm(np.log(np.abs(fmat)+1)))
fmat = fmat * fG
opener.mat2pgm('report/h2_p1_7_amp_afilter.pgm', dip.norm(np.log(np.abs(fmat)+1)))
imat = np.fft.ifft2(np.fft.ifftshift(fmat))
imat = np.abs(imat)

opener.mat2pgm('report/h2_p1_7_ifft.pgm', dip.norm(imat))
opener.mat2pgm('report/h2_p1_7_conv.pgm', dip.norm(R))
