
import streamlit as st

st.set_page_config(
    page_title="Sales Forecasting Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Sales Forecasting & Demand Intelligence System")

st.markdown("""
### Welcome

Use the navigation panel on the left to explore:

- 📈 Sales Overview
- 🔮 Forecast Explorer
- 🚨 Anomaly Report
- 📦 Product Demand Segments
""")

st.success("Dashboard Loaded Successfully")
