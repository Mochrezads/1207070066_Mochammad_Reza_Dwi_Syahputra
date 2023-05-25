import matplotlib.pyplot as plt# Mengimport modul matplotlib untuk membuat plot
# Mengimport library matplotlib.pyplot untuk membuat plot gambar.

#%matplotlib inline
# Komentar: Komentar ini mungkin seharusnya digunakan di lingkungan notebook untuk menampilkan plot secara langsung.

from skimage import data #import modul data dari skimage buat pemprosesan citra
from skimage.io import imread # import fungsi imread dari skimage lo agar membaca citra
from skimage.color import rgb2gray# mengonversi citra ke skala abu
import numpy as np# Mengimpor modul numpy untuk operasi numerik

import cv2 #inport cv2 dari OpenCV untuk pemrosesan citra
# Mengimport beberapa modul yang akan digunakan dalam kode. Modul skimage digunakan untuk memanipulasi gambar, sedangkan numpy dan cv2 digunakan untuk operasi pengolahan citra.

citra1 = cv2.imread("ferari.jpg", cv2.IMREAD_GRAYSCALE)
# Membaca gambar dengan nama file "riram.jpg" dan mengubahnya menjadi citra grayscale.

print(citra1.shape)
# Menampilkan dimensi citra dalam bentuk (tinggi, lebar).

plt.imshow(citra1, cmap='gray')#menampilkan colormapgray pada subplot pertama
# Menampilkan citra grayscale menggunakan imshow dengan colormap 'gray'.

kernel = np.array([[-1, 0, -1], #kernel
                   [0, 4, 0],
                   [-1, 0, -1]])
# Membuat kernel dengan matriks tertentu yang akan digunakan dalam operasi konvolusi.

citraOutput = cv2.filter2D(citra1, -1, kernel)
# Melakukan operasi konvolusi pada citra citra1 menggunakan kernel yang telah dibuat sebelumnya, dan hasilnya disimpan dalam variabel citraOutput.

fig, axes = plt.subplots(1, 2, figsize=(12, 12))# Membuat subplots 
ax = axes.ravel()# merubah aray

ax[0].imshow(citra1, cmap='gray')#menampilkan colormapgray pada subplot ke2
ax[0].set_title("Citra Input")#menampilkan judul
ax[1].imshow(citraOutput, cmap='gray')#menampilkan colormapgray pada subplot ke3
ax[1].set_title("Citra Output") #menapilkan judul

fig.tight_layout()# Mengatur tata letak plot agar lebih rapi.
plt.show()# Menampilkan plot ke layar.