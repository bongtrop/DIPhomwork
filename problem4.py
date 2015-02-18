import opener
import cv2
import dip
import view
import numpy as np
import json

mat = opener.pgm2mat('dataset/grid.pgm')

# Convolute to find cross line
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
for i in range(16,256,16):
        R[255, i] = 255
        R[i, 255] = 255

R[255,255] = 255

view.mat(R, "Convolute Result")
opener.mat2pgm('report/convolute_p4.pgm', R)

grid_c = np.where(R==255)
grid_x = grid_c[1]
grid_y = grid_c[0]

grid = []

for i in range(0,256):
    g = {}
    g["n"] = i
    g["x1"] = grid_x[i] - 16
    g["y1"] = grid_y[i] - 16
    g["x2"] = grid_x[i]
    g["y2"] = grid_y[i] - 16
    g["x3"] = grid_x[i] - 16
    g["y3"] = grid_y[i]
    g["x4"] = grid_x[i]
    g["y4"] = grid_y[i]

    grid.append(g)

# Distgrid not automatic
json_data = open('distgrid.json')
distgrid = json.load(json_data)
json_data.close()

p = opener.pgm2mat('dataset/distgrid.pgm')
res = dip.controlgrid(p, grid, distgrid)
view.mat(res, "Result from distgrid")
opener.mat2pgm('report/distgrid_fix_p4.pgm', res)

p = opener.pgm2mat('dataset/distlenna.pgm')
res = dip.controlgrid(p, grid, distgrid)
view.mat(res, "Result from distlenna")
opener.mat2pgm('report/distlenna_fix_p4.pgm', res)
view.show()
