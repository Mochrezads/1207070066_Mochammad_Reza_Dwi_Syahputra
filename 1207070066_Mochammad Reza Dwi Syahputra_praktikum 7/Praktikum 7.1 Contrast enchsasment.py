#Praktikum 7.1 - Contrast Enhancment
#Untuk melakukan perbaikan contrast pada suatu citra terdapat beberapa metode, diantaranya :

#Import Library
import numpy as np # Mengimpor modul numpy untuk operasi numerik
import matplotlib.pyplot as plt # Mengimpor modul pyplot dari matplotlib untuk visualisasi
#%matplotlib inline# Komentar ini mungkin merujuk pada pengaturan output plot dalam lingkungan spesifik
import cv2 # Mengimpor modul cv2 dari OpenCV untuk pemrosesan citra
import matplotlib.image as mpimg # Mengimpor modul mpimg dari matplotlib untuk membaca citra
from skimage import data # Mengimpor modul data dari skimage untuk citra contoh

image = cv2.imread("ferari.jpg", cv2.IMREAD_GRAYSCALE)  # Membaca citra "ferari.jpg" dalam mode grayscale
image_equalized = cv2.equalizeHist(image) # Melakukan equalisasi histogram pada citra
clahe = cv2.createCLAHE(clipLimit=2, tileGridSize=(8,8)) # Membuat objek CLAHE dengan parameter tertentu

# Terapkan CLAHE pada citra asli
image_clahe = clahe.apply(image_equalized)
#Penerapan metode Contrast Stretching (CS)
# Create an empty array to store the final output
image_cs = np.zeros((image.shape[0],image.shape[1]),dtype = 'uint8')#membuat aray multidimensi dengan ukuran row column dengan nilai 0

# Apply Min-Max Contrasting
min = np.min(image) #apply minimum
max = np.max(image)#apply maximum

for i in range(image.shape[0]):#perulangan yang digunakan untuk 
    for j in range(image.shape[1]):
        image_cs[i,j] = 255*(image[i,j]-min)/(max-min)
#Penerapan Metode Perkalian Konstanta
copyCamera = image.copy().astype(float)

m1,n1 = copyCamera.shape
output1 = np.empty([m1, n1])

for baris in range(0, m1-1):
    for kolom in range(0, n1-1):
        a1 = baris#baris a1
        b1 = kolom#kolomb1
        output1[a1, b1] = copyCamera[baris, kolom] * 1.9
#Plot Image
fig, axes = plt.subplots(5, 2, figsize=(20, 20))
ax = axes.ravel()

ax[0].imshow(image, cmap=plt.cm.gray)#menghasilkan colormap gray pada sublot yang pertama
ax[0].set_title("Citra Input")#menampilkan tulisan citra input
ax[1].hist(image.ravel(), bins=256)
ax[1].set_title('Histogram Input')#menampilkan title histogram input

ax[2].imshow(image_equalized, cmap=plt.cm.gray)#menghasilkan colormap gray pada sublot yang 2
ax[2].set_title("Citra Output HE") #menampilkan tulisan citra output
ax[3].hist(image_equalized.ravel(), bins=256)
ax[3].set_title('Histogram Output HE Method')#menampilkan title histogram output HE Menthod

ax[4].imshow(image_cs, cmap=plt.cm.gray)#menghasilkan colormap gray pada sublot yang 3
ax[4].set_title("Citra Output CS")#menampilkan tulisan citra output cs
ax[5].hist(image_cs.ravel(), bins=256)
ax[5].set_title('Histogram Output CS Method')#menampilkan tulisan histogram output cs method

ax[6].imshow(image_clahe, cmap=plt.cm.gray)#menghasilkan colormap gray pada sublot yang 4
ax[6].set_title("Citra Grayscale CLAHE") #menampilkan tulisan Citra Gray scale clame
ax[7].hist(image_clahe.ravel(), bins=256)
ax[7].set_title('Histogram Output CLAHE Method')#menampilkan tulisan Histogram output clame method

ax[8].imshow(output1, cmap=plt.cm.gray) #menghasilkan colormap gray pada sublot yang 5
ax[8].set_title("Citra Grayscale Perkalian Konstanta")#menampilkan tulisan citra grayslcale perkalian konstanta
ax[9].hist(output1.ravel(), bins=256)
ax[9].set_title('Histogram Output Perkalian Konstanta Method')#menampilkan hasil title histogram

fig.tight_layout()# Menyesuaikan tata letak subplot agar rapi
plt.show() # Menampilkan plot
 