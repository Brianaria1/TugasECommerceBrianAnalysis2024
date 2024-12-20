# **Dashboard Analisis E-Commerce Brasil**

Dashboard ini dirancang untuk menganalisis data e-commerce Brasil berdasarkan beberapa aspek utama, seperti kategori produk, tren penjualan, dan distribusi tipe pembayaran. Tujuannya adalah memberikan wawasan mendalam terkait produk yang terjual dengan baik dan pola pembayaran yang digunakan oleh pelanggan, untuk mendukung pengambilan keputusan strategis.

---

## **Fitur Dashboard**

### 1.1 **Kategori Produk**
- Menampilkan kategori produk dengan penjualan tertinggi dan terendah.
- Visualisasi berupa bar chart untuk mempermudah analisis pola penjualan.

### 1.2 **Tren Penjualan**
- Menampilkan tren penjualan selama beberapa tahun terakhir menggunakan garis waktu.
- Visualisasi untuk memahami perubahan penjualan dari tahun ke tahun.

### 2.1 **Distribusi Tipe Pembayaran**
- Menampilkan distribusi berbagai tipe pembayaran yang digunakan oleh pelanggan.
- Bar chart untuk memudahkan pemahaman tipe pembayaran yang paling sering digunakan.

### 2.2 **Tipe Pembayaran Paling Populer**
- Menampilkan tipe pembayaran yang paling sering digunakan oleh pelanggan.

---

## **Fitur Filter Tanggal**
- **Interaktivitas Baru:** Pengguna harus memilih **tanggal awal** dan **tanggal akhir** secara lengkap untuk menghindari error. Jika hanya satu tanggal yang dipilih, dashboard akan memberikan pesan error dan meminta pengguna untuk menyelesaikan input rentang tanggal.
- Rentang tanggal dapat dipilih menggunakan antarmuka **date_input** di Streamlit.
- Data pada dashboard akan disesuaikan dengan periode yang dipilih, mencakup analisis kategori produk, tren penjualan, dan distribusi tipe pembayaran.

---

## **Cara Penggunaan**

### 1. **Persyaratan Sistem**
- **Python 3.10 atau lebih baru**
- Pustaka yang dibutuhkan:
  - `streamlit==1.24.0`
  - `pandas==1.5.3`
  - `matplotlib==3.7.1`
  - `seaborn==0.11.2`
  - `numpy==1.24.0`

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
- Siapkan dataset Anda dalam format CSV yang memiliki kolom berikut:
  - `order_id`
  - `customer_id`
  - `order_status`
  - `order_purchase_timestamp`
  - `product_category_name`
  - `price`
  - `payment_type`
- Unggah file `main_data.csv` untuk dianalisis dalam dashboard.

---

## **Struktur Direktori**

```plaintext
.
├── dashboard.py            # File utama aplikasi Streamlit
├── requirements.txt        # Daftar pustaka yang dibutuhkan
├── README.md               # Dokumentasi aplikasi
```

---

## **Teknologi yang Digunakan**

- **Python 3.10**: Bahasa pemrograman utama yang mendukung semua pustaka terbaru.
- **Streamlit**: Untuk membangun antarmuka dashboard.
- **Matplotlib & Seaborn**: Untuk visualisasi data.
- **Pandas & NumPy**: Untuk manipulasi data.

---

## **Fitur Tambahan**

1. **Interaksi Tanggal yang Lebih Stabil**:
   - Jika pengguna hanya memilih satu tanggal (awal atau akhir), aplikasi akan memberikan pesan error.
   - Hal ini memastikan pengguna memilih rentang tanggal yang lengkap sebelum data difilter.

2. **Visualisasi yang Lebih Informatif**:
   - Menambahkan bar chart untuk **10 kategori produk dengan penjualan tertinggi** dan **10 kategori produk dengan penjualan terendah**.
   - Menyediakan ringkasan tren penjualan berdasarkan tahun.

---

## **Catatan**

- Pastikan dataset Anda memiliki struktur kolom yang sesuai dengan analisis yang dilakukan dalam aplikasi.
- Dataset Anda harus memiliki data yang mencakup rentang tanggal yang ingin dianalisis.
- Jika Anda mengalami kesulitan dalam mengunggah file CSV atau menemukan masalah teknis lainnya, pastikan format data sesuai dengan yang dijelaskan pada bagian *Dataset*.

---

## **Kontribusi**

Kontribusi untuk meningkatkan dashboard ini sangat diterima! Silakan buka _pull request_ atau diskusikan ide Anda melalui _issue tracker_.

---

## **Lisensi**

Aplikasi ini dilisensikan di bawah [MIT License](LICENSE).  
