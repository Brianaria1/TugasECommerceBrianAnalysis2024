import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests  # Untuk mengunduh dataset dari Dropbox
import os  # Untuk memeriksa file yang sudah diunduh

@st.cache_data
def load_data(uploaded_file=None):
    try:
        csv_file = "processed_order_data.csv.gz"  # Nama file GZIP lokal
        dropbox_url = "https://www.dropbox.com/scl/fi/tkzrpbbtgh4yqvu6dnu9c/processed_order_data.csv.gz?rlkey=0zjd9jgvv41fgku8tipbn8m33&st=90an6u6k&dl=1"
        
        # Jika file di-upload, gunakan file tersebut
        if uploaded_file:
            st.info("Dataset diupload secara manual.")
            data = pd.read_csv(uploaded_file, compression='gzip')
            return data
        
        # Periksa apakah file GZIP sudah ada di lokal
        if not os.path.exists(csv_file):
            st.info("Mengunduh dataset dari Dropbox...")
            with requests.get(dropbox_url, stream=True) as r:
                r.raise_for_status()
                with open(csv_file, "wb") as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        f.write(chunk)

        # Membaca file CSV terkompresi
        st.info("Memuat dataset...")
        data = pd.read_csv(csv_file, compression='gzip')
        return data
    
    except Exception as e:
        st.error(f"Gagal memuat dataset: {e}")
        return pd.DataFrame()  # Return DataFrame kosong


# Memuat dataset
st.title("Dashboard E-Commerce Brasil")
st.write("Dashboard ini memberikan wawasan dari data e-commerce Brasil berdasarkan hasil analisis.")

uploaded_file = st.file_uploader("Upload dataset (GZIP format):", type=["gz"])
data = load_data(uploaded_file)

if data.empty:
    st.warning("Dataset belum dimuat. Harap periksa file atau koneksi Anda.")
else:
    # Tab navigasi
    tab1, tab2, tab3, tab4, tab5 = st.tabs(
        ["Kategori Produk", "Durasi Pengiriman", "Segmentasi Pelanggan", "Clustering", "Ringkasan"]
    )

    # 1. Kategori Produk
    with tab1:
        st.header("Identifikasi 5 Kategori Produk dengan Penjualan Tertinggi dan Terendah")
        st.write("Menampilkan kategori produk dengan jumlah penjualan tertinggi dan terendah.")
        
        product_sales = data.groupby("product_category_name")["price"].count().sort_values(ascending=False)
        top_5_categories = product_sales.head(5)
        bottom_5_categories = product_sales.tail(5)

        st.subheader("5 Kategori Produk dengan Penjualan Tertinggi")
        st.write(top_5_categories)
        
        st.subheader("5 Kategori Produk dengan Penjualan Terendah")
        st.write(bottom_5_categories)
        
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.barplot(x=top_5_categories.index, y=top_5_categories.values, ax=ax, color="green", label="Tertinggi")
        sns.barplot(x=bottom_5_categories.index, y=bottom_5_categories.values, ax=ax, color="red", label="Terendah")
        plt.title("Kategori Produk dengan Penjualan Tertinggi dan Terendah")
        plt.xticks(rotation=45)
        plt.legend()
        st.pyplot(fig)

    # 2. Durasi Pengiriman
    with tab2:
        st.header("Analisis Durasi Pengiriman")
        data["delivery_duration"] = pd.to_datetime(data["order_delivered_customer_date"]) - pd.to_datetime(data["order_purchase_timestamp"])
        data["delivery_duration"] = data["delivery_duration"].dt.days
        
        st.write("Rata-rata Durasi Pengiriman:", data["delivery_duration"].mean())
        
        longest_delivery = data.loc[data["delivery_duration"].idxmax()]
        st.subheader("Pengiriman Terlama")
        st.write(longest_delivery[["order_id", "delivery_duration"]])

        plt.figure(figsize=(8, 4))
        sns.histplot(data["delivery_duration"], bins=30, kde=True, color="green")
        plt.title("Distribusi Durasi Pengiriman")
        plt.xlabel("Durasi Pengiriman (hari)")
        st.pyplot(plt)

    # 3. Segmentasi Pelanggan
    with tab3:
        st.header("Segmentasi Pelanggan Berdasarkan RFM")
        data["recency"] = (pd.Timestamp.now() - pd.to_datetime(data["order_purchase_timestamp"])).dt.days
        frequency = data.groupby("customer_id").size()
        monetary = data.groupby("customer_id")["price"].sum()
        rfm = pd.DataFrame({"frequency": frequency, "monetary": monetary}).reset_index()

        st.write("Contoh Segmentasi RFM:")
        st.dataframe(rfm.head(10))

    # 4. Clustering
    with tab4:
        st.header("Clustering Pelanggan")
        transaction_count = data.groupby("customer_id")["order_id"].count().reset_index()
        avg_delivery_duration = data.groupby("customer_id")["delivery_duration"].mean().reset_index()
        merged_data = pd.merge(transaction_count, avg_delivery_duration, on="customer_id")
        st.write("Contoh Data Clustering:")
        st.dataframe(merged_data.head())

    # 5. Ringkasan
    with tab5:
        st.header("Ringkasan Analisis")
        st.write("""
        - **Kategori Produk:** Menampilkan kategori produk dengan penjualan tertinggi dan terendah.
        - **Durasi Pengiriman:** Sebagian besar pengiriman dilakukan dalam waktu singkat.
        - **Segmentasi Pelanggan:** Mengelompokkan pelanggan berdasarkan metrik RFM.
        - **Clustering:** Membagi pelanggan berdasarkan transaksi dan durasi pengiriman.
        """)

# Footer
st.sidebar.title("Informasi")
st.sidebar.info("Dashboard ini mendukung upload dataset manual (format GZIP) atau unduhan otomatis dari Dropbox.")
