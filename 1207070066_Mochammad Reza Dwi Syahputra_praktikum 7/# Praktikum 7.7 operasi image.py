# memanggil modul yang diperlukan
import cv2#inport cv2 dari OpenCV untuk pemrosesan citra
import numpy as np# Mengimpor modul numpy untuk operasi numerik
from matplotlib import pyplot as plt# Mengimpor modul pyplot dari matplotlib untuk membuat plot

img = cv2.imread("ferari.jpg") # Membaca gambar dengan nama file "riram.jpg" menggunakan OpenCV, yang menghasilkan citra dengan format BGR.

ferari = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # Mengubah format citra dari BGR menjadi RGB menggunakan fungsi cv2.cvtColor.

plt.imshow(ferari)
plt.title("Gambar Awal")#menampilkan judul
plt.axis("off")
plt.show() # Menampilkan plot ke layar.
# Menampilkan gambar awal (citra RGB) tanpa filter menggunakan plt.imshow, dengan judul "Gambar Awal" dan sumbu (axis) yang tidak ditampilkan.

kernel = np.ones((5,5),np.float32)/25
print(kernel)
# Membuat filter dengan matriks berukuran 5x5 yang berisi nilai 1 dan kemudian membaginya dengan 25. Nilai filter ini akan digunakan dalam operasi filtering.

ferari_filter = cv2.filter2D(img,-1,kernel)
# Melakukan operasi filtering pada citra asli (img) menggunakan filter yang telah dibuat sebelumnya (kernel), dan hasilnya disimpan dalam variabel riram_filter.

plt.imshow(ferari_filter)
plt.title("Gambar Setelah Filtering")#menampilkan judul
plt.axis("off")
plt.show()# Menampilkan plot ke layar.
# Menampilkan citra setelah proses filtering menggunakan plt.imshow, dengan judul "Gambar Setelah Filtering" dan sumbu (axis) yang tidak ditampilkan.

data = np.random.normal(size=1000)

plt.rcParams["figure.figsize"] = (15,15)
# Mengatur ukuran plot menjadi 15x15 jika diperlukan, agar tampilan lebih besar.

plt.subplot(221)
plt.hist(data, bins=30)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram')#memberikan judul histogram

plt.subplot(222), plt.imshow(ferari)
plt.title('Original')#menampilkan judul
plt.xticks([]), plt.yticks([])

plt.subplot(223), plt.imshow(ferari_filter)
plt.title('Averaging')#menampilkan judul
plt.xticks([]), plt.yticks([])

plt.subplot(224)
hist_data = ferari_filter.flatten()
plt.hist(hist_data, bins=30)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram Setelah Filtering')#menampilkan judul

plt.suptitle('Gambar dan Histogram') #menampilkan judul
plt.show()# Menampilkan plot ke layar.

ferari_blur = cv2.blur(img,(5,5))
plt.imshow(ferari_blur) # Menampilkan plot ke layar.
# Melakukan operasi blurring pada citra asli (img) menggunakan cv2.blur dengan kernel berukuran 5x5, dan hasilnya disimpan dalam variabel riram_blur. Kemudian menampilkan hasil blurring menggunakan plt.imshow.

kernel = np.matrix([
          [1, 1, 1],
          [1, 2, 1],
          [1, 1, 1]
          ])/25
print(kernel)
# Membuat kernel dengan menggunakan np.matrix dengan matriks berukuran 3x3 yang memiliki pola tertentu, dan kemudian membaginya dengan 25. Nilai kernel ini akan digunakan dalam operasi filtering.

ferari_filter = cv2.filter2D(img,-1,kernel)

plt.imshow(ferari_filter)
plt.show() # Menampilkan plot ke layar.
# Melakukan operasi filtering pada citra asli (img) menggunakan kernel yang telah dibuat sebelumnya (kernel), dan hasilnya disimpan dalam variabel riram_filter. Kemudian menampilkan hasil filtering menggunakan plt.imshow dan plt.show()


# Highpass Filter

img = cv2.imread("ferari.jpg", 0)  # Membaca citra dengan nama file "riram.jpg" dalam format grayscale menggunakan OpenCV, dengan memberikan argumen 0 kepada fungsi `cv2.imread`.

laplacian = cv2.Laplacian(img, cv2.CV_64F)  # Menerapkan algoritma high-pass filtering menggunakan operator Laplacian pada citra grayscale (`img`). Hasilnya disimpan dalam variabel `laplacian`.

sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)
# Menerapkan algoritma high-pass filtering menggunakan operator Sobel pada citra grayscale (`img`). Operator Sobel digunakan untuk mendeteksi tepi vertikal (dalam `sobelx`) dan tepi horizontal (dalam `sobely`) pada citra. Kedua hasilnya disimpan dalam variabel `sobelx` dan `sobely`.

plt.rcParams["figure.figsize"] = (20, 20)  # Mengatur ukuran plot menjadi 20x20 untuk tampilan yang lebih besar.

