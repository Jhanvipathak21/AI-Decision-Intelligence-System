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
    page_title="System Status",
    page_icon="🖥️",
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
st.title("🖥️ System Status Dashboard")

st.success(
    "🚀 AI-powered monitoring system is active."
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
# SYSTEM STATUS DATA
# =========================
st.markdown("## ⚙️ AI System Health Status")

status_data = pd.DataFrame({
    "Component": [
        "Prediction Engine",
        "Database Connection",
        "Analytics System",
        "AI Monitoring"
    ],
    "Status": [
        "Active",
        "Connected",
        "Running",
        "Online"
    ]
})

try:
    st.dataframe(
        status_data,
        use_container_width=True
    )

except Exception as e:
    st.error(f"Error loading system status: {e}")

st.markdown("---")

# =========================
# LIVE METRICS
# =========================
st.markdown("## 📊 Live System Metrics")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="CPU Usage",
        value="42%"
    )

with col2:
    st.metric(
        label="Memory Usage",
        value="68%"
    )

with col3:
    st.metric(
        label="Active Users",
        value="124"
    )

st.markdown("---")

# =========================
# SYSTEM LOGS
# =========================
st.markdown("## 📄 Recent System Logs")

logs = [
    "✔ AI Prediction Engine Started",
    "✔ Customer Dataset Loaded",
    "✔ Business Analytics Updated",
    "✔ Reports Generated Successfully"
]

for log in logs:
    st.success(log)

st.markdown("---")

# =========================
# SYSTEM HEALTH
# =========================
st.markdown("## 💡 Overall System Health")

st.progress(95)

st.info(
    "System health is stable and running efficiently."
)

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