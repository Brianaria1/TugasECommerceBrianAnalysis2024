import os
import gdown
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Fungsi untuk memuat data dari Google Drive
@st.cache_data(persist="disk")
def load_data():
    # ID file dari Google Drive
    file_id = "1KeLL573qhSjHyiC4X5gAeaQ8qiSsgjui"  # File ID dari link saya
    url = f"https://drive.google.com/uc?id={file_id}"  # URL untuk unduh file
    output = "order_data_clean.csv"  # Nama file lokal setelah diunduh
    
    # Jika file belum ada, unduh dari Google Drive
    if not os.path.exists(output):
        gdown.download(url, output, quiet=False)
    
    # Membaca file CSV
    return pd.read_csv(output)

# Memuat dataset
st.title("Dashboard E-Commerce Brasil")
st.write("Dashboard ini memberikan wawasan dari data e-commerce Brasil berdasarkan hasil analisis.")

data = load_data()

# Tab navigasi
tab1, tab2, tab3, tab4, tab5 = st.tabs(
    ["Kategori Produk", "Durasi Pengiriman", "Segmentasi Pelanggan", "Clustering", "Ringkasan"]
)

# 1. Kategori Produk
with tab1:
    st.header("Identifikasi 5 Kategori Produk dengan Penjualan Tertinggi dan Terendah")
    st.write("Menampilkan kategori produk dengan jumlah penjualan tertinggi dan terendah.")
    
    # Menghitung total penjualan per kategori
    product_sales = data.groupby("product_category")["sales"].sum().sort_values(ascending=False)
    
    # Menampilkan 5 kategori produk dengan penjualan tertinggi
    top_5_categories = product_sales.head(5)
    st.subheader("5 Kategori Produk dengan Penjualan Tertinggi")
    st.write(top_5_categories)
    
    # Menampilkan 5 kategori produk dengan penjualan terendah
    bottom_5_categories = product_sales.tail(5)
    st.subheader("5 Kategori Produk dengan Penjualan Terendah")
    st.write(bottom_5_categories)
    
    # Visualisasi
    fig, ax = plt.subplots(figsize=(10, 6))
    
    sns.barplot(x=top_5_categories.index, y=top_5_categories.values, ax=ax, color="green", label="Tertinggi")
    sns.barplot(x=bottom_5_categories.index, y=bottom_5_categories.values, ax=ax, color="red", label="Terendah")
    
    plt.title("Kategori Produk dengan Penjualan Tertinggi dan Terendah")
    plt.xlabel("Kategori Produk")
    plt.ylabel("Jumlah Penjualan")
    plt.xticks(rotation=45)
    plt.legend()
    st.pyplot(fig)

# 2. Durasi Pengiriman
with tab2:
    st.header("Analisis Durasi Pengiriman")
    st.write("Menampilkan distribusi durasi pengiriman dan pengiriman terlama.")
    
    # Plot distribusi durasi pengiriman
    plt.figure(figsize=(8, 4))
    sns.histplot(data["delivery_time"], bins=30, kde=True, color="green")
    plt.title("Distribusi Durasi Pengiriman")
    plt.xlabel("Durasi Pengiriman (hari)")
    plt.ylabel("Frekuensi")
    st.pyplot(plt)

    # Informasi pengiriman terlama
    longest_delivery = data.loc[data["delivery_time"].idxmax()]
    st.subheader("Pengiriman Terlama")
    st.write(f"Durasi Pengiriman: {longest_delivery['delivery_time']} hari")
    st.write(f"ID Pesanan: {longest_delivery['order_id']}")
    st.map(pd.DataFrame({"lat": [longest_delivery["geolocation_lat"]], 
                         "lon": [longest_delivery["geolocation_lng"]]}))

