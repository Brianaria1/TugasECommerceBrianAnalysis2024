import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Judul aplikasi Streamlit
st.title('Analisis E-Commerce: Penjualan Produk dan Pembayaran')

# Fungsi untuk memuat data setelah upload
@st.cache
def load_data(uploaded_file):
    # Memuat data dari CSV
    main_data = pd.read_csv(uploaded_file, parse_dates=["order_purchase_timestamp"])
    return main_data

# Upload file CSV
uploaded_file = st.file_uploader("Upload file CSV", type=["csv"])

if uploaded_file is not None:
    # Memuat data
    main_data = load_data(uploaded_file)
    
    # Menampilkan data beberapa baris pertama
    st.write(main_data.head())

    # --- Analisis 1: Kategori Produk dengan Penjualan Tertinggi dan Terendah ---
    
    # 1.1: Penjualan berdasarkan kategori produk
    category_sales = main_data.groupby('product_category_name')['price'].sum().sort_values(ascending=False)
    
    # Menampilkan kategori produk dengan penjualan tertinggi dan terendah
    st.subheader("Penjualan Produk berdasarkan Kategori")
    st.write(category_sales)

    # Visualisasi Penjualan Kategori Produk
    st.subheader("Visualisasi Penjualan Kategori Produk")
    plt.figure(figsize=(10, 6))
    sns.barplot(x=category_sales.index, y=category_sales.values)
    plt.xticks(rotation=90)
    plt.xlabel('Kategori Produk')
    plt.ylabel('Penjualan (Total Harga)')
    plt.title('Penjualan Berdasarkan Kategori Produk')
    st.pyplot()

    # 1.2: Tren Penjualan Produk berdasarkan Tahun
    main_data['year'] = main_data['order_purchase_timestamp'].dt.year
    yearly_sales = main_data.groupby('year')['price'].sum()
    
    st.subheader("Tren Penjualan Produk per Tahun")
    st.write(yearly_sales)

    # Visualisasi Tren Penjualan Produk per Tahun
    st.subheader("Visualisasi Tren Penjualan Produk per Tahun")
    plt.figure(figsize=(10, 6))
    sns.lineplot(x=yearly_sales.index, y=yearly_sales.values)
    plt.xlabel('Tahun')
    plt.ylabel('Total Penjualan (Harga)')
    plt.title('Tren Penjualan Produk per Tahun')
    st.pyplot()

    # --- Analisis 2: Distribusi Tipe Pembayaran pada Pesanan ---
    
    # 2.1: Distribusi tipe pembayaran
    payment_type_dist = main_data['payment_type'].value_counts()
    
    st.subheader("Distribusi Tipe Pembayaran")
    st.write(payment_type_dist)

    # Visualisasi Distribusi Tipe Pembayaran
    st.subheader("Visualisasi Distribusi Tipe Pembayaran")
    plt.figure(figsize=(10, 6))
    sns.barplot(x=payment_type_dist.index, y=payment_type_dist.values)
    plt.xlabel('Tipe Pembayaran')
    plt.ylabel('Jumlah Pesanan')
    plt.title('Distribusi Tipe Pembayaran')
    st.pyplot()

    # 2.2: Tipe Pembayaran yang Paling Sering Digunakan
    most_common_payment_type = payment_type_dist.idxmax()
    st.subheader(f"Tipe Pembayaran yang Paling Sering Digunakan: {most_common_payment_type}")
