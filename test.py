import opener
import cv2
import dip
import view
import numpy as np

'''
mat = opener.pgm2mat('dataset/grid.pgm')

F = 255 - mat
G = np.array([[0, 0, 1, 0, 0],
              [0, 0, 1, 0, 0],
              [1, 1, 1, 1, 1],
              [0, 0, 1, 0, 0],
              [0, 0, 1, 0, 0]
             ])

R = dip.convolute(F, G, [2,2])
R = dip.norm(R)

R[R<200] = 0
R[R>=200] = 255

grid = np.where(R==255)
grid_x = grid[1] - 1
grid_y = grid[0] - 1
'''

# Distgrid not automatic
mat = opener.pgm2mat('dataset/distgrid.pgm')

F = 255 - mat
G = np.array([[1, 1, 1],
              [1, 0, 1],
              [1, 1, 1]

             ])

R = dip.convolute(F, G, [2,2])
R = dip.norm(R)
bw = dip.localotsu(R, 15, 15)
view.mat(R, "Con")
view.mat(bw, "BW")
view.show()