# 3. Segmentasi Pelanggan
with tab3:
    st.header("Segmentasi Pelanggan")
    st.write("Menampilkan segmentasi pelanggan berdasarkan RFM (Recency, Frequency, Monetary).")
    
    sample_rfm = data[["customer_id", "recency", "frequency", "monetary", "segment"]].head(10)
    st.dataframe(sample_rfm)

    segment_count = data["segment"].value_counts()
    fig, ax = plt.subplots()
    segment_count.plot(kind="bar", color="skyblue", ax=ax)
    plt.title("Distribusi Segmentasi Pelanggan")
    plt.xlabel("Segment")
    plt.ylabel("Jumlah Pelanggan")
    st.pyplot(fig)

# 4. Clustering
with tab4:
    st.header("Clustering Pelanggan")
    st.write("Visualisasi clustering berdasarkan jumlah transaksi dan rata-rata durasi pengiriman.")
    
    plt.figure(figsize=(10, 6))
    sns.scatterplot(
        x=data["transaction_count"],
        y=data["avg_delivery_time"],
        hue=data["cluster"],
        palette="Set2",
        alpha=0.7
    )
    plt.title("Clustering Pelanggan Berdasarkan Transaksi dan Durasi Pengiriman")
    plt.xlabel("Jumlah Transaksi")
    plt.ylabel("Rata-rata Durasi Pengiriman (hari)")
    st.pyplot(plt)

# 5. Ringkasan
with tab5:
    st.header("Ringkasan Analisis")
    st.write("""
    - **Kategori Produk:** Menampilkan kategori produk dengan penjualan tertinggi dan terendah untuk melihat pola dalam penjualan produk.
    - **Durasi Pengiriman:** Sebagian besar pengiriman dilakukan dalam waktu singkat, namun terdapat pengiriman dengan durasi yang sangat lama.
    - **Segmentasi Pelanggan:** Pelanggan diklasifikasikan ke dalam segmen berdasarkan perilaku pembelian (RFM).
    - **Clustering:** Pelanggan dikelompokkan menjadi 3 cluster: transaksi besar-durasi cepat, transaksi sedang-durasi rata-rata, dan transaksi kecil-durasi lama.
    """)

