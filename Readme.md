# Dashboard E-Commerce Brasil  

Dashboard ini dirancang untuk menganalisis data e-commerce Brasil berdasarkan beberapa aspek utama, seperti kategori produk, durasi pengiriman, segmentasi pelanggan, dan clustering. Tujuannya adalah memberikan wawasan mendalam untuk membantu pengambilan keputusan strategis.  

---

## Fitur Dashboard  

### 1. **Kategori Produk**  
- Menampilkan 5 kategori produk dengan jumlah penjualan tertinggi dan terendah.  
- Visualisasi berupa bar chart untuk mempermudah analisis pola penjualan.  

### 2. **Durasi Pengiriman**  
- Menampilkan distribusi durasi pengiriman dalam histogram.  
- Informasi pengiriman terlama termasuk ID pesanan dan lokasi asal serta tujuan pengiriman.  

### 3. **Segmentasi Pelanggan**  
- Menggunakan pendekatan RFM (Recency, Frequency, Monetary) untuk mengelompokkan pelanggan ke dalam segmen tertentu.  
- Menampilkan distribusi segmen pelanggan dalam bentuk bar chart.  

### 4. **Clustering**  
- Visualisasi hasil clustering pelanggan berdasarkan jumlah transaksi dan rata-rata durasi pengiriman.  
- Scatter plot dengan warna berbeda untuk setiap cluster.  

### 5. **Ringkasan Analisis**  
- Rangkuman temuan dari analisis yang dilakukan, meliputi kategori produk, durasi pengiriman, segmentasi pelanggan, dan clustering.  

---

## Cara Penggunaan  

### 1. **Persyaratan Sistem**  
- Python 3.7 atau lebih baru.  
- Pustaka yang dibutuhkan:  
  - `streamlit`  
  - `pandas`  
  - `numpy`  
  - `matplotlib`  
  - `seaborn`  
  - `gdown`  
  - **`setuptools`**  
  - **`wheel`**  

### 2. **Langkah-Langkah**  
1. Clone repositori ini atau unduh file zip-nya.  
2. Instal pustaka yang dibutuhkan dengan perintah:  
   ```bash  
   pip install -r requirements.txt  
   ```  
3. Jalankan aplikasi Streamlit dengan perintah:  
   ```bash  
   streamlit run dashboard.py  
   ```  

### 3. **Dataset**  
- Dataset diunduh secara otomatis dari Google Drive menggunakan pustaka `gdown`.  
- Pastikan koneksi internet aktif saat pertama kali menjalankan aplikasi untuk mengunduh dataset.  

---

## Struktur Direktori  

```plaintext  
.  
├── dashboard.py            # File utama aplikasi Streamlit  
├── requirements.txt        # Daftar pustaka yang dibutuhkan  
├── README.md               # Dokumentasi aplikasi  
```  

---

## Teknologi yang Digunakan  

- **Python**: Bahasa pemrograman utama.  
- **Streamlit**: Untuk membangun antarmuka dashboard.  
- **Matplotlib & Seaborn**: Untuk visualisasi data.  
- **Pandas & NumPy**: Untuk manipulasi data.  
- **gdown**: Untuk mengunduh dataset dari Google Drive.  
- **setuptools & wheel**: Untuk mendukung instalasi pustaka Python.  

---

## Dataset  

Dataset yang digunakan berisi data e-commerce Brasil dan diunduh dari Google Drive dengan ID file: `1KeLL573qhSjHyiC4X5gAeaQ8qiSsgjui`.  

---

## Catatan  

- Pastikan dataset memiliki struktur kolom yang sesuai dengan analisis dalam aplikasi.  
- Jika terjadi masalah saat mengunduh dataset, periksa ID file di dalam `dashboard.py`.  

---

## Kontribusi  

Kontribusi untuk meningkatkan dashboard ini dipersilakan! Silakan buka _pull request_ atau diskusikan ide Anda melalui _issue tracker_.  

---

## Lisensi  

Aplikasi ini dilisensikan di bawah [MIT License](LICENSE).  
