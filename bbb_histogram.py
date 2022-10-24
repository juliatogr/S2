import cv2
import numpy as np
import matplotlib.pyplot as plt

vidcap = cv2.VideoCapture('bbb.mp4')
histograms = []
success,img = vidcap.read()
count = 0
while success:

    histogram, bin_edges = np.histogram(img)

    cv2.imshow('Color input image', img)
    plt.plot(bin_edges[0:-1], histogram)  # <- or her
    plt.show()
    cv2.waitKey(0)
    histograms.append(histogram)
    success,image = vidcap.read()
    print('Read a new frame: ', success)
    count += 1

height, width, layers = histograms[0].shape
size = (width, height)
out = cv2.VideoWriter('project.avi', cv2.VideoWriter_fourcc(*'DIVX'), 15, size)

for i in range(len(histograms)):
    out.write(histograms[i])
out.release()
