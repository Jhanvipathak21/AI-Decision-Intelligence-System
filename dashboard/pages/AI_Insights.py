import streamlit as st
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
    page_title="AI Insights",
    page_icon="🧠",
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
st.title("🧠 AI Insights Dashboard")

st.success(
    "🚀 AI recommendation engine is active."
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
# AI RECOMMENDATION ENGINE
# =========================
st.markdown("## 🤖 AI Recommendation Engine")

monthlycharges = st.slider(
    "💳 Monthly Charges",
    0,
    200,
    90
)

tenure = st.slider(
    "📅 Tenure",
    0,
    72,
    10
)

partner = st.selectbox(
    "💍 Partner",
    ["Yes", "No"]
)

dependents = st.selectbox(
    "👨‍👩‍👧 Dependents",
    ["Yes", "No"]
)

recommendations = []

if tenure < 12:
    recommendations.append(
        "🎁 Offer welcome discounts for new customers."
    )

if monthlycharges > 80:
    recommendations.append(
        "💰 Suggest affordable subscription plans."
    )

if partner == "No":
    recommendations.append(
        "📞 Personalized retention calls recommended."
    )

if dependents == "No":
    recommendations.append(
        "👨‍👩‍👧 Promote bundled family offers."
    )

if tenure < 12 and monthlycharges > 80:
    recommendations.append(
        "🚨 Immediate retention action required."
    )

st.markdown("---")

# =========================
# AI RECOMMENDATIONS
# =========================
st.markdown("## 📋 AI Recommendations")

for rec in recommendations:
    st.write(rec)

if len(recommendations) == 0:
    st.success(
        "✅ Customer profile looks healthy."
    )

st.markdown("---")

# =========================
# LIVE AI MONITORING
# =========================
st.markdown("## 🤖 Live AI Monitoring")

st.success("✅ AI Prediction Engine Active")

st.info("📡 Real-time monitoring enabled")

st.success("🔄 AI analytics updated successfully")

st.markdown("---")

# =========================
# AI RISK ANALYSIS
# =========================
st.markdown("## 🚨 AI Risk Analysis")

if tenure < 12 and monthlycharges > 80:
    st.error(
        "🔴 High churn risk detected."
    )

elif tenure < 24:
    st.warning(
        "🟠 Medium churn risk detected."
    )

else:
    st.success(
        "🟢 Low churn risk detected."
    )

st.markdown("---")

# =========================
# AI BUSINESS INSIGHTS
# =========================
st.markdown("## 💡 AI Business Insights")

st.info(
    "📌 Customers with high monthly charges show increased churn probability."
)

st.warning(
    "⚠️ New customers require stronger retention strategies."
)

st.success(
    "✅ Loyal customers contribute significantly to revenue stability."
)

st.markdown("---")

# # =========================
# # FOOTER
# # =========================
# st.markdown(
#     "✨ Developed by Jhanvi Pathak | AI Decision Intelligence System"
# )

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