plt.subplot(2, 2, 1), plt.imshow(img, cmap='gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])#menampilkan judul
plt.subplot(2, 2, 2), plt.imshow(laplacian, cmap='gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])#menampilkan judul
plt.subplot(2, 2, 3), plt.imshow(sobelx, cmap='gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])#menampilkan judul
plt.subplot(2, 2, 4), plt.imshow(sobely, cmap='gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])#menampilkan judul

plt.figure(figsize=(10, 5))
plt.subplot(121)
hist_data = img.flatten()
plt.hist(hist_data, bins=30)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram (Original)')#menampilkan judul

plt.subplot(122)
hist_data = laplacian.flatten()
plt.hist(hist_data, bins=30)
plt.xlabel('Value') #label value
plt.ylabel('Frequency') #label frekuensi
plt.title('Histogram (Laplacian)')#menampilkan judul

plt.show() # Menampilkan plot ke layar.


img = cv2.imread("ferari.jpg", 0) # Membaca citra dengan nama file "riram.jpg" dalam format grayscale menggunakan OpenCV, dengan memberikan argumen 0 kepada fungsi `cv2.imread`.

# memanggil fungsi Canny Edges dengan argument (citra, nilai_min, nilai_max)
edges = cv2.Canny(img, 100, 200)

plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])#menampilkan judul
plt.subplot(122), plt.imshow(edges, cmap='gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])#menampilkan judul
plt.show() # Menampilkan plot ke layar.
# Menampilkan citra asli dan citra hasil deteksi tepi menggunakan `plt.subplot`. Citra asli ditampilkan pada subplot pertama dengan judul "Original Image", sedangkan citra hasil deteksi tepi ditampilkan pada subplot kedua dengan judul "Edge Image". Sumbu x dan y tidak ditampilkan.


img = cv2.imread("ferari.jpg",0) # Membaca citra dengan nama file "riram.jpg" dalam format grayscale menggunakan OpenCV, dengan memberikan argumen 0 kepada fungsi `cv2.imread`.

ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
# Melakukan thresholding pada citra grayscale (`img`) dengan nilai threshold 127. Hasilnya disimpan dalam variabel `thresh1`, `thresh2`, `thresh3`, `thresh4`, dan `thresh5` sesuai dengan jenis thresholding yang digunakan.

titles = ['Gambar asli','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
# Menyimpan judul dan citra hasil thresholding dalam bentuk list untuk keperluan plotting.

for i in range(6):
    plt.subplot(3,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show() # Menampilkan plot ke layar.
# Menampilkan citra-citra hasil thresholding dalam satu plot menggunakan `plt.subplot`. Citra asli ditampilkan pada subplot pertama, sedangkan citra hasil thresholding ditampilkan pada subplot-subplot berikutnya sesuai dengan urutan yang telah ditentukan. Setiap subplot diberi judul dan sumbu x dan y tidak ditampilkan.

img = cv2.medianBlur(img,5) # Menggunakan median blur pada citra grayscale (`img`) dengan ukuran kernel 5. Hal ini dilakukan untuk menghaluskan tepi objek pada citra sebelum melakukan thresholding.

# Lakukan Thresholding
# Binary Threshold
ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
# Melakukan thresholding binary menggunakan fungsi threshold dari OpenCV dengan nilai threshold 127.

# Adaptive Threshold dengan Mean
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
# Melakukan thresholding adaptif dengan metode mean menggunakan fungsi adaptiveThreshold dari OpenCV. Menggunakan ukuran blok 11x11 dan konstanta C sebesar 2.

# Adaptive Threshold dengan Gaussian
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
# Melakukan thresholding adaptif dengan metode Gaussian menggunakan fungsi adaptiveThreshold dari OpenCV. Menggunakan ukuran blok 11x11 dan konstanta C sebesar 2.

# Plotting
titles = ['Original Image', 'Global Thresholding (v = 127)', 'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, th1, th2, th3]
# Membuat list judul 'titles' yang akan digunakan untuk memberikan judul pada setiap gambar yang akan ditampilkan. Membuat list 'images' yang berisi citra asli dan hasil thresholding.

# menampilkan hasil
for i in range(4):
    plt.subplot(2, 2, i + 1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
# Melakukan iterasi untuk menampilkan gambar-gambar secara berurutan. Mengatur tata letak subplot dengan 2 baris dan 2 kolom. Menampilkan gambar pada subplot yang sesuai, memberikan judul menggunakan 'titles', dan menghilangkan label sumbu x dan y.

plt.tight_layout()
plt.show() # Menampilkan plot ke layar.
# Mengatur tata letak subplot agar lebih rapi dan menampilkan plot.

# Membuat histogram dari gambar asli
plt.subplot(2, 2, 1)
plt.hist(img.ravel(), 256, [0, 256])
plt.title('Histogram Gambar asli')#menampilkan judul
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')#frekuenmsi

# Membuat histogram dari gambar setelah di filter
for i in range(1, 4):
    plt.subplot(2, 2, i + 1)
    plt.hist(images[i].ravel(), 256, [0, 256])
    plt.title('Histogram ' + titles[i])#menampilkan judul
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')#frekuensi

plt.tight_layout() #agar plot rapih
plt.show()# Menampilkan plot ke layar.

# membaca gambar baymax 
img = cv2.imread('baymax.jpg',0)

# Hitungan threshold. 
# Perhatikan nilai ambang batas bawah dan atas dari tiap fungsi 
# yang diberikan
ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

# menampilkan hasil
titles = ['Gambar asli','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

# menampilkan beberapa gambar sekaligus
for i in range(6):
    # 3 baris, 2 kolom
    plt.subplot(3,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])#menampilkan judul
    plt.xticks([]),plt.yticks([])
plt.show()# Menampilkan plot ke layar.

# masih menggunakan variabel img yang sama
#img = cv2.imread('images/baymax.jpg',0)

# digunakan median blur untuk menghaluskan tepi objek pada citra
# ini diperlukan agar thresholding memberikan hasil lebih baik
img = cv2.medianBlur(img,5)

# Lakukan Thresholding
# Binary Threshold
ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

# Adaptive Threshold dengan Mean
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY,11,2)

# Adaptive Threshold dengan Gaussian
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)


# Plotting
titles = ['Original Image', 'Global Thresholding (v = 127)',
            'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, th1, th2, th3]

# menampilkan hasil
for i in range(4):
    plt.subplot(2,2,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])#menampilkan judul
    plt.xticks([]),plt.yticks([])
plt.show()# Menampilkan plot ke layar.