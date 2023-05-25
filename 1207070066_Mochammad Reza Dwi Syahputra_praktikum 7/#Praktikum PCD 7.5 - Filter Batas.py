#Praktikum PCD 7 - Filter Batas
#Import Library
import matplotlib.pyplot as plt# Mengimport modul matplotlib untuk membuat plot
import cv2 # Mengimport modul cv2 (OpenCV) untuk membaca citra
#%matplotlib inline
from skimage import data #import modul data dari skimage buat pemprosesan citra
from skimage.io import imread # import fungsi imread dari skimage lo agar membaca citra
from skimage.color import rgb2gray # mengonversi citra ke skala abu
import numpy as np #mengimpor pustaka numpy ke dalam program python
#Load & Plot Input Image
citra1 = cv2.imread("ferari.jpg", cv2.IMREAD_GRAYSCALE)    # Membaca citra 1 dalam mode skala abu-abu menggunakan cv2
citra2 = cv2.imread("mobil.jpg", cv2.IMREAD_GRAYSCALE)    # Membaca citra 2 dalam mode skala abu-abu menggunakan cv2

print('Shape citra 1 : ', citra1.shape)#menampilkan bentuk shape
print('Shape citra 1 : ', citra2.shape)#menampilkan bentuk shape

fig, axes = plt.subplots(1, 2, figsize=(10, 10))#subplots dengan 2 kolom satu baris
ax = axes.ravel() # merubah aray

ax[0].imshow(citra1, cmap = 'gray')#menampilkan colormapgray pada subplot pertama
ax[0].set_title("Citra 1") #menampilkan tulisan citra 1
ax[1].imshow(citra2, cmap = 'gray')#menampilkan colormapgray pada subplot kedua
ax[1].set_title("Citra 2")#menampilkan tulisan citra 2


#Code Asal Matlab
#for baris=2 : tinggi-1
#    for kolom=2 : lebar-1
#        minPiksel = min([F(baris-1, kolom-1) F(baris-1, kolom) F(baris, kolom+1) ...
#            F(baris, kolom-1) F(baris, kolom+1) F(baris+1, kolom-1)  ...
#            F(baris+1, kolom) F(baris+1, kolom+1)]);
#        
#        maksPiksel = max([F(baris-1, kolom-1) F(baris-1, kolom) F(baris, kolom+1)    ...
#            F(baris, kolom-1) F(baris, kolom+1) F(baris+1, kolom-1)  ...
#            F(baris+1, kolom) F(baris+1, kolom+1)]);    
#            
#        if F(baris, kolom) < minPiksel
#           G(baris, kolom) = minPiksel;
#        else
#            if F(baris, kolom) > maksPiksel
#                G(baris, kolom) = maksPiksel;
#            else
#                G(baris, kolom) = F(baris, kolom);
#            end
#        end    
#    end
#end
#Menyiapkan variable output
copyCitra1 = citra1.copy()#membuat salinan
copyCitra2 = citra2.copy()#membuat salinan

m1,n1 = copyCitra1.shape#memperoleh dimensi citra 1
output1 = np.empty([m1, n1])#membuat aray kosong dengan dimensi mengikuti citra 1

m2,n2 = copyCitra2.shape#mendapatkan dimensi citra
output2 = np.empty([m2, n2])#membuat aray kosong dengan dimensi mengikuti citra 2
print('Shape copy citra 1 : ', copyCitra1.shape)#memperoleh dimensi citra
print('Shape output citra 1 : ', output1.shape)#membuat aray kosong dengan dimensi mengikuti citra

print('m1 : ',m1)#mendapatkan dimensi
print('n1 : ',n1)#mendapatkan dimensi
print() #menampilkan hasil

print('Shape copy citra 2 : ', copyCitra2.shape)#shape copy
print('Shape output citra 3 : ', output2.shape)#shape copy
print('m2 : ',m2)# Menampilkan nilai m2
print('n2 : ',n2)# Menampilkan nilai m2
print() #menampilkan hasil

#Proses Filter Batas Pada Citra Input 1
for baris in range(0, m1-1): #range untuk baris
    for kolom in range(0, n1-1):#range untuk kolom
        
        a1 = baris#baris a1
        b1 = kolom#kolom b1
        
        arr = np.array([copyCitra1[a1-1, b1-1], copyCitra1[a1-1, b1], copyCitra1[a1, b1+1], \
            copyCitra1[a1, b1-1], copyCitra1[a1, b1+1], copyCitra1[a1+1, b1-1],  \
            copyCitra1[a1+1, b1], copyCitra1[a1+1, b1+1]])
        
        minPiksel = np.amin(arr);        
        maksPiksel = np.amax(arr);    
            
        if copyCitra1[baris, kolom] < minPiksel :
            output1[baris, kolom] = minPiksel
        else :
            if copyCitra1[baris, kolom] > maksPiksel :
                output1[baris, kolom] = maksPiksel
            else :
                output1[baris, kolom] = copyCitra1[baris, kolom] #koordinat dalam output 1 yang mengacu pada indeks koordinat dalam aray [a1,b1]
#Proses Filter Batas Pada Citra Input 2
for baris1 in range(0, m2-1):
    for kolom1 in range(0, n2-1):
        
        a1 = baris1
        b1 = kolom1
        
        arr = np.array([copyCitra2[a1-1, b1-1], copyCitra2[a1-1, b1], copyCitra2[a1, b1+1], \
            copyCitra2[a1, b1-1], copyCitra2[a1, b1+1], copyCitra2[a1+1, b1-1],  \
            copyCitra2[a1+1, b1], copyCitra2[a1+1, b1+1]])
        
        minPiksel = np.amin(arr);        
        maksPiksel = np.amax(arr);    
            
        if copyCitra2[baris1, kolom1] < minPiksel :
            output2[baris1, kolom1] = minPiksel
        else :
            if copyCitra2[baris1, kolom1] > maksPiksel :
                output2[baris1, kolom1] = maksPiksel
            else :
                output2[baris1, kolom1] = copyCitra2[baris1, kolom1] #koordinat dalam output 2 yang mengacu pada indeks koordinat dalam aray [a1,b1]
#Plot Citra Input dan Output Hasil dari Filter Batas
fig, axes = plt.subplots(2, 2, figsize=(10, 10))# Membuat subplots dengan 2 baris dan 2 kolom
ax = axes.ravel() # Mengubah array axes jadi satu dimensi

ax[0].imshow(citra1, cmap = 'gray')# Menampilkan output citra 1 pada subplot 1
ax[0].set_title("Input Citra 1") #menampilkan tulisan citra 1

ax[1].imshow(citra2, cmap = 'gray')# Menampilkan output citra 1 pada subplot 2
ax[1].set_title("Input Citra 2")#menampilkan tulisan input citra 2

ax[2].imshow(output1, cmap = 'gray')# Menampilkan output citra 1 pada subplot 3
ax[2].set_title("Output Citra 1")#menampilkan tulisan output citra 1

ax[3].imshow(output2, cmap = 'gray')# Menampilkan output citra 1 pada subplot 4
ax[3].set_title("Output Citra 2")#menampilkan tulisan output citra 2

fig.tight_layout()    # Mengatur tata letak subplot agar rapi
plt.show()    # Menampilkan plot
 