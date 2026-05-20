import streamlit as st
import pandas as pd
from datetime import datetime

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

# =========================
# SIDEBAR LOGO
# =========================
st.sidebar.image(
    "https://cdn-icons-png.flaticon.com/512/4712/4712027.png",
    width=120
)

# =========================
# TITLE SECTION
# =========================
st.title("📊 Analytics Dashboard")

st.success(
    "🚀 AI analytics engine is running successfully."
)

# =========================
# SYSTEM TIME
# =========================
current_time = datetime.now().strftime(
    "%d-%m-%Y %H:%M:%S"
)

st.caption(
    f"🕒 System Time: {current_time}"
)

st.markdown("---")

# =========================
# REVENUE ANALYTICS
# =========================
st.markdown("## 📈 Revenue Analytics")

# Revenue Chart
revenue_data = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Revenue": [12, 18, 15, 22, 28, 35]
})

st.line_chart(
    revenue_data.set_index("Month")
)

st.markdown("---")

# =========================
# KPI CARDS
# =========================
st.markdown("## 📌 Key Metrics")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "💰 Total Revenue",
        "$245K"
    )

with col2:
    st.metric(
        "📉 Churn Rate",
        "26%"
    )

with col3:
    st.metric(
        "👥 Active Customers",
        "7043"
    )

st.markdown("---")

# =========================
# CUSTOMER SEGMENTATION
# =========================
st.markdown("## 🥧 Customer Segmentation")

segment_data = pd.DataFrame({
    "Segment": [
        "Loyal",
        "At Risk",
        "New"
    ],
    "Customers": [4200, 1869, 974]
})

st.bar_chart(
    segment_data.set_index("Segment")
)

st.markdown("---")

# =========================
# AI ANALYTICS INSIGHTS
# =========================
st.markdown("## 🧠 AI Analytics Insights")

st.info(
    "📌 Revenue growth increased steadily over the last 6 months."
)

st.warning(
    "⚠️ Churn rate remains high among medium-tenure customers."
)

st.success(
    "✅ Loyal customer segment contributes the highest revenue."
)

st.markdown("---")

# =========================
# FOOTER
# =========================
st.markdown(
    "✨ Developed by Jhanvi Pathak | AI Decision Intelligence System"
)