import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Konfigurasi halaman Streamlit
st.set_page_config(
    page_title="Dashboard E-Commerce Brasil",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Judul aplikasi
st.title("Dashboard E-Commerce Brasil")

# Membaca dataset
@st.cache_data
def load_data():
    return pd.read_csv("main_data.csv")

data = load_data()

# Sidebar
st.sidebar.header("Filter Data")
start_date = st.sidebar.date_input("Tanggal Mulai", value=pd.to_datetime(data['order_purchase_timestamp']).min())
end_date = st.sidebar.date_input("Tanggal Akhir", value=pd.to_datetime(data['order_purchase_timestamp']).max())

# Filter berdasarkan tanggal
filtered_data = data[
    (pd.to_datetime(data['order_purchase_timestamp']) >= pd.to_datetime(start_date)) &
    (pd.to_datetime(data['order_purchase_timestamp']) <= pd.to_datetime(end_date))
]

st.sidebar.write(f"Jumlah data yang ditampilkan: {len(filtered_data)}")

# **Analisis 1: Kategori Produk**
st.header("Analisis Kategori Produk")
top_categories = (
    filtered_data['product_category_name']
    .value_counts()
    .head(5)
    .sort_values(ascending=False)
)
bottom_categories = (
    filtered_data['product_category_name']
    .value_counts()
    .tail(5)
    .sort_values(ascending=True)
)

col1, col2 = st.columns(2)

# Bar Chart: Top Categories
with col1:
    st.subheader("Top 5 Kategori Produk")
    fig, ax = plt.subplots()
    ax.bar(top_categories.index, top_categories.values, color="skyblue")
    ax.set_xlabel("Kategori Produk")
    ax.set_ylabel("Jumlah Penjualan")
    ax.set_title("Top 5 Kategori Produk")
    plt.xticks(rotation=45)
    st.pyplot(fig)

# Bar Chart: Bottom Categories
with col2:
    st.subheader("Bottom 5 Kategori Produk")
    fig, ax = plt.subplots()
    ax.bar(bottom_categories.index, bottom_categories.values, color="salmon")
    ax.set_xlabel("Kategori Produk")
    ax.set_ylabel("Jumlah Penjualan")
    ax.set_title("Bottom 5 Kategori Produk")
    plt.xticks(rotation=45)
    st.pyplot(fig)

# Tren Penjualan Produk
st.subheader("Tren Penjualan Produk")
filtered_data['order_year'] = pd.to_datetime(filtered_data['order_purchase_timestamp']).dt.year
trend = filtered_data.groupby(['order_year', 'product_category_name']).size().unstack(fill_value=0)

fig, ax = plt.subplots(figsize=(10, 6))
for category in top_categories.index:
    if category in trend.columns:
        ax.plot(trend.index, trend[category], label=category)
ax.set_xlabel("Tahun")
ax.set_ylabel("Jumlah Penjualan")
ax.set_title("Tren Penjualan Produk (Top 5 Kategori)")
ax.legend(title="Kategori", bbox_to_anchor=(1.05, 1), loc='upper left')
st.pyplot(fig)

# **Analisis 2: Distribusi Tipe Pembayaran**
st.header("Distribusi Tipe Pembayaran")
payment_counts = filtered_data['payment_type'].value_counts()

# Bar Chart: Distribusi Tipe Pembayaran
fig, ax = plt.subplots()
ax.bar(payment_counts.index, payment_counts.values, color="green")
ax.set_xlabel("Tipe Pembayaran")
ax.set_ylabel("Jumlah Pesanan")
ax.set_title("Distribusi Tipe Pembayaran")
plt.xticks(rotation=45)
st.pyplot(fig)

# **Kesimpulan**
st.markdown("---")
st.header("Kesimpulan")
st.markdown(
    """
    1. **Kategori Produk**: 
       - **Top 5 kategori produk** dengan penjualan tertinggi ditampilkan secara visual dengan bar chart.
       - Tren penjualan produk dianalisis untuk kategori produk yang sering terjual setiap tahun.
       - **Bottom 5 kategori produk** menunjukkan produk dengan penjualan terendah.

    2. **Distribusi Tipe Pembayaran**: 
       - Tipe pembayaran paling sering digunakan adalah **{0}**.
       - Tipe pembayaran lain juga ditampilkan dalam bar chart.
    """.format(payment_counts.idxmax())
)