# Footer
st.sidebar.title("Informasi")
st.sidebar.info("Dashboard inimport os
import gdown
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Fungsi untuk memuat data dari Google Drive
@st.cache_data(persist="disk")
def load_data():
    # ID file dari Google Drive
    file_id = "1KeLL573qhSjHyiC4X5gAeaQ8qiSsgjui"  # File ID dari link saya
    url = f"https://drive.google.com/uc?id={file_id}"  # URL untuk unduh file
    output = "order_data_clean.csv"  # Nama file lokal setelah diunduh
    
    # Jika file belum ada, unduh dari Google Drive
    if not os.path.exists(output):
        gdown.download(url, output, quiet=False)
    
    # Membaca file CSV
    return pd.read_csv(output)

# Memuat dataset
st.title("Dashboard E-Commerce Brasil")
st.write("Dashboard ini memberikan wawasan dari data e-commerce Brasil berdasarkan hasil analisis.")

data = load_data()

# Tab navigasi
tab1, tab2, tab3, tab4, tab5 = st.tabs(
    ["Kategori Produk", "Durasi Pengiriman", "Segmentasi Pelanggan", "Clustering", "Ringkasan"]
)

# 1. Kategori Produk
with tab1:
    st.header("Identifikasi 5 Kategori Produk dengan Penjualan Tertinggi dan Terendah")
    st.write("Menampilkan kategori produk dengan jumlah penjualan tertinggi dan terendah.")
    
    # Menghitung total penjualan per kategori
    product_sales = data.groupby("product_category")["sales"].sum().sort_values(ascending=False)
    
    # Menampilkan 5 kategori produk dengan penjualan tertinggi
    top_5_categories = product_sales.head(5)
    st.subheader("5 Kategori Produk dengan Penjualan Tertinggi")
    st.write(top_5_categories)
    
    # Menampilkan 5 kategori produk dengan penjualan terendah
    bottom_5_categories = product_sales.tail(5)
    st.subheader("5 Kategori Produk dengan Penjualan Terendah")
    st.write(bottom_5_categories)
    
    # Visualisasi
    fig, ax = plt.subplots(figsize=(10, 6))
    
    sns.barplot(x=top_5_categories.index, y=top_5_categories.values, ax=ax, color="green", label="Tertinggi")
    sns.barplot(x=bottom_5_categories.index, y=bottom_5_categories.values, ax=ax, color="red", label="Terendah")
    
    plt.title("Kategori Produk dengan Penjualan Tertinggi dan Terendah")
    plt.xlabel("Kategori Produk")
    plt.ylabel("Jumlah Penjualan")
    plt.xticks(rotation=45)
    plt.legend()
    st.pyplot(fig)

# 2. Durasi Pengiriman
with tab2:
    st.header("Analisis Durasi Pengiriman")
    st.write("Menampilkan distribusi durasi pengiriman dan pengiriman terlama.")
    
    # Plot distribusi durasi pengiriman
    plt.figure(figsize=(8, 4))
    sns.histplot(data["delivery_time"], bins=30, kde=True, color="green")
    plt.title("Distribusi Durasi Pengiriman")
    plt.xlabel("Durasi Pengiriman (hari)")
    plt.ylabel("Frekuensi")
    st.pyplot(plt)

    # Informasi pengiriman terlama
    longest_delivery = data.loc[data["delivery_time"].idxmax()]
    st.subheader("Pengiriman Terlama")
    st.write(f"Durasi Pengiriman: {longest_delivery['delivery_time']} hari")
    st.write(f"ID Pesanan: {longest_delivery['order_id']}")
    st.map(pd.DataFrame({"lat": [longest_delivery["geolocation_lat"]], 
                         "lon": [longest_delivery["geolocation_lng"]]}))

# 3. Segmentasi Pelanggan
with tab3:
    st.header("Segmentasi Pelanggan")
    st.write("Menampilkan segmentasi pelanggan berdasarkan RFM (Recency, Frequency, Monetary).")
    
    sample_rfm = data[["customer_id", "recency", "frequency", "monetary", "segment"]].head(10)
    st.dataframe(sample_rfm)

    segment_count = data["segment"].value_counts()
    fig, ax = plt.subplots()
    segment_count.plot(kind="bar", color="skyblue", ax=ax)
    plt.title("Distribusi Segmentasi Pelanggan")
    plt.xlabel("Segment")
    plt.ylabel("Jumlah Pelanggan")
    st.pyplot(fig)

# 4. Clustering
with tab4:
    st.header("Clustering Pelanggan")
    st.write("Visualisasi clustering berdasarkan jumlah transaksi dan rata-rata durasi pengiriman.")
    
    plt.figure(figsize=(10, 6))
    sns.scatterplot(
        x=data["transaction_count"],
        y=data["avg_delivery_time"],
        hue=data["cluster"],
        palette="Set2",
        alpha=0.7
    )
    plt.title("Clustering Pelanggan Berdasarkan Transaksi dan Durasi Pengiriman")
    plt.xlabel("Jumlah Transaksi")
    plt.ylabel("Rata-rata Durasi Pengiriman (hari)")
    st.pyplot(plt)

# 5. Ringkasan
with tab5:
    st.header("Ringkasan Analisis")
    st.write("""
    - **Kategori Produk:** Menampilkan kategori produk dengan penjualan tertinggi dan terendah untuk melihat pola dalam penjualan produk.
    - **Durasi Pengiriman:** Sebagian besar pengiriman dilakukan dalam waktu singkat, namun terdapat pengiriman dengan durasi yang sangat lama.
    - **Segmentasi Pelanggan:** Pelanggan diklasifikasikan ke dalam segmen berdasarkan perilaku pembelian (RFM).
    - **Clustering:** Pelanggan dikelompokkan menjadi 3 cluster: transaksi besar-durasi cepat, transaksi sedang-durasi rata-rata, dan transaksi kecil-durasi lama.
    """)

# Footer
st.sidebar.title("Informasi")
st.sidebar.info("Dashboard ini dikembangkan untuk menganalisis data e-commerce Brasil.")
i dikembangkan untuk menganalisis data e-commerce Brasil.")
