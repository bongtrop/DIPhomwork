import numpy as np
import cal

def mat2hist(im):
  hist = np.zeros(256, dtype=np.uint32)
  for i in range(0,256):
      hist[i] = sum(sum(im==i))

  return hist

def hist2im(hist):
    hist[255] = 0
    m = np.max(hist)
    x = 255.0/m
    hist = hist * x

    im = np.zeros((256,512), dtype=np.uint8)
    for i in range(0, 512, 2):
      f = int(round(hist[i/2]))
      for j in range(255, 255-f, -1):
        im[j][i] = 255

    return im

def mat2bw(mat, V):
  bw = np.zeros(mat.shape, dtype=np.uint8)
  for v in V:
    bw[mat==v] = 255

  return bw

def moment(mat, p, q):
  mat = mat.astype(np.float64)
  if (np.max(mat)>1):
    mat = mat/255

  w = mat.shape[1]
  h = mat.shape[0]
  return np.sum(np.array([[(x**p)*(y**q)*mat[y][x] for x in range(0, w)] for y in range(0,h)]))

def central_moment(mat, p, q):
  mat = mat.astype(np.float64)
  if (np.max(mat)>1):
    mat = mat/255

  w = mat.shape[1]
  h = mat.shape[0]

  M00 = moment(mat, 0, 0)
  M10 = moment(mat, 1, 0)
  M01 = moment(mat, 0, 1)
  xc = M10/M00
  yc = M01/M00
  return np.sum(np.array([[((x-xc)**p)*((y-yc)**q)*mat[y][x] for x in range(0, w)] for y in range(0,h)]))

def norm_moment(mat, p, q):
  mat = mat.astype(np.float64)
  if (np.max(mat)>1):
    mat = mat/255

  Cpq = central_moment(mat, p, q)
  C00 = central_moment(mat, 0, 0)

  return Cpq/(C00**((p+q)/2+1))

def hist2cdf(hist):
  area = np.sum(hist)
  prop = 0
  i = 0
  cdf = np.zeros(hist.shape)

  for h in hist:
    prop = prop + (h*1.0/area)
    cdf[i] = prop
    i+=1

  return cdf

def histeq(mat):
  out = np.zeros(mat.shape, np.int32)
  hist = mat2hist(mat)
  cdf = hist2cdf(hist)
  f = np.round(cdf*255).astype(np.uint8)

  for i in range(0,256):
    out[mat==i] = f[i]

  return out

def lpo(mat, m, c):
  mat = mat*m + c

  return mat

def norm(mat):
  mat = mat.astype(np.float64)
  mat = ((mat-np.min(mat))/(np.max(mat)-np.min(mat)))*255
  return mat.astype(np.int32)

def convolute(F, G, origin, fill=0):
  G = np.fliplr(G)
  G = np.flipud(G)
  origin[0] = G.shape[0] - origin[0]
  origin[1] = G.shape[1] - origin[1]

  result = np.ones(F.shape, dtype=np.int32)*fill

  for i in range(origin[0], F.shape[0]-origin[0]):
    for j in range(origin[1], F.shape[1]-origin[1]):
      try:
        result[i][j] = np.sum(F[i-origin[0]:i-origin[0]+G.shape[0],j-origin[1]:j-origin[1]+G.shape[1]] * G)
      except:
        pass

  return result

def otsu(mat, bias):
  hist = mat2hist(mat)
  total = np.sum(hist)
  summ = 0
  for i in range (1,256):
    summ += i*hist[i]

  sumB = 0
  wB = 0
  WF = 0
  maxx = 0.0
  between = 0.0
  th1 = 0.0
  th2 = 0.0

  for i in range(0,256):
    wB+= hist[i]
    if wB==0:
      continue

    wF = total - wB
    if wF==0:
      break

    sumB += i*hist[i]
    mB = sumB/wB
    mF = (summ - sumB)/wF
    between = wB * wF * (mB-mF)**2
    if between>=maxx:
      th1 = i
      if between>maxx:
        th2=i

      maxx = between

  th = int((th1+th2)/2)+bias
  bw = mat2bw(mat, range(th,256))
  return bw


def localotsu(mat, nh, nw):
  res = np.zeros(mat.shape, np.int32)
  sh = mat.shape[0]/nh
  sw = mat.shape[1]/nw

  for i in range(0,nh):
    for j in range(0,sw):
      submat = mat[sh*i:sh*(i+1),sw*j:sw*(j+1)]
      res[sh*i:sh*(i+1),sw*j:sw*(j+1)] = otsu(submat,104)

  return res

def controlgrid(mat, grid, distgrid):
    res = np.zeros(mat.shape, dtype=np.int32)
    for i in range(0, 256):
        A = [[grid[i]["x1"]*1.0, grid[i]["y1"]*1.0, grid[i]["x1"]*grid[i]["y1"]*1.0, 1.],
             [grid[i]["x2"]*1.0, grid[i]["y2"]*1.0, grid[i]["x2"]*grid[i]["y2"]*1.0, 1.],
             [grid[i]["x3"]*1.0, grid[i]["y3"]*1.0, grid[i]["x3"]*grid[i]["y3"]*1.0, 1.],
             [grid[i]["x4"]*1.0, grid[i]["y4"]*1.0, grid[i]["x4"]*grid[i]["y4"]*1.0, 1.]]

        B = [distgrid[i]["x1"], distgrid[i]["x2"], distgrid[i]["x3"], distgrid[i]["x4"]]
        wx = cal.GEPP(np.array(A), np.array(B))

        B = [distgrid[i]["y1"], distgrid[i]["y2"], distgrid[i]["y3"], distgrid[i]["y4"]]
        wy = cal.GEPP(np.array(A), np.array(B))


        for j in range((i/16)*16, ((i/16)+1)*16):
            for k in range((i%16)*16, ((i%16)+1)*16):
                posx = wx[0]*k + wx[1]*j + wx[2] * j * k + wx[3]
                posy = wy[0]*k + wy[1]*j + wy[2] * j * k + wy[3]

                res[j][k] = cal.bilinear(mat, posy, posx)

    return res

def affine(mat, A, B, ori=[0,0], fill=0):
    nmat = np.zeros(mat.shape, dtype=np.uint8)
    for i in range(0, mat.shape[1]):
        for j in range(0, mat.shape[0]):
            pos = np.array([[i-ori[0]],[j-ori[1]]])
            npos = np.dot(A, pos) + B
            npos[0,0] = npos[0,0]+ori[0]
            npos[1,0] = npos[1,0]+ori[1]


            if npos[0,0]>=0 and npos[0,0]<mat.shape[0] and npos[1,0]>=0 and npos[1,0]<mat.shape[1]:
                nmat[i, j] = mat[int(npos[0, 0]), int(npos[1,0])]
            else:
                nmat[i, j] = fill

    return nmat

def resize(mat, wr, hr):
    nmat = np.zeros((mat.shape[1]*hr, mat.shape[0]*wr), dtype=np.uint8)
    for i in range(0, nmat.shape[1]):
        for j in range(0, nmat.shape[0]):
            nmat[i, j] = mat[round(i/hr), round(j/wr)]

    return nmat
