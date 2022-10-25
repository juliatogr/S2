import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os

vidcap = cv2.VideoCapture('bbb_cut_high.mp4')
histogram_images = []
temp_hist_img = 'temp_figure.png'

success, img = vidcap.read()
while success:

    histogram, bin_edges = np.histogram(img)

    img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
    y, u, v = cv2.split(img_yuv)
    y_histogram, y_bin_edges = np.histogram(y)
    u_histogram, u_bin_edges = np.histogram(u)
    v_histogram, v_bin_edges = np.histogram(v)

    fig = plt.figure(figsize=(8, 6))
    plt.plot(y_histogram)
    plt.plot(u_histogram)
    plt.plot(v_histogram)
    fig.savefig(temp_hist_img)
    plt.close(fig)
    cv2.waitKey(0)
    image = Image.open(temp_hist_img)
    image = image.resize((200, 200))
    image.save(temp_hist_img)
    image = cv2.imread(temp_hist_img)

    for i in range(len(image)):
        for j in range(len(image[0])):
            img[i,j] = image[i,j]

    histogram_images.append(img)
    success, img = vidcap.read()

for file in os.listdir('./'):
    if file.endswith(temp_hist_img):
        os.remove(file)
# from image sequence to video

video_name = 'histograms.mp4'

height, width, layers = histogram_images[0].shape
cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
video = cv2.VideoWriter(video_name, 0, 1, (width, height))

for image in histogram_images:
    video.write(np.uint8(image))

video.release()
