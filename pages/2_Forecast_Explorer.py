
import streamlit as st
import pandas as pd
from prophet import Prophet
import plotly.express as px

st.title("🔮 Forecast Explorer")

df=pd.read_csv("clean_superstore.csv")

df["Order Date"] = pd.to_datetime(
    df["Order Date"],
    dayfirst=True,
    format="mixed",
    errors="coerce"
)

monthly=df.groupby(pd.Grouper(key="Order Date",freq="ME"))["Sales"].sum().reset_index()

monthly.columns=["ds","y"]

model=Prophet()

model.fit(monthly)

future=model.make_future_dataframe(periods=3,freq="ME")

forecast=model.predict(future)

fig=px.line(
    forecast,
    x="ds",
    y="yhat",
    title="3 Month Sales Forecast"
)

st.plotly_chart(fig,use_container_width=True)

st.dataframe(
forecast[["ds","yhat","yhat_lower","yhat_upper"]].tail(3)
)
