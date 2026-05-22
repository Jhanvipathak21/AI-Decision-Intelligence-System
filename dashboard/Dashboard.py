import streamlit as st
import pandas as pd
import sklearn
import joblib
import plotly.express as px
import streamlit as st

# =========================
# SESSION STATE
# =========================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="AI Decision Intelligence System",
    page_icon="🚀",
    layout="wide"
)

# =========================
# LOAD DATASET
# =========================

df = pd.read_csv(
    "dataset/WA_Fn-UseC_-Telco-Customer-Churn.csv"
)

# =========================
# LOAD MODEL
# =========================

model = joblib.load(
    "models/churn_model.pkl"
)

# =========================
# SIDEBAR WIDTH
# =========================

st.markdown("""
<style>

section[data-testid="stSidebar"] {
    width: 350px !important;
}

/* =========================
MAIN BACKGROUND
========================= */

.stApp {
    background: linear-gradient(
        135deg,
        #050816,
        #0B1026,
        #111827
    );
    color: white;
}

/* =========================
SIDEBAR
========================= */

[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #0B1020,
        #111827
    );
    border-right: 1px solid #7C3AED;
}

/* =========================
HEADINGS
========================= */

h1, h2, h3, h4 {
    color: white !important;
    font-weight: 700;
}

/* =========================
GLASS KPI CARDS
========================= */

[data-testid="metric-container"] {

    background: rgba(17, 24, 39, 0.75);

    border: 1px solid rgba(124, 58, 237, 0.3);

    padding: 20px;

    border-radius: 20px;

    backdrop-filter: blur(12px);

    box-shadow:
        0 0 20px rgba(124, 58, 237, 0.2);

    transition: 0.3s;
}

[data-testid="metric-container"]:hover {

    transform: translateY(-5px);

    box-shadow:
        0 0 30px rgba(168, 85, 247, 0.5);
}

/* =========================
BUTTONS
========================= */

div.stButton > button {

    background: linear-gradient(
        90deg,
        #7C3AED,
        #A855F7
    );

    color: white;

    border: none;

    border-radius: 12px;

    padding: 12px;

    font-size: 18px;

    font-weight: bold;

    transition: 0.3s;

    box-shadow:
        0 0 15px rgba(124, 58, 237, 0.4);
}

div.stButton > button:hover {

    transform: scale(1.03);

    background: linear-gradient(
        90deg,
        #9333EA,
        #C084FC
    );
}

/* =========================
INPUT BOXES
========================= */

.stTextInput > div > div > input {

    background-color: #111827;

    color: white;

    border-radius: 10px;

    border: 1px solid #7C3AED;
}

/* =========================
SELECTBOX
========================= */

.stSelectbox > div > div {

    background-color: #111827;

    border-radius: 10px;

    border: 1px solid #7C3AED;
}

/* =========================
SCROLLBAR
========================= */

::-webkit-scrollbar {
    width: 10px;
}

::-webkit-scrollbar-thumb {

    background: #7C3AED;

    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

# =========================
# SIDEBAR LOGO
# =========================

st.sidebar.image(
    "images/RobotAi.png",
    width=120
)
import streamlit as st

# LOGIN INPUTS
username = st.sidebar.text_input("Username")
password = st.sidebar.text_input("Password", type="password")

if st.sidebar.button("Login"):

    if username == "admin" and password == "admin123":
        st.session_state.logged_in = True
        st.sidebar.success("Login Successful ✅")
if st.session_state.logged_in:

# # LOGOUT BUTTON

    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()
    else:
        st.sidebar.error("Invalid Credentials ❌")

# LOGIN CHECK
if not st.session_state.logged_in:

    st.warning("Please login to access AI Dashboard")

    st.stop()




# # =========================
# # LOGIN SECTION
# # =========================

# st.sidebar.markdown("## 🔐 User Login")

# username = st.sidebar.text_input(
#     "👤 Username"
# )

# password = st.sidebar.text_input(
#     "🔑 Password",
#     type="password"
# )

# login_button = st.sidebar.button(
#     "Login"
# )

# if login_button:

#     if username == "admin" and password == "admin123":

#         st.sidebar.success(
#             "✅ Login Successful"
#         )

#     else:

#         st.sidebar.error(
#             "❌ Invalid Username or Password"
#         )

# =========================
# USER INPUTS
# =========================

st.sidebar.markdown("---")

st.sidebar.header(
    "🧾 Customer Input Parameters"
)

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
# TITLE SECTION
# =========================

# st.title(
#     "🧠 AI Decision Intelligence System"
# )

col_logo, col_title = st.columns([1, 12])

with col_logo:
    st.image("images/RobotAi.png", width=70)

with col_title:
    st.title("AI Decision Intelligence System")


st.subheader(
    "📊 Customer Churn Prediction Dashboard"
)

st.caption(
    f"Scikit-learn Version: {sklearn.__version__}"
)
# =========================
# HERO SECTION
# =========================

st.markdown("""
<div style="
    background: linear-gradient(
        90deg,
        rgba(124,58,237,0.25),
        rgba(59,130,246,0.20)
    );
    padding: 35px;
    border-radius: 24px;
    border: 1px solid rgba(168,85,247,0.30);
    margin-bottom: 30px;
    box-shadow: 0 0 30px rgba(124,58,237,0.25);
">

<div style="
    display:flex;
    justify-content:space-between;
    align-items:center;
">

<div>


<div style="
    display:flex;
    align-items:center;
    gap:18px;
    margin-bottom:15px;
">

<img src="https://cdn-icons-png.flaticon.com/512/4712/4712109.png"
width="55">

<h1 style="
    color:white;
    margin:0;
    font-size:42px;
    font-weight:800;
">
AI Decision Intelligence Platform
</h1>

</div>

<h3 style="
    color:#C4B5FD;
    margin-bottom:12px;
    font-size:28px;
    text-align:center;
   box-shadow: -5px 2px 21px 11px rgba(25, 165, 184, 0.43);
border-radius: 11px;
">
Real-Time Customer Churn Analytics System
</h3>

<p style="
    color:#E5E7EB;
    font-size:16px;
">
Powered by Machine Learning + Explainable AI + Business Intelligence
</p>

</div>

<div style="
    background: rgba(255,255,255,0.05);
    padding:25px;
    border-radius:20px;
    box-shadow: 5px 5px 15px 0px rgba(100, 7, 83, 0.22);
    border-radius: 8px;
    text-align:center;
    min-width:180px;
">

<h2 style="
    color:#A855F7;
    margin-bottom:10px;
  box-shadow: inset 5px 5px 20px 3px rgba(16, 140, 142, 0.22);
border-radius: 8px;
">
⚡ LIVE AI 

</h2>

<p style="
    color:white;
    font-size:16px;
">
Prediction Engine Active
</p>

</div>

</div>

</div>
""", unsafe_allow_html=True)

st.markdown("---")

# =========================
# KPI SECTION
# =========================

st.markdown(
    "## 📌 Key Performance Indicators"
)

total_customers = len(df)

high_risk = int(total_customers * 0.26)

revenue_impact = round(
    df["MonthlyCharges"].sum(),
    2
)

retention_rate = round(
    100 - ((high_risk / total_customers) * 100),
    2
)

col1, col2, col3, col4 = st.columns(4)

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

st.markdown("---")

# =========================
# INTERACTIVE ANALYTICS
# =========================

st.markdown(
    "## 📊 Interactive Business Analytics"
)

chart_col1, chart_col2 = st.columns(2)

with chart_col1:

    churn_counts = df["Churn"].value_counts()

    fig1 = px.pie(
        values=churn_counts.values,
        names=churn_counts.index,
        hole=0.5,
        title="Customer Churn Distribution",
        color_discrete_sequence=[
            "#7C3AED",
            "#06B6D4"
        ]
    )

    fig1.update_layout(
        paper_bgcolor="#111827",
        plot_bgcolor="#111827",
        font_color="white"
    )

    st.plotly_chart(
        fig1,
        width="stretch"
        
    )

with chart_col2:

    fig2 = px.histogram(
        df,
        x="MonthlyCharges",
        nbins=30,
        title="Monthly Charges Distribution",
        color_discrete_sequence=[
            "#A855F7"
        ]
    )

    fig2.update_layout(
        paper_bgcolor="#111827",
        plot_bgcolor="#111827",
        font_color="white"
    )

    st.plotly_chart(
        fig2,
        width="stretch"
    )

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
    st.write(f"🧓 Senior Citizen: {seniorcitizen}")
    st.write(f"💍 Partner: {partner}")

with profile_col2:

    st.write(f"👨‍👩‍👧 Dependents: {dependents}")
    st.write(f"📅 Tenure: {tenure} months")
    st.write(f"💳 Monthly Charges: ${monthlycharges}")

st.markdown("---")

# =========================
# CUSTOMER ANALYSIS
# =========================

st.markdown(
    "## 🚀 Customer Analysis"
)

if st.button(
    "🚀 Analyze Customer"
):

    input_data = pd.DataFrame({
        "tenure": [tenure],
        "MonthlyCharges": [monthlycharges],
        "TotalCharges": [totalcharges]
    })

    prediction = model.predict(
        input_data
    )

    probability = model.predict_proba(
        input_data
    )

    churn_probability = probability[0][1] * 100

    risk_value = int(churn_probability)

    st.info(
        f"🎯 Customer Risk Score: {churn_probability:.2f}%"
    )

    st.progress(
        risk_value
    )

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
# FOOTER
# =========================

# st.markdown("""
# <hr>
# <p style='text-align:center;color:#9CA3AF; 
# font-size:18px;
# color:#9CA3AF;
# letter-spacing:0.5px;'>
# © 2026 AI Decision Intelligence Platform | Developed by Jhanvi Pathak
# </p>
# """, unsafe_allow_html=True)
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