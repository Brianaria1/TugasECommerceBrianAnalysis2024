import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Judul aplikasi Streamlit
st.title('Analisis E-Commerce: Penjualan Produk dan Pembayaran')

# Fungsi untuk memuat data dari URL Dropbox
def load_data_from_dropbox():
    url = "https://www.dropbox.com/scl/fi/x70t1awzkxtrkztjps55n/main_data.csv?rlkey=owlw5huxhfn484maqjfnl4ssz&st=pjp7vk4j&dl=1"
    main_data = pd.read_csv(url, parse_dates=["order_purchase_timestamp"])
    return main_data

# Memuat data dari Dropbox
main_data = load_data_from_dropbox()

# Menampilkan data beberapa baris pertama
st.write(main_data.head())

# Fitur interaktif: Filter berdasarkan rentang tanggal
st.subheader("Filter Data berdasarkan Rentang Tanggal")
min_date = main_data['order_purchase_timestamp'].min()
max_date = main_data['order_purchase_timestamp'].max()

# Membuat filter rentang tanggal menggunakan date_input
start_end_date = st.date_input(
    "Pilih Rentang Tanggal:",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

# Validasi input tanggal
if len(start_end_date) == 2:
    start_date = pd.to_datetime(start_end_date[0])
    end_date = pd.to_datetime(start_end_date[1])
else:
    st.error("Pilih rentang tanggal yang valid.")
    start_date = min_date
    end_date = max_date

# Filter data berdasarkan rentang tanggal
filtered_data = main_data[
    (main_data['order_purchase_timestamp'] >= start_date) &
    (main_data['order_purchase_timestamp'] <= end_date)
]

st.write(f"Data dari tanggal {start_date.date()} hingga {end_date.date()}:")
st.write(filtered_data)

# --- Analisis 1.1: Penjualan Produk berdasarkan Kategori ---
st.subheader("1.1: Penjualan Produk berdasarkan Kategori")
category_sales = filtered_data.groupby('product_category_name')['price'].sum().sort_values(ascending=False)

if not category_sales.empty:
    # 10 kategori dengan penjualan tertinggi
    top_10_categories = category_sales.nlargest(10)
    # 10 kategori dengan penjualan terendah
    bottom_10_categories = category_sales.nsmallest(10)

    # Visualisasi 10 kategori dengan penjualan tertinggi
    st.subheader("10 Kategori Produk dengan Penjualan Tertinggi")
    fig1, ax1 = plt.subplots(figsize=(12, 6))
    sns.barplot(x=top_10_categories.index, y=top_10_categories.values, ax=ax1, palette="viridis")
    ax1.set_xticklabels(ax1.get_xticklabels(), rotation=45, ha='right')
    ax1.set_xlabel('Kategori Produk')
    ax1.set_ylabel('Total Penjualan')
    ax1.set_title('10 Kategori Produk dengan Penjualan Tertinggi')
    st.pyplot(fig1)

    # Visualisasi 10 kategori dengan penjualan terendah
    st.subheader("10 Kategori Produk dengan Penjualan Terendah")
    fig2, ax2 = plt.subplots(figsize=(12, 6))
    sns.barplot(x=bottom_10_categories.index, y=bottom_10_categories.values, ax=ax2, palette="Reds_d")
    ax2.set_xticklabels(ax2.get_xticklabels(), rotation=45, ha='right')
    ax2.set_xlabel('Kategori Produk')
    ax2.set_ylabel('Total Penjualan')
    ax2.set_title('10 Kategori Produk dengan Penjualan Terendah')
    st.pyplot(fig2)
else:
    st.write("Tidak ada data yang tersedia untuk kategori produk pada rentang tanggal yang dipilih.")

# --- Analisis 1.2: Tren Penjualan Produk berdasarkan Tahun ---
st.subheader("1.2: Tren Penjualan Produk berdasarkan Tahun")
filtered_data.loc[:, 'year'] = filtered_data['order_purchase_timestamp'].dt.year
yearly_sales = filtered_data.groupby('year')['price'].sum()

if not yearly_sales.empty:
    st.write(yearly_sales)

    # Visualisasi Tren Penjualan Produk per Tahun
    fig3, ax3 = plt.subplots(figsize=(10, 6))
    sns.lineplot(x=yearly_sales.index, y=yearly_sales.values, ax=ax3)
    ax3.set_xlabel('Tahun')
    ax3.set_ylabel('Total Penjualan (Harga)')
    ax3.set_title('Tren Penjualan Produk per Tahun')
    st.pyplot(fig3)
else:
    st.write("Tidak ada data yang tersedia untuk tren penjualan pada rentang tanggal yang dipilih.")

# --- Analisis 2.1: Distribusi Tipe Pembayaran ---
st.subheader("2.1: Distribusi Tipe Pembayaran")
payment_type_dist = filtered_data['payment_type'].value_counts()

if not payment_type_dist.empty:
    st.write(payment_type_dist)

    # Visualisasi Distribusi Tipe Pembayaran
    fig4, ax4 = plt.subplots(figsize=(10, 6))
    sns.barplot(x=payment_type_dist.index, y=payment_type_dist.values, ax=ax4, palette="muted")
    ax4.set_xlabel('Tipe Pembayaran')
    ax4.set_ylabel('Jumlah Pesanan')
    ax4.set_title('Distribusi Tipe Pembayaran')
    st.pyplot(fig4)
else:
    st.write("Tidak ada data yang tersedia untuk distribusi tipe pembayaran pada rentang tanggal yang dipilih.")

# --- Analisis 2.2: Tipe Pembayaran yang Paling Sering Digunakan ---
st.subheader("2.2: Tipe Pembayaran yang Paling Sering Digunakan")
if not payment_type_dist.empty:
    most_common_payment_type = payment_type_dist.idxmax()
    st.write(f"Tipe Pembayaran yang Paling Sering Digunakan: **{most_common_payment_type}**")
else:
    st.write("Tidak ada data yang tersedia untuk tipe pembayaran pada rentang tanggal yang dipilih.")

