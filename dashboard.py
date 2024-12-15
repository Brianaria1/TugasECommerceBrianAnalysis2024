import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests  # Untuk mengunduh dataset dari Dropbox
import zipfile  # Untuk mengekstrak file ZIP
import os  # Untuk memeriksa file yang sudah diunduh

@st.cache_data
def load_data():
    try:
        # URL Dropbox
        url = "https://www.dropbox.com/scl/fi/pdmdf8mhp399cjww3bqd2/order_data_clean.zip?rlkey=8yvp5undp57m4xtqz2x4v7jzy&st=ivvqzjvc&dl=1"
        zip_file = "order_data_clean.zip"  
        csv_file = "order_data_clean.csv"

        # Periksa apakah file CSV sudah ada
        if not os.path.exists(csv_file):
            st.info("Mengunduh dataset...")
            with requests.get(url, stream=True) as r:
                r.raise_for_status()
                with open(zip_file, "wb") as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        f.write(chunk)

            # Ekstrak file ZIP
            with zipfile.ZipFile(zip_file, "r") as z:
                z.extractall()

        # Membaca file CSV
        order_data_clean = pd.read_csv(csv_file)
        return order_data_clean
    
    except Exception as e:
        st.error(f"Gagal memuat dataset: {e}")
        return pd.DataFrame()  # Return DataFrame kosong


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
    
    # Plot Kategori Produk dengan Penjualan Tertinggi
    sns.barplot(x=top_5_categories.index, y=top_5_categories.values, ax=ax, color="green", label="Tertinggi")
    
    # Plot Kategori Produk dengan Penjualan Terendah
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
    
    # Tabel contoh segmentasi
    sample_rfm = data[["customer_id", "recency", "frequency", "monetary", "segment"]].head(10)
    st.dataframe(sample_rfm)

    # Visualisasi segmentasi
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
    
    # Scatter plot clustering
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
