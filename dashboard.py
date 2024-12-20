import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Judul aplikasi Streamlit
st.title('Analisis E-Commerce: Penjualan Produk dan Pembayaran')

# Fungsi untuk memuat data
def load_data_from_dropbox():
    url = "https://www.dropbox.com/scl/fi/x70t1awzkxtrkztjps55n/main_data.csv?rlkey=owlw5huxhfn484maqjfnl4ssz&st=pjp7vk4j&dl=1"
    main_data = pd.read_csv(url, parse_dates=["order_purchase_timestamp"])
    return main_data

# Memuat data
main_data = load_data_from_dropbox()

# Filter data berdasarkan rentang tanggal
st.subheader("Filter Data berdasarkan Rentang Tanggal")
min_date = main_data['order_purchase_timestamp'].min()
max_date = main_data['order_purchase_timestamp'].max()

start_date, end_date = st.slider(
    "Pilih Rentang Tanggal:",
    min_value=min_date.to_pydatetime(),
    max_value=max_date.to_pydatetime(),
    value=(min_date.to_pydatetime(), max_date.to_pydatetime())
)

# Filter data dengan salinan untuk menghindari SettingWithCopyWarning
filtered_data = main_data[
    (main_data['order_purchase_timestamp'] >= start_date) &
    (main_data['order_purchase_timestamp'] <= end_date)
].copy()

# Tambahkan kolom tahun
filtered_data['year'] = filtered_data['order_purchase_timestamp'].dt.year

# Menampilkan data hasil filter
st.write(f"Data dari {start_date.date()} hingga {end_date.date()}:")
st.write(filtered_data)

# Analisis distribusi penjualan per tahun
st.subheader("Distribusi Penjualan per Tahun")
sales_per_year = filtered_data.groupby('year')['order_id'].count().reset_index()
sales_per_year.columns = ['Year', 'Total Sales']

# Visualisasi distribusi penjualan
fig, ax = plt.subplots()
sns.barplot(data=sales_per_year, x='Year', y='Total Sales', ax=ax)
ax.set_title("Distribusi Penjualan per Tahun")
ax.set_xlabel("Tahun")
ax.set_ylabel("Total Penjualan")
st.pyplot(fig)

# Analisis metode pembayaran
st.subheader("Metode Pembayaran yang Digunakan")
payment_method_count = filtered_data['payment_type'].value_counts().reset_index()
payment_method_count.columns = ['Payment Method', 'Count']

# Visualisasi metode pembayaran
fig, ax = plt.subplots()
sns.barplot(data=payment_method_count, x='Count', y='Payment Method', ax=ax, palette="viridis")
ax.set_title("Metode Pembayaran yang Digunakan")
ax.set_xlabel("Jumlah")
ax.set_ylabel("Metode Pembayaran")
st.pyplot(fig)

# Analisis kategori produk yang paling laris
st.subheader("Kategori Produk yang Paling Laris")
top_categories = (
    filtered_data.groupby('product_category_name_english')['order_id']
    .count()
    .reset_index()
    .sort_values(by='order_id', ascending=False)
    .head(10)
)
top_categories.columns = ['Category', 'Total Orders']

# Visualisasi kategori produk
fig, ax = plt.subplots()
sns.barplot(data=top_categories, x='Total Orders', y='Category', ax=ax, palette="cubehelix")
ax.set_title("10 Kategori Produk Teratas")
ax.set_xlabel("Total Pesanan")
ax.set_ylabel("Kategori Produk")
st.pyplot(fig)

# Penutup
st.write("Dashboard ini memberikan wawasan mengenai penjualan dan pembayaran e-commerce.")
