import numpy as np

# PGM File to Matrix
# Input pgm2mat(Filename)
def pgm2mat(filename):
    f = open(filename, "rb")

    # Read Detail
    i = 0
    detail = []
    while i<3:
        line = f.readline()
        line = line.replace("\n","").replace("\r","")
        if line[0]=='#':
            continue

        detail.append(line)
        i+=1

    # Read Image
    [w, h] = detail[1].split(' ')
    h = int(h)
    w = int(w)
    mat = np.zeros((h,w), dtype=np.int32)

    byte = f.read(1)

    for i in range(0,h):
        for j in range(0,w):
            mat[i][j] = ord(byte)
            byte = f.read(1)

    f.close()
    return mat

# Matrix to PGM File
# Input mat2pgm(Filename, Matrix)
def mat2pgm(filename, mat, pgmtype="P5", level="255"):
    mat[mat>255] = 255
    mat[mat<0] = 0
    f = open(filename, "wb")
    w = mat.shape[1]
    h = mat.shape[0]

    # Write Detial
    f.write(pgmtype+"\n")
    f.write(str(w)+" "+str(h)+"\n")
    f.write(level+"\n")

    # Write Image
    for i in range(0,h):
        for j in range(0,w):
            f.write(chr(mat[i][j]))


    f.close()
