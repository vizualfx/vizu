import numpy as np
from sys import argv
from scipy.io.wavfile import read, write

path = argv[1]
fs, data = read(path)

data = data[:,0]

print("data: ", str(len(data)))
print(fs)