#Praktikum PCD 7 - Filter Median
#Import Library
import matplotlib.pyplot as plt # Mengimpor modul pyplot dari matplotlib untuk membuat plot
import cv2   # Mengimpor modul cv2 dari OpenCV untuk pemrosesan citra
#%matplotlib inline   # Komentar ini tidak digunakan dalam kode dan dapat diabaikan



from skimage import data #import modul data dari skimage buat pemprosesan citra
from skimage.io import imread # import fungsi imread dari skimage lo agar membaca citra
from skimage.color import rgb2gray # mengonversi citra ke skala abu
import numpy as np #mengimpor pustaka numpy ke dalam program python
#Load & Plot Input Image
citra1 = cv2.imread("ferari.jpg", cv2.IMREAD_GRAYSCALE)  # Membaca citra "riram.jpg" dalam mode grayscale
citra2 = cv2.imread("mobil.jpg", cv2.IMREAD_GRAYSCALE)   # Membaca citra "uin.png" dalam mode grayscale

print('Shape citra 1 : ', citra1.shape)#menampilkan bentuk shape
print('Shape citra 1 : ', citra2.shape)#menampilkan bentuk shape

fig, axes = plt.subplots(1, 2, figsize=(10, 10)) #subplots dengan 2 kolom satu baris
ax = axes.ravel() # merubah aray

ax[0].imshow(citra1, cmap = 'gray') #menampilkan colormapgray pada subplot pertama
ax[0].set_title("Citra 1") #menampilkan judul
ax[1].imshow(citra2, cmap = 'gray')#menampilkan citra 2 dengan colormap gray pada subplot kedua
ax[1].set_title("Citra 2") #menampilkan judul

#Code Asal Matlab
#%proses filter median untuk citra mobil
#for baris=2 : tinggiA-1
#    for kolom=2 : lebarA-1
#        dataA = [inputMobil(baris-1, kolom-1) inputMobil(baris-1, kolom) inputMobil(baris-1, kolom+1)  ...
#              inputMobil(baris, kolom-1) inputMobil(baris, kolom) inputMobil(baris, kolom+1)  ...
#              inputMobil(baris+1, kolom-1) inputMobil(baris+1, kolom) inputMobil(baris+1, kolom+1)];
#        % Urutkan
#        for i=1 : 8
#            for j=i+1 : 9
#                if dataA(i) > dataA(j)
#                    tmpA = dataA(i);
#                    dataA(i) = dataA(j);
#                    dataA(j) = tmpA;
#                end
#            end
#        end      
#        % Ambil nilai median
#        outputMobil(baris, kolom) = dataA(5);
#    end
#end
#Menyiapkan variable output
copyCitra1 = citra1.copy() #membuat salinan
copyCitra2 = citra2.copy()#membuat salinan

m1,n1 = copyCitra1.shape #memperoleh dimensi citra 1
output1 = np.empty([m1, n1])#membuat aray kosong dengan dimensi mengikuti citra 1

m2,n2 = copyCitra2.shape #mendapatkan dimensi citra
output2 = np.empty([m2, n2]) #membuat aray kosong dengan dimensisama kayak citra 2
print('Shape copy citra 1 : ', copyCitra1.shape)#memperoleh dimensi citra
print('Shape output citra 1 : ', output1.shape)#membuat aray kosong dengan dimensi mengikuti citra

print('m1 : ',m1)#mendapatkan dimensi
print('n1 : ',n1)#mendapatkan dimensi
print() #menampilkan hasil

print('Shape copy citra 2 : ', copyCitra2.shape)#shape copy
print('Shape output citra 3 : ', output2.shape)#shape output
print('m2 : ',m2)# Menampilkan nilai m2
print('n2 : ',n2)# Menampilkan nilai m2
print()#menampilkan hasil

#Proses Filter Median Pada Citra Input 1
for baris in range(0, m1-1):
    for kolom in range(0, n1-1):
        a1 = baris #baris
        b1 = kolom #kolom
        dataA = [copyCitra1[a1-1, b1-1], copyCitra1[a1-1, b1], copyCitra1[a1-1, b1+1], \
              copyCitra1[a1, b1-1], copyCitra1[a1, b1], copyCitra1[a1, b1+1], \
              copyCitra1[a1+1, b1-1], copyCitra1[a1+1, b1], copyCitra1[a1+1, b1+1]]
        
        # Urutkan
        for i in range(1, 8):
            for j in range(i, 9):
                if dataA[i] > dataA[j]:
                    tmpA = dataA[i];
                    dataA[i] = dataA[j];
                    dataA[j]= tmpA;
        
        output1[a1, b1] = dataA[5] #koordinat dalam output 1 yang mengacu pada indeks koordinat dalam aray [a1,b1]

#Proses Filter Median Pada Citra Input 2
for baris in range(0, m2-1):
    for kolom in range(0, n2-1):
        a1 = baris #baris
        b1 = kolom #kolom
        dataA = [copyCitra2[a1-1, b1-1], copyCitra2[a1-1, b1], copyCitra2[a1-1, b1+1], \
              copyCitra2[a1, b1-1], copyCitra2[a1, b1], copyCitra2[a1, b1+1], \
              copyCitra2[a1+1, b1-1], copyCitra2[a1+1, b1], copyCitra2[a1+1, b1+1]]
        
        # Urutkan
        for i in range(1, 8):
            for j in range(i, 9):
                if dataA[i] > dataA[j]:
                    tmpA = dataA[i];
                    dataA[i] = dataA[j];
                    dataA[j]= tmpA;
        
        output2[a1, b1] = dataA[5] #koordinat dalam output 2 yang mengacu pada indeks koordinat dalam aray [a1,b1]

#Plot Citra Input dan Output Hasil dari Filter Rerata
fig, axes = plt.subplots(2, 2, figsize=(10, 10))# Membuat subplots dengan 2 baris dan 2 kolom
ax = axes.ravel()# Mengubah array axes jadi satu dimensi

ax[0].imshow(citra1, cmap = 'gray') # Menampilkan output citra 1 pada subplot 1
ax[0].set_title("Input Citra 1") #menampilkan tulisan input citra 1

ax[1].imshow(citra2, cmap = 'gray') # Menampilkan output citra 1 pada subplot 2
ax[1].set_title("Input Citra 1") #menampilkan tulisan input citra 1

ax[2].imshow(output1, cmap = 'gray') # Menampilkan output citra 1 pada subplot ketiga
ax[2].set_title("Output Citra 1") #menampilkan tulisan output citra 1

ax[3].imshow(output2, cmap = 'gray') # Menampilkan output citra 1 pada subplot ke4
ax[3].set_title("Output Citra 2") #menampilkan tulisan output citra 1

fig.tight_layout() # Menyusun subplot secara rapi
plt.show()# Menampilkan plot