# Dashboard E-Commerce Brasil

Dashboard ini dirancang untuk menganalisis data e-commerce Brasil berdasarkan beberapa aspek utama, seperti kategori produk, durasi pengiriman, segmentasi pelanggan, dan clustering. Tujuannya adalah memberikan wawasan mendalam untuk membantu pengambilan keputusan strategis.

## Fitur Dashboard

### 1. **Kategori Produk**
- Menampilkan 5 kategori produk dengan jumlah penjualan tertinggi dan terendah.
- Visualisasi berupa bar chart untuk mempermudah analisis pola penjualan.

### 2. **Durasi Pengiriman**
- Menampilkan distribusi durasi pengiriman dalam histogram.
- Informasi pengiriman terlama termasuk ID pesanan dan lokasi asal-pengiriman.

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

1. **Persyaratan Sistem:**
   - Python 3.7 atau lebih baru.
   - Pustaka yang dibutuhkan: `streamlit`, `pandas`, `matplotlib`, `seaborn`, `gdown`.

2. **Langkah-Langkah:**
   - Clone repositori ini atau unduh file zip-nya.
   - Instal pustaka yang dibutuhkan dengan perintah:
     ```bash
     pip install -r requirements.txt
     ```
   - Jalankan aplikasi Streamlit dengan perintah:
     ```bash
     streamlit run app.py
     ```

3. **Dataset:**
   - Dataset diunduh secara otomatis dari Google Drive menggunakan pustaka `gdown`.
   - Pastikan koneksi internet aktif saat menjalankan aplikasi untuk pertama kali.

---

## Struktur Direktori

```plaintext
.
├── app.py               # File utama aplikasi Streamlit
├── requirements.txt     # Daftar pustaka yang dibutuhkan
├── README.md            # Dokumentasi aplikasi
```

---

## Teknologi yang Digunakan

- **Python**: Bahasa pemrograman utama.
- **Streamlit**: Untuk membangun antarmuka dashboard.
- **Matplotlib & Seaborn**: Untuk visualisasi data.
- **Pandas**: Untuk manipulasi data.
- **gdown**: Untuk mengunduh dataset dari Google Drive.

---

## Dataset

Dataset yang digunakan berisi data e-commerce Brasil dan diunduh dari Google Drive dengan ID file: `1KeLL573qhSjHyiC4X5gAeaQ8qiSsgjui`.

---

## Catatan

- Pastikan dataset memiliki struktur kolom yang sesuai dengan analisis dalam aplikasi.
- Jika terdapat masalah dengan file dataset, pastikan ID file di `app.py` sudah benar.

---

## Kontribusi

Kontribusi untuk meningkatkan dashboard ini dipersilakan! Silakan buka _pull request_ atau diskusikan ide Anda melalui _issue tracker_.

---

## Lisensi

Aplikasi ini dilisensikan di bawah [MIT License](LICENSE).
