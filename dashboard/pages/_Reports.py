import streamlit as st
import pandas as pd
from datetime import datetime

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Reports Dashboard",
    page_icon="📈",
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
st.title("📈 Reports Dashboard")

st.success(
    "🚀 AI-powered reporting system is active."
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
# REPORTS SECTION
# =========================
st.markdown("## 📄 Business Reports")

# Report Data
report_data = pd.DataFrame({
    "Department": [
        "Sales",
        "Customer Support",
        "Marketing",
        "Retention"
    ],
    "Performance": [85, 78, 90, 88]
})

st.dataframe(
    report_data,
    use_container_width=True
)

st.markdown("---")

# =========================
# DOWNLOAD REPORT
# =========================
report = """
AI Decision Intelligence System Report

Total Customers: 7043
Retention Rate: 73%
High Risk Customers: 1869

System Status:
AI Monitoring Active
Prediction Engine Running
"""

st.download_button(
    label="📥 Download Full Report",
    data=report,
    file_name="AI_Report.txt",
    mime="text/plain"
)

st.markdown("---")

# =========================
# PERFORMANCE METRICS
# =========================
st.markdown("## 📊 Department Performance")

st.bar_chart(
    report_data.set_index("Department")
)

st.markdown("---")

# =========================
# REPORT STATUS
# =========================
st.markdown("## ⚙️ Report Status")

col1, col2, col3 = st.columns(3)

with col1:
    st.success("✅ Reports Generated")

with col2:
    st.success("✅ Data Synced")

with col3:
    st.success("✅ Analytics Updated")

st.markdown("---")

# =========================
# FOOTER
# =========================
st.markdown(
    "✨ Developed by Jhanvi Pathak | AI Decision Intelligence System"
)