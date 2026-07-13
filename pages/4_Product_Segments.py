
import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import plotly.express as px

st.title("📦 Product Demand Segments")

df=pd.read_csv("clean_superstore.csv")

cluster=df.groupby("Sub-Category").agg(
Sales=("Sales","sum"),
Profit=("Profit","sum"),
Quantity=("Quantity","sum")
).reset_index()

X=cluster[["Sales","Profit","Quantity"]]

X=StandardScaler().fit_transform(X)

kmeans=KMeans(
n_clusters=4,
random_state=42,
n_init=10
)

cluster["Cluster"]=kmeans.fit_predict(X)

pca=PCA(n_components=2)

points=pca.fit_transform(X)

cluster["PCA1"]=points[:,0]

cluster["PCA2"]=points[:,1]

fig=px.scatter(
cluster,
x="PCA1",
y="PCA2",
color=cluster["Cluster"].astype(str),
hover_name="Sub-Category"
)

st.plotly_chart(fig,use_container_width=True)

st.dataframe(cluster)
