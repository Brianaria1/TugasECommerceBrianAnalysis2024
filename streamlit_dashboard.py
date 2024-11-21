
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import gdown

url = "https://drive.google.com/file/d/10qUFPUnNzo8uRaJ6HDLgueio1q1TBHAf/"
output = "main_data.csv"
gdown.download(url, output, quiet=False)

# Set page configuration
st.set_page_config(page_title="Dashboard E-Commerce", layout="wide")

# Sidebar for file upload
st.sidebar.title("Upload Data")
uploaded_file_customers = st.sidebar.file_uploader("Upload customers_dataset.csv", type=["csv"])
uploaded_file_orders = st.sidebar.file_uploader("Upload orders_dataset.csv", type=["csv"])
uploaded_file_items = st.sidebar.file_uploader("Upload order_items_dataset.csv", type=["csv"])

# Load datasets
if uploaded_file_customers and uploaded_file_orders and uploaded_file_items:
    # Read datasets
    customers = pd.read_csv(uploaded_file_customers)
    orders = pd.read_csv(uploaded_file_orders)
    items = pd.read_csv(uploaded_file_items)
    
    # Display dataset shapes
    st.write("## Dataset Shapes")
    st.write(f"Customers: {customers.shape}, Orders: {orders.shape}, Items: {items.shape}")
    
    # Display data samples
    st.write("## Sample Data")
    st.write("### Customers Dataset")
    st.dataframe(customers.head())
    
    st.write("### Orders Dataset")
    st.dataframe(orders.head())
    
    st.write("### Items Dataset")
    st.dataframe(items.head())

    # Analysis Section
    st.write("## Analysis and Visualizations")
    
    # Example: Customer distribution
    st.write("### Customer Distribution by State")
    if 'customer_state' in customers.columns:
        state_distribution = customers['customer_state'].value_counts()
        st.bar_chart(state_distribution)
    else:
        st.warning("Column 'customer_state' not found in customers dataset.")
    
    # Example: Order value analysis
    st.write("### Order Values")
    if 'price' in items.columns:
        st.write(f"Total Order Value: ${items['price'].sum():,.2f}")
        st.write(f"Average Order Value: ${items['price'].mean():,.2f}")
        fig, ax = plt.subplots()
        sns.histplot(items['price'], bins=30, kde=True, ax=ax)
        ax.set_title("Distribution of Order Prices")
        st.pyplot(fig)
    else:
        st.warning("Column 'price' not found in order items dataset.")
else:
    st.warning("Please upload all required datasets to proceed.")

