import streamlit as st
import pandas as pd
import sklearn
import joblib


# Load Dataset
df = pd.read_csv(
    "../dataset/WA_Fn-UseC_-Telco-Customer-Churn.csv"
)


# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="AI Decision Intelligence System",
    page_icon="🚀",
    layout="wide"
)

# =========================
# LOAD MODEL
# =========================
model = joblib.load(
    "../models/churn_model.pkl"
)

# =========================
# SIDEBAR WIDTH
# =========================
st.markdown("""
<style>
section[data-testid="stSidebar"] {
    width: 350px !important;
}
</style>
""", unsafe_allow_html=True)

# =========================
# CUSTOM CSS
# =========================
st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

.stMetric {
    background-color: #1E1E1E;
    padding: 15px;
    border-radius: 15px;
    border: 1px solid #333;
}

div.stButton > button {
    background-color: #FF4B4B;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-size: 18px;
    font-weight: bold;
}

div.stButton > button:hover {
    background-color: #FF2E2E;
    color: white;
}

[data-testid="stSidebar"] {
    background-color: #161A23;
}

</style>
""", unsafe_allow_html=True)

# =========================
# SIDEBAR LOGO
# =========================
st.sidebar.image(
    "https://cdn-icons-png.flaticon.com/512/4712/4712027.png",
    width=120
)

# =========================
# LOGIN SECTION
# =========================
st.sidebar.markdown("## 🔐 User Login")

username = st.sidebar.text_input("👤 Username")

password = st.sidebar.text_input(
    "🔑 Password",
    type="password"
)

login_button = st.sidebar.button("Login")

if login_button:

    if username == "admin" and password == "admin123":

        st.sidebar.success(
            "✅ Login Successful"
        )

    else:

        st.sidebar.error(
            "❌ Invalid Username or Password"
        )

# =========================
# SIDEBAR
# =========================
st.sidebar.header(
    "🧾 Customer Input Parameters"
)

st.sidebar.markdown("---")

st.sidebar.markdown(
    "## ℹ️ Project Information"
)

st.sidebar.info(
    """
    AI Decision Intelligence System

    Features:

    ✅ Customer Churn Prediction
    ✅ Risk Analysis
    ✅ AI Insights
    ✅ Business Dashboard
    ✅ Report Generation
    """
)

# =========================
# USER INPUTS
# =========================
tenure = st.sidebar.slider(
    "📅 Tenure",
    0,
    72,
    12
)

monthlycharges = st.sidebar.slider(
    "💳 Monthly Charges",
    0,
    200,
    70
)

totalcharges = st.sidebar.slider(
    "💰 Total Charges",
    0,
    10000,
    1000
)

gender = st.sidebar.selectbox(
    "👤 Gender",
    ["Male", "Female"]
)

seniorcitizen = st.sidebar.selectbox(
    "🧓 Senior Citizen",
    [0, 1]
)

partner = st.sidebar.selectbox(
    "💍 Partner",
    ["Yes", "No"]
)

dependents = st.sidebar.selectbox(
    "👨‍👩‍👧 Dependents",
    ["Yes", "No"]
)

# =========================
# NOTIFICATION CENTER
# =========================
st.sidebar.markdown("---")

st.sidebar.markdown(
    "## 🚨 Notification Center"
)

notifications = []

if monthlycharges > 80:

    notifications.append(
        "⚠️ High monthly charges detected."
    )

if tenure < 12:

    notifications.append(
        "🚨 New customer at high churn risk."
    )

if partner == "No":

    notifications.append(
        "📞 Retention outreach recommended."
    )

if len(notifications) == 0:

    st.sidebar.success(
        "✅ No critical alerts."
    )

for note in notifications:

    st.sidebar.warning(note)

# =========================
# TITLE SECTION
# =========================
st.title(
    "🤖 AI Decision Intelligence System"
)

st.subheader(
    "📊 Customer Churn Prediction Dashboard"
)

st.success(
    "🚀 AI-powered churn intelligence platform is active."
)

st.caption(
    f"Scikit-learn Version: {sklearn.__version__}"
)

st.markdown("---")

# =========================
# KPI CARDS
# =========================
st.markdown(
    "## 📌 Key Performance Indicators"
)

col1, col2, col3, col4 = st.columns(4)
# Total Customers
total_customers = len(df)

# High Risk Customers
high_risk = len(
    df[df["Churn"] == "Yes"]
)

# Retention Rate
retention_rate = round(
    (
        len(df[df["Churn"] == "No"])
        / len(df)
    ) * 100,
    2
)

# Revenue Impact
revenue_impact = round(
    df["MonthlyCharges"].astype(float).sum() / 1000,
    2
)

with col1:

    st.metric(
        "👥 Total Customers",
        total_customers
    )

with col2:

    st.metric(
        "⚠️ High Risk Customers",
        high_risk
    )

with col3:

    st.metric(
        "💰 Revenue Impact",
        f"${revenue_impact}K"
    )

with col4:

    st.metric(
        "📈 Retention Rate",
        f"{retention_rate}%"
    )
# with col1:

#     st.metric(
#         "👥 Total Customers",
#         "7043"
#     )

# with col2:

#     st.metric(
#         "⚠️ High Risk Customers",
#         "1869"
#     )

# with col3:

#     st.metric(
#         "💰 Revenue Impact",
#         "$139K"
#     )

# with col4:

#     st.metric(
#         "📈 Retention Rate",
#         "73%"
#     )

st.markdown("---")

# =========================
# CUSTOMER PROFILE
# =========================
st.markdown(
    "## 🧑‍💼 Customer Profile Summary"
)

profile_col1, profile_col2 = st.columns(2)

with profile_col1:

    st.write(f"👤 Gender: {gender}")

    st.write(
        f"🧓 Senior Citizen: {seniorcitizen}"
    )

    st.write(f"💍 Partner: {partner}")

with profile_col2:

    st.write(
        f"👨‍👩‍👧 Dependents: {dependents}"
    )

    st.write(
        f"📅 Tenure: {tenure} months"
    )

    st.write(
        f"💳 Monthly Charges: ${monthlycharges}"
    )

st.markdown("---")

# =========================
# CUSTOMER ANALYSIS
# =========================
st.markdown("## 🚀 Customer Analysis")

# Default Risk Value
risk_value = 0

if st.button("🚀 Analyze Customer"):

    # Create Input Data
    input_data = pd.DataFrame({
        "tenure": [tenure],
        "MonthlyCharges": [monthlycharges],
        "TotalCharges": [totalcharges]
    })

    # Model Prediction
    prediction = model.predict(input_data)

    # Probability Prediction
    probability = model.predict_proba(input_data)

    # Risk Score
    churn_probability = probability[0][1] * 100

    risk_value = int(churn_probability)

    # Success Notification
    st.toast(
        "Prediction Completed Successfully 🚀"
    )

    # Display Risk Score
    st.info(
        f"🎯 Customer Risk Score: {churn_probability:.2f}%"
    )

    # Prediction Result
    if prediction[0] == 1:

        st.error(
            "🚨 Customer is likely to Churn"
        )

    else:

        st.success(
            "✅ Customer is likely to Stay"
        )

    st.markdown("---")

    # =========================
    # REAL-TIME RISK METER
    # =========================
    st.markdown(
        "## 🎯 Real-Time Risk Meter"
    )

    st.progress(risk_value)

    if risk_value >= 80:

        st.error(
            f"🔴 High Risk Score: {risk_value}%"
        )

    elif risk_value >= 50:

        st.warning(
            f"🟠 Medium Risk Score: {risk_value}%"
        )

    else:

        st.success(
            f"🟢 Low Risk Score: {risk_value}%"
        )

    st.markdown("---")

    # =========================
    # CUSTOMER RISK LEVEL
    # =========================
    st.markdown(
        "## 🛡️ Customer Risk Level"
    )

    if risk_value >= 80:

        st.error(
            "🔴 HIGH RISK CUSTOMER"
        )

    elif risk_value >= 50:

        st.warning(
            "🟠 MEDIUM RISK CUSTOMER"
        )

    else:

        st.success(
            "🟢 LOW RISK CUSTOMER"
        )

# =========================
# FOOTER
# =========================
st.markdown("---")

st.markdown(
    "✨ Developed by Jhanvi Pathak | AI Decision Intelligence System"
)




























# # =========================
# # CUSTOMER ANALYSIS
# # =========================
# st.markdown("## 🚀 Customer Analysis")

# churn_probability = 20

# if st.button("🚀 Analyze Customer"):

#     if tenure < 12 and monthlycharges > 80:
#         churn_probability = 85
#         prediction = 1

#     else:
#         churn_probability = 20
#         prediction = 0

#     st.toast("Prediction Completed Successfully 🚀")

#     st.info(
#         f"🎯 Customer Risk Score: {churn_probability}%"
#     )

#     if prediction == 1:
#         st.error("🚨 Customer is likely to Churn")

#     else:
#         st.success("✅ Customer is likely to Stay")

# st.markdown("---")

# # =========================
# # REAL-TIME RISK METER
# # =========================
# st.markdown("## 🎯 Real-Time Risk Meter")

# risk_value = 20

# if tenure < 12 and monthlycharges > 80:
#     risk_value = 85

# elif tenure < 24:
#     risk_value = 55

# st.progress(risk_value)

# if risk_value >= 80:
#     st.error(f"🔴 High Risk Score: {risk_value}%")

# elif risk_value >= 50:
#     st.warning(f"🟠 Medium Risk Score: {risk_value}%")

# else:
#     st.success(f"🟢 Low Risk Score: {risk_value}%")

# st.markdown("---")

# # # =========================
# # # CUSTOMER RISK LEVEL (dummy)
# # # =========================
# # st.markdown("## 🛡️ Customer Risk Level")

# # if tenure < 12 and monthlycharges > 80:
# #     st.error("🔴 HIGH RISK CUSTOMER")

# # elif tenure < 24:
# #     st.warning("🟠 MEDIUM RISK CUSTOMER")

# # else:
# #     st.success("🟢 LOW RISK CUSTOMER")
# # =========================
# # Real model
# # =========================

# if st.button("🚀 Analyze Customer"):

#     input_data = pd.DataFrame({
#         "tenure": [tenure],
#         "MonthlyCharges": [monthlycharges],
#         "TotalCharges": [totalcharges]
#     })

#     prediction = model.predict(input_data)

#     probability = model.predict_proba(input_data)

#     churn_probability = probability[0][1] * 100

#     st.info(
#         f"🎯 Customer Risk Score: {churn_probability:.2f}%"
#     )

#     if prediction[0] == 1:
#         st.error(
#             "🚨 Customer is likely to Churn"
#         )

#     else:
#         st.success(
#             "✅ Customer is likely to Stay"
#         )


# # =========================
# # FOOTER
# # =========================
# st.markdown("---")

# st.markdown(
#     "✨ Developed by Jhanvi Pathak | AI Decision Intelligence System"
# )