#Praktikum PCD 7 - Filter Rerata
#Import Library
import cv2 # Mengimpor modul cv2 dari OpenCV untuk pemrosesan citra
import numpy as np #mengimpor pustaka numpy ke dalam program python
from skimage import data, io# Mengimpor modul data dan io dari skimage untuk pemrosesan citra
import matplotlib.pyplot as plt# Mengimpor modul pyplot dari matplotlib untuk membuat plot
#%matplotlib inline

#Load & Plot Input Image
img1 = cv2.imread("ferari.jpg", cv2.IMREAD_GRAYSCALE) # Membaca citra "ferari.jpg" mode grayscale
img2 = cv2.imread("mobil.jpg", cv2.IMREAD_GRAYSCALE) # Membaca citra "mobil.jpg" mode grayscale

print('Shape citra 1 : ', img1.shape) #menampilkan bentuk shape
print('Shape citra 2 : ', img2.shape)#menampilkan bentuk shape

fig, axes = plt.subplots(1, 2, figsize=(10, 10))#subplot 2 kolom 1 baris
ax = axes.ravel()# mengubah aray menjadi satu dimensi

ax[0].imshow(img1, cmap = 'gray')#menghasilkan colormap gray pada sublot yang pertama
ax[0].set_title("Citra 1") #menampilkan citra 1
ax[1].imshow(img2, cmap = 'gray')#menghasilkan colormap gray pada sublot yang kedua
ax[1].set_title("Citra 2") #menampilkan tulisan citra 2

#Code Asal Matlab
#proses filter rerata untuk citra mobil
#F2 = double(inputMobil);
#for baris=2 : tinggiA-1
#    for kolom=2 : lebarA-1
#        jum = F2(baris-1, kolom-1)+ F2(baris-1, kolom) + F2(baris-1, kolom-1) + ...
#              F2(baris, kolom-1) + F2(baris, kolom) + F2(baris, kolom+1) + ...
#              F2(baris+1, kolom-1) + F2(baris+1, kolom) + F2(baris+1, kolom+1);         
#         outputMobil(baris, kolom) = uint8(1/9 * jum);
#    end
#end
#Menyiapkan variable output
copy_img1 = img1.copy().astype(float)#membuat salinan tipe datanya float
copy_img2 = img2.copy().astype(float)#membuat salinan tipe datanya float

m1,n1 = copy_img1.shape# dimensi citra 1
output1 = np.empty([m1, n1])#membuar aray kosong dimensinya sama denghan citra

m2,n2 = copy_img2.shape#dimensi citra2
output2 = np.empty([m2, n2])#membuat aray kosong dimensinya sama denghan citra
print('Shape copy citra 1 : ', copy_img1.shape)#menampilkan bentuk shape citra 1
print('Shape output citra 1 : ', output1.shape)#menampilkan bentuk shape citra 1

print('m1 : ',m1)#menampilkan m1
print('n1 : ',n1)#enampilkan n1
print() #menampilkan hasil

print('Shape copy citra 2 : ', copy_img2.shape)#menampilkan bentuk shape citra 2
print('Shape output citra 3 : ', output2.shape)#menampilkan bentuk shape citra 2
print('m2 : ',m2)#menampilkan m2
print('n2 : ',n2)#menampilkan n2
print() #menampilkan hasil
#Proses Filter Rerata Pada Citra Input 1
for baris in range(0, m1-1):#untuk baris range nya
    for kolom in range(0, n1-1):#untuk rsange kolom
        a1 = baris #untuk koordinar baris
        b1 = kolom#b1 koordinat kolom
        jumlah = copy_img1[a1-1, b1-1] + copy_img1[a1-1, b1] + copy_img1[a1-1, b1-1] + \
                 copy_img1[a1, b1-1] + copy_img1[a1, b1] + copy_img1[a1, b1+1] + \
                 copy_img1[a1+1, b1-1] + copy_img1[a1+1, b1] + copy_img1[a1+1, b1+1]
        output1[a1, b1] = (1/9 * jumlah)#koordinat dalam output 1 yang mengacu pada indeks koordinat dalam aray [a1,b1]

for baris1 in range(0, m2-1):#range untuk baris
    for kolom1 in range(0, n2-1):#range untuk kolom
        a1 = baris1 #koordinat a1 baris1
        b1 = kolom1 #koordinat kolom b1
        jumlah = copy_img2[a1-1, b1-1] + copy_img2[a1-1, b1] + copy_img2[a1-1, b1-1] + \
                 copy_img2[a1, b1-1] + copy_img2[a1, b1] + copy_img2[a1, b1+1] + \
                 copy_img2[a1+1, b1-1] + copy_img2[a1+1, b1] + copy_img2[a1+1, b1+1]
        output2[a1, b1] = (1/9 * jumlah)#koordinat dalam output 2yang mengacu pada indeks koordinat dalam aray [a1,b1]

fig, axes = plt.subplots(2, 2, figsize=(10, 10)) #subplot menjadi 2 baris 2 kolom   # Membuat subplots dengan 2 baris dan 2 kolom
ax = axes.ravel() #mengubah aray menjadi dimensi                               

ax[0].imshow(img1, cmap='gray') # Menampilkan citra 1 pada subplot pertama
ax[0].set_title("Input Citra 1")# Menetapkan judul pada subplot pertama

ax[1].imshow(img2, cmap='gray') # Menampilkan citra 2 pada subplot kedua
ax[1].set_title("Input Citra 2") # Menetapkan judul pada subplot kedua

ax[2].imshow(output1, cmap='gray')# Menampilkan output citra 1 pada subplot ketiga
ax[2].set_title("Output Citra 1") # Menetapkan judul pada subplot ketiga

ax[3].imshow(output2, cmap='gray') # Menampilkan output citra 2 pada subplot keempat
ax[3].set_title("Output Citra 2")# Menetapkan judul pada subplot keempat

fig.tight_layout()# Menyesuaikan tata letak subplot
plt.show()    # Menampilkan plot