import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Judul aplikasi Streamlit
st.title('Analisis E-Commerce: Penjualan Produk dan Pembayaran')

# Fungsi untuk memuat data dari URL Dropbox
def load_data_from_dropbox():
    url = "https://www.dropbox.com/scl/fi/x70t1awzkxtrkztjps55n/main_data.csv?rlkey=owlw5huxhfn484maqjfnl4ssz&st=pjp7vk4j&dl=1"
    main_data = pd.read_csv(url, parse_dates=["order_purchase_timestamp"])
    return main_data

# Memuat data dari Dropbox
main_data = load_data_from_dropbox()

# Pastikan kolom tanggal sudah dalam format datetime
main_data['order_purchase_timestamp'] = pd.to_datetime(main_data['order_purchase_timestamp'], errors='coerce')

# Menampilkan data beberapa baris pertama
st.write(main_data.head())

# Fitur interaktif: Filter berdasarkan rentang tanggal
st.subheader("Filter Data berdasarkan Rentang Tanggal")
min_date = main_data['order_purchase_timestamp'].min()
max_date = main_data['order_purchase_timestamp'].max()

# Membuat slider untuk memilih rentang tanggal
start_date, end_date = st.slider(
    "Pilih Rentang Tanggal:",
    min_value=min_date,
    max_value=max_date,
    value=(min_date, max_date)
)

# Filter data berdasarkan rentang tanggal yang dipilih
filtered_data = main_data[
    (main_data['order_purchase_timestamp'] >= start_date) &
    (main_data['order_purchase_timestamp'] <= end_date)
]

st.write(f"Menampilkan data untuk rentang tanggal: {start_date.date()} hingga {end_date.date()}")
st.write(filtered_data)

# --- Analisis 1: Kategori Produk dengan Penjualan Tertinggi dan Terendah ---
# 1.1: Penjualan berdasarkan kategori produk
st.subheader("1.1: Penjualan Produk berdasarkan Kategori")
category_sales = filtered_data.groupby('product_category_name')['price'].sum().sort_values(ascending=False)

if not category_sales.empty:
    highest_sales_category = category_sales.head(1)
    lowest_sales_category = category_sales.tail(1)

    st.write("**Kategori Produk dengan Penjualan Tertinggi:**")
    st.write(highest_sales_category)

    st.write("**Kategori Produk dengan Penjualan Terendah:**")
    st.write(lowest_sales_category)

    # Membatasi jumlah kategori untuk visualisasi (10 teratas)
    top_10_categories = category_sales.nlargest(10)

    # Visualisasi 10 kategori produk dengan penjualan tertinggi
    st.subheader("Visualisasi Penjualan Kategori Produk")
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x=top_10_categories.index, y=top_10_categories.values, ax=ax, palette="viridis")

    # Modifikasi tampilan
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
    ax.set_xlabel('Kategori Produk', fontsize=12)
    ax.set_ylabel('Penjualan (Total Harga)', fontsize=12)
    ax.set_title('10 Kategori Produk dengan Penjualan Tertinggi', fontsize=14)
    ax.tick_params(axis='x', labelsize=10)
    ax.tick_params(axis='y', labelsize=10)

    # Menampilkan plot di Streamlit
    st.pyplot(fig)
else:
    st.write("Tidak ada data yang tersedia untuk rentang tanggal yang dipilih.")

# 1.2: Tren Penjualan Produk berdasarkan Tahun
st.subheader("1.2: Tren Penjualan Produk berdasarkan Tahun")
filtered_data['year'] = filtered_data['order_purchase_timestamp'].dt.year
yearly_sales = filtered_data.groupby('year')['price'].sum()

if not yearly_sales.empty:
    st.write(yearly_sales)

    # Visualisasi Tren Penjualan Produk per Tahun
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(x=yearly_sales.index, y=yearly_sales.values, ax=ax)
    ax.set_xlabel('Tahun')
    ax.set_ylabel('Total Penjualan (Harga)')
    ax.set_title('Tren Penjualan Produk per Tahun')
    st.pyplot(fig)
else:
    st.write("Tidak ada data yang tersedia untuk tren penjualan pada rentang tanggal yang dipilih.")

# --- Analisis 2: Distribusi Tipe Pembayaran pada Pesanan ---
# 2.1: Distribusi tipe pembayaran
st.subheader("2.1: Distribusi Tipe Pembayaran")
payment_type_dist = filtered_data['payment_type'].value_counts()

if not payment_type_dist.empty:
    st.write(payment_type_dist)

    # Visualisasi Distribusi Tipe Pembayaran
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=payment_type_dist.index, y=payment_type_dist.values, ax=ax, palette="muted")
    ax.set_xlabel('Tipe Pembayaran')
    ax.set_ylabel('Jumlah Pesanan')
    ax.set_title('Distribusi Tipe Pembayaran')
    st.pyplot(fig)
else:
    st.write("Tidak ada data yang tersedia untuk distribusi tipe pembayaran pada rentang tanggal yang dipilih.")

# 2.2: Tipe Pembayaran yang Paling Sering Digunakan
st.subheader("2.2: Tipe Pembayaran yang Paling Sering Digunakan")
if not payment_type_dist.empty:
    most_common_payment_type = payment_type_dist.idxmax()
    st.write(f"Tipe Pembayaran yang Paling Sering Digunakan: **{most_common_payment_type}**")
else:
    st.write("Tidak ada data yang tersedia untuk tipe pembayaran pada rentang tanggal yang dipilih.")
