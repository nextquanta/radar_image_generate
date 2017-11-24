import os
import numpy as np
from matplotlib import pyplot as plt
import cv2
import math
import csv


ofile=open("data.csv","wb")
writer = csv.writer(ofile, delimiter=",")

NUM_SAMPLE_PER_CHIRP=256
Fs=10*(10**6)
Ts= 1.0/float(Fs)
f=(4*10**5)
NUM_CHIRPS_PER_FRAME=256


t=np.linspace(0,NUM_SAMPLE_PER_CHIRP*Ts,NUM_SAMPLE_PER_CHIRP)
y=256*(0.5+0.5*np.sin(2*np.pi*f*t))
#y=[[0,item,0] for item in y]


M=np.zeros((NUM_CHIRPS_PER_FRAME,NUM_SAMPLE_PER_CHIRP),np.uint8)

for i in range(NUM_CHIRPS_PER_FRAME):
    M[i]=y

#plt.plot(t,M[0])
#plt.show()

x=cv2.imread(r'C:\Users\B49032\Desktop\personal_document\chopta\risi\IMG_20160308_114032940_HDR.jpg')
cv2.imwrite('image.jpg',M)
#cv2.waitKey()

for row in M:
    writer.writerow(row)
ofile.close()


#cv2.imshow('image',M)
