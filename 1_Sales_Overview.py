
import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📈 Sales Overview Dashboard")

df = pd.read_csv("train.csv")

df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True)

df["Year"] = df["Order Date"].dt.year
df["Month"] = df["Order Date"].dt.month_name()

# KPIs
col1,col2,col3 = st.columns(3)

col1.metric("Total Sales",f"${df['Sales'].sum():,.2f}")
col2.metric("Total Orders",len(df))
col3.metric("Average Sales",f"${df['Sales'].mean():,.2f}")

# Yearly Sales
yearly=df.groupby("Year")["Sales"].sum().reset_index()

fig=px.bar(
    yearly,
    x="Year",
    y="Sales",
    title="Yearly Sales"
)

st.plotly_chart(fig,use_container_width=True)

# Monthly Trend
monthly=df.groupby(pd.Grouper(key="Order Date",freq="ME"))["Sales"].sum().reset_index()

fig=px.line(
    monthly,
    x="Order Date",
    y="Sales",
    markers=True,
    title="Monthly Sales Trend"
)

st.plotly_chart(fig,use_container_width=True)

# Category Sales
category=df.groupby("Category")["Sales"].sum().reset_index()

fig=px.pie(
    category,
    names="Category",
    values="Sales",
    title="Sales by Category"
)

st.plotly_chart(fig,use_container_width=True)
