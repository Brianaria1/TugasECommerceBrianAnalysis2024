import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Fungsi untuk memuat data dari file unggahan
@st.cache_data
def load_data(uploaded_file):
    try:
        # Membaca file CSV langsung dari file uploader (format GZIP)
        order_data_clean = pd.read_csv(uploaded_file, compression='gzip')
        return order_data_clean
    except Exception as e:
        st.error(f"Gagal memuat dataset: {e}")
        return pd.DataFrame()

# Judul aplikasi
st.title("Dashboard E-Commerce Brasil")
st.write("Dashboard ini memberikan wawasan dari data e-commerce Brasil berdasarkan hasil analisis.")

# File uploader untuk dataset
uploaded_file = st.file_uploader("Unggah file dataset (GZIP format)", type=["csv", "gz"])

if uploaded_file is not None:
    # Memuat dataset jika file diunggah
    data = load_data(uploaded_file)
    st.success("Dataset berhasil dimuat!")

    # Tab navigasi untuk analisis
    tab1, tab2, tab3, tab4, tab5 = st.tabs(
        ["Kategori Produk", "Durasi Pengiriman", "Segmentasi Pelanggan", "Clustering", "Ringkasan"]
    )

    # 1. Kategori Produk
    with tab1:
        st.header("Identifikasi 5 Kategori Produk dengan Penjualan Tertinggi dan Terendah")
        st.write("Menampilkan kategori produk dengan jumlah penjualan tertinggi dan terendah.")

        # Analisis kategori produk
        product_sales = data.groupby("product_category_name").size().sort_values(ascending=False)
        top_5_categories = product_sales.head(5)
        bottom_5_categories = product_sales.tail(5)

        st.subheader("5 Kategori Produk dengan Penjualan Tertinggi")
        st.write(top_5_categories)

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

        data['delivery_duration'] = (pd.to_datetime(data['order_delivered_customer_date']) -
                                     pd.to_datetime(data['order_purchase_timestamp'])).dt.days

        avg_delivery = data['delivery_duration'].mean()
        st.write(f"Rata-rata durasi pengiriman: {avg_delivery:.2f} hari")

        longest_delivery = data.loc[data['delivery_duration'].idxmax()]
        st.write(f"Pengiriman Terlama: {longest_delivery['delivery_duration']} hari")
        st.write(f"Koordinat: ({longest_delivery['geolocation_lat']}, {longest_delivery['geolocation_lng']})")

        # Visualisasi
        plt.figure(figsize=(10, 6))
        sns.histplot(data['delivery_duration'], bins=30, kde=True, color="green")
        plt.title("Distribusi Durasi Pengiriman")
        plt.xlabel("Durasi Pengiriman (Hari)")
        plt.ylabel("Frekuensi")
        st.pyplot(plt)

    # 3. Segmentasi Pelanggan
    with tab3:
        st.header("Segmentasi Pelanggan")
        st.write("Menampilkan segmentasi pelanggan berdasarkan RFM (Recency, Frequency, Monetary).")

        # Menghitung Recency, Frequency, dan Monetary
        recency = (pd.to_datetime("today") - pd.to_datetime(data.groupby('customer_id')['order_purchase_timestamp'].max())).dt.days
        frequency = data.groupby('customer_id').size()
        monetary = data.groupby('customer_id')['price'].sum()

        rfm = pd.DataFrame({'Recency': recency, 'Frequency': frequency, 'Monetary': monetary})

        # Visualisasi distribusi segmen
        st.write(rfm.head())
        sns.scatterplot(x='Frequency', y='Monetary', hue='Recency', data=rfm, palette='viridis')
        plt.title("Segmentasi Pelanggan Berdasarkan RFM")
        plt.xlabel("Frequency")
        plt.ylabel("Monetary")
        st.pyplot(plt)

    # 4. Clustering
    with tab4:
        st.header("Clustering Pelanggan")
        st.write("Visualisasi clustering berdasarkan jumlah transaksi dan rata-rata durasi pengiriman.")

        # Clustering sederhana (manual)
        cluster_conditions = [
            (data['delivery_duration'] < 10) & (data['price'] > 500),
            (data['delivery_duration'] >= 10) & (data['price'] <= 500)
        ]
        cluster_labels = ['Cepat & Mahal', 'Lambat & Murah']
        data['cluster'] = pd.cut(data['price'], bins=[0, 500, float('inf')], labels=cluster_labels)

        # Visualisasi clustering
        sns.scatterplot(x='delivery_duration', y='price', hue='cluster', data=data, palette='Set2')
        plt.title("Clustering Pelanggan")
        plt.xlabel("Durasi Pengiriman (Hari)")
        plt.ylabel("Harga")
        st.pyplot(plt)

    # 5. Ringkasan
    with tab5:
        st.header("Ringkasan Analisis")
        st.write("""
        - **Kategori Produk:** Menampilkan kategori produk dengan penjualan tertinggi dan terendah.
        - **Durasi Pengiriman:** Sebagian besar pengiriman selesai dalam waktu rata-rata 11 hari.
        - **Segmentasi Pelanggan:** Visualisasi data RFM untuk memahami pelanggan.
        - **Clustering:** Mengelompokkan pelanggan berdasarkan pola pengiriman dan harga.
        """)

else:
    st.warning("Silakan unggah file dataset terlebih dahulu untuk melanjutkan.")
