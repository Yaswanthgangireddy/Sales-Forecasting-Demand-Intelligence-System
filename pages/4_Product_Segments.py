import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import plotly.express as px

st.title("📦 Product Demand Segments")

# Load dataset
df = pd.read_csv("clean_superstore.csv")

# Check required columns
required_columns = ["Sub-Category", "Sales"]

for col in required_columns:
    if col not in df.columns:
        st.error(f"Column '{col}' not found in dataset.")
        st.write("Available Columns:")
        st.write(df.columns.tolist())
        st.stop()

# Aggregate only available columns
cluster = df.groupby("Sub-Category").agg(
    Total_Sales=("Sales", "sum"),
    Average_Sales=("Sales", "mean"),
    Sales_Count=("Sales", "count")
).reset_index()

# Features for clustering
X = cluster[["Total_Sales", "Average_Sales", "Sales_Count"]]

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# KMeans
kmeans = KMeans(
    n_clusters=4,
    random_state=42,
    n_init=10
)

cluster["Cluster"] = kmeans.fit_predict(X_scaled)

# PCA
pca = PCA(n_components=2)

points = pca.fit_transform(X_scaled)

cluster["PCA1"] = points[:, 0]
cluster["PCA2"] = points[:, 1]

# Scatter Plot
fig = px.scatter(
    cluster,
    x="PCA1",
    y="PCA2",
    color=cluster["Cluster"].astype(str),
    hover_name="Sub-Category",
    title="Product Demand Segments"
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Clustered Products")

st.dataframe(cluster)
