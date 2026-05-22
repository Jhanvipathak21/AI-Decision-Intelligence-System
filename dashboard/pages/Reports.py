import streamlit as st
import pandas as pd
from datetime import datetime

# =========================
# LOGIN PROTECTION
# =========================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.warning("Please login first 🔒")
    st.stop()

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
    "images/RobotAi.png",
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

try:

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

except Exception as e:
    st.error(f"Error loading report data: {e}")

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

st.markdown("""
<hr style="margin-top:50px; margin-bottom:20px; border:1px solid rgba(255,255,255,0.08);">

<div style="
    text-align:center;
    padding:15px;
    color:#9CA3AF;
    font-size:15px;
">
© 2026 AI Decision Intelligence Platform | Developed by <span style="color:#A855F7; font-weight:600;">Jhanvi Pathak</span>
</div>
""", unsafe_allow_html=True)
