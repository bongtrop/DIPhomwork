import numpy as np
import math

# Gaussian Elimination Partial Pivoting
# Input GEPP(Ax = b)
def GEPP(A, b):
    n =  len(A)
    if b.size != n:
        raise ValueError("Invalid argument: incompatible sizes between A & b.", b.size, n)
    for k in xrange(n-1):
        maxindex = abs(A[k:,k]).argmax() + k
        if A[maxindex, k] == 0:
            raise ValueError("Matrix is singular.")
        if maxindex != k:
            A[[k,maxindex]] = A[[maxindex, k]]
            b[[k,maxindex]] = b[[maxindex, k]]
        for row in xrange(k+1, n):
            multiplier = A[row][k]/A[k][k]
            A[row][k] = multiplier
            for col in xrange(k + 1, n):
                A[row][col] = A[row][col] - multiplier*A[k][col]
            b[row] = b[row] - multiplier*b[k]
    #print A
    #print b
    x = np.zeros(n)
    k = n-1
    x[k] = b[k]/A[k,k]
    while k >= 0:
        x[k] = (b[k] - np.dot(A[k,k+1:],x[k+1:]))/A[k,k]
        k = k-1
    return x

# Bilinear Interpolate
# Input bilinear(Matrix Image, Position y, Position x)
def bilinear(mat, posy, posx):
    if posx>mat.shape[1]-1 or posy>mat.shape[0]-1:
        return mat[math.floor(posy)][math.floor(posx)]

    f00 = mat[math.floor(posy),math.floor(posx)]
    f01 = mat[math.floor(posy),math.ceil(posx)]
    f10 = mat[math.ceil(posy),math.floor(posx)]
    f11 = mat[math.ceil(posy),math.ceil(posx)]

    a = f01 - f00
    b = f10 - f00
    c = f11 + f00 - f01 - f10
    d = f00

    posx = posx-math.floor(posx)
    posy = posy-math.floor(posy)

    return a*posx + b*posy + c*posx*posy + d
