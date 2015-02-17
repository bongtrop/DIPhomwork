import numpy as np
import matplotlib.pyplot as plt

def mat2hist(im):
    hist = np.zeros(256, dtype=np.uint32)
    for i in range(0,256):
        hist[i] = sum(sum(im==i))

    return hist

def plothist(hist):
    plt.hist(hist)
    plt.ylabel('Frequency')
    plt.xlabel('Gray Level')
    plt.show()
