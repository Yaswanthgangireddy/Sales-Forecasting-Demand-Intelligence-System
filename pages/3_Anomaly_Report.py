
import streamlit as st
import pandas as pd
from sklearn.ensemble import IsolationForest
import plotly.express as px

st.title("🚨 Sales Anomaly Report")

df=pd.read_csv("clean_superstore.csv")

df["Order Date"]=pd.to_datetime(df["Order Date"],dayfirst=True)

weekly=df.groupby(pd.Grouper(key="Order Date",freq="W"))["Sales"].sum().reset_index()

model=IsolationForest(
contamination=0.05,
random_state=42
)

weekly["Anomaly"]=model.fit_predict(weekly[["Sales"]])

fig=px.line(
weekly,
x="Order Date",
y="Sales",
title="Weekly Sales"
)

fig.add_scatter(
x=weekly[weekly["Anomaly"]==-1]["Order Date"],
y=weekly[weekly["Anomaly"]==-1]["Sales"],
mode="markers",
name="Anomaly"
)

st.plotly_chart(fig,use_container_width=True)

st.dataframe(
weekly[weekly["Anomaly"]==-1]
)
