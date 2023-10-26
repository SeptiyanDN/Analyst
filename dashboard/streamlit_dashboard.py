import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load data
customers = pd.read_csv("data/customers_dataset.csv")
order_items = pd.read_csv("data/order_items_dataset.csv")
order_payments = pd.read_csv("data/order_payments_dataset.csv")
order_reviews = pd.read_csv("data/order_reviews_dataset.csv")
orders = pd.read_csv("data/orders_dataset.csv")
products = pd.read_csv("data/products_dataset.csv")
sellers = pd.read_csv("data/sellers_dataset.csv")

st.sidebar.title("Data Analysis Options")

analysis_type = st.sidebar.selectbox("Select Analysis Type", ["Pie Chart - Customer States", "Bar Chart - Order Status", "Stacked Bar Chart - Payment Types", "Histogram - Review Scores", "Scatter Plot - Product Weight vs. Product Price", "Heatmap - Correlation Matrix (Products)"])

st.title("Data Analysis Dashboard")

if analysis_type == "Pie Chart - Customer States":
    st.header("Pie Chart - Customer States")
    state_counts = customers["customer_state"].value_counts()
    fig = px.pie(state_counts, names=state_counts.index, values=state_counts.values)
    st.plotly_chart(fig)

elif analysis_type == "Bar Chart - Order Status":
    st.header("Bar Chart - Order Status")
    order_status_counts = orders["order_status"].value_counts()
    fig = px.bar(order_status_counts, x=order_status_counts.index, y=order_status_counts.values, labels={"x": "Order Status", "y": "Count"})
    st.plotly_chart(fig)

elif analysis_type == "Stacked Bar Chart - Payment Types":
    st.header("Stacked Bar Chart - Payment Types")
    payment_type_counts = order_payments["payment_type"].value_counts()
    fig = px.bar(order_payments, x="payment_type", color="payment_type", labels={"x": "Payment Type"})
    st.plotly_chart(fig)

elif analysis_type == "Histogram - Review Scores":
    st.header("Histogram - Review Scores")
    fig = px.histogram(order_reviews, x="review_score", title="Distribution of Review Scores")
    st.plotly_chart(fig)

elif analysis_type == "Scatter Plot - Product Weight vs. Product Price":
    st.header("Scatter Plot - Product Weight vs. Product Price")
    fig = px.scatter(products, x="product_weight_g", y="product_photos_qty", title="Product Weight vs. Product Photos Quantity", labels={"x": "Product Weight (g)", "y": "Product Photos Quantity"})
    st.plotly_chart(fig)


elif analysis_type == "Heatmap - Correlation Matrix (Products)":
    st.header("Heatmap - Correlation Matrix (Products)")
    correlation_matrix = products[["product_name_lenght", "product_description_lenght", "product_photos_qty", "product_weight_g", "product_length_cm", "product_height_cm", "product_width_cm"]].corr()
    fig = go.Figure(data=go.Heatmap(z=correlation_matrix, x=correlation_matrix.columns, y=correlation_matrix.columns))
    st.plotly_chart(fig)

