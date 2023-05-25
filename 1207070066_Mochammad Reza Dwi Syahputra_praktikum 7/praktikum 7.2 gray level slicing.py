import cv2 #untuk menggunakan library open cv
import numpy as np #mengimpor pustaka numpy ke dalam program python
from skimage import data
import matplotlib.pyplot as plt# Mengimpor modul pyplot dari matplotlib untuk visualisasi
#%matplotlib inline
img = data.camera() #mengambil gambar dari koleksi gambar bawaaan yang disebut camera
img = cv2.imread("ferari.jpg", cv2.IMREAD_GRAYSCALE)  # Membaca citra "ferari.jpg" dalam mode grayscale
row, column = img.shape

img1 = np.zeros((row,column),dtype = 'uint8') #membuat aray multidimensi dengan ukuran row column dengan nilai 0
 

min_range = 10 #range minimal di set 10
max_range = 60 #range max disetel 60
 

for i in range(row):
    for j in range(column):
        if img[i,j]>min_range and img[i,j]<max_range:
            img1[i,j] = 255
        else: #jika
            img1[i,j] = 0
fig, axes = plt.subplots(2, 2, figsize=(12, 12))
ax = axes.ravel() #mengubah aray menjadi dimensi  

ax[0].imshow(img, cmap=plt.cm.gray)#menghasilkan colormap gray pada sublot yang pertama
ax[0].set_title("Citra Input") #menampilkan tulisan citra input
ax[1].hist(img.ravel(), bins=256)
ax[1].set_title('Histogram Input')#menampilkan tulisan histogram input

ax[2].imshow(img1, cmap=plt.cm.gray)#menghasilkan colormap gray pada sublot yang ke2
ax[2].set_title("Citra Output") #menampilkan tulisan citra output
ax[3].hist(img1.ravel(), bins=256)
ax[3].set_title('Histogram Output')#menampilkan tulisan Histogram output
fig.tight_layout()  # Menyesuaikan tata letak subplot agar rapi
plt.show()  # Menampilkan plot