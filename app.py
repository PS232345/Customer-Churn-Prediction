import streamlit as st
import pandas as pd
import plotly.express as px
import joblib

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="Customer Churn Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

# =====================================
# CUSTOM CSS
# =====================================

st.markdown("""
<style>

.main {
    background-color: #F8FAFC;
}

div[data-testid="metric-container"]{
    background:white;
    border:1px solid #E2E8F0;
    padding:20px;
    border-radius:15px;
    box-shadow:0px 4px 12px rgba(0,0,0,0.08);
}

h1,h2,h3{
    color:#1E293B;
}

</style>
""", unsafe_allow_html=True)

# =====================================
# LOAD DATA
# =====================================

df = pd.read_csv("Telco-Customer-Churn.csv")

df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"],
    errors="coerce"
)

df["TotalCharges"] = df["TotalCharges"].fillna(
    df["TotalCharges"].median()
)

# =====================================
# LOAD MODEL FILES
# =====================================

try:
    model = joblib.load("customer_churn_model.pkl")
    scaler = joblib.load("scaler.pkl")
    label_encoders = joblib.load("label_encoders.pkl")
    model_loaded = True
except:
    model_loaded = False

# =====================================
# SIDEBAR
# =====================================

st.sidebar.title("📌 Navigation")

page = st.sidebar.radio(
    "Select Page",
    [
        "Executive Dashboard",
        "Churn Analysis",
        "Business Insights"
    ]
)

# =====================================
# EXECUTIVE DASHBOARD
# =====================================

if page == "Executive Dashboard":

    st.title("📊 Customer Churn Analytics Dashboard")

    total_customers = len(df)

    churn_customers = len(
        df[df["Churn"] == "Yes"]
    )

    churn_rate = round(
        churn_customers / total_customers * 100,
        2
    )

    avg_tenure = round(
        df["tenure"].mean(),
        1
    )

    avg_monthly = round(
        df["MonthlyCharges"].mean(),
        2
    )

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Total Customers",
        f"{total_customers:,}"
    )

    c2.metric(
        "Churn Rate",
        f"{churn_rate}%"
    )

    c3.metric(
        "Average Tenure",
        avg_tenure
    )

    c4.metric(
        "Avg Monthly Charges",
        f"${avg_monthly}"
    )

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:

        fig = px.pie(
            df,
            names="Churn",
            title="Customer Churn Distribution"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with col2:

        fig = px.histogram(
            df,
            x="tenure",
            title="Customer Tenure Distribution"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    st.markdown("---")

    st.subheader("🤖 Model Status")

    if model_loaded:
        st.success(
            "Random Forest Model Loaded Successfully"
        )

        st.info(
            "Model Accuracy: 80.2%"
        )

    else:
        st.error(
            "Model Files Not Found"
        )

# =====================================
# CHURN ANALYSIS
# =====================================

elif page == "Churn Analysis":

    st.title("📉 Customer Churn Analysis")

    fig1 = px.histogram(
        df,
        x="Contract",
        color="Churn",
        barmode="group",
        title="Churn by Contract Type"
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

    fig2 = px.histogram(
        df,
        x="PaymentMethod",
        color="Churn",
        barmode="group",
        title="Churn by Payment Method"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    fig3 = px.histogram(
        df,
        x="InternetService",
        color="Churn",
        barmode="group",
        title="Churn by Internet Service"
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

    fig4 = px.scatter(
        df,
        x="tenure",
        y="MonthlyCharges",
        color="Churn",
        title="Tenure vs Monthly Charges"
    )

    st.plotly_chart(
        fig4,
        use_container_width=True
    )

# =====================================
# BUSINESS INSIGHTS
# =====================================

elif page == "Business Insights":

    st.title("📌 Business Insights")

    st.info("""
    Key Findings from Customer Churn Analysis
    """)

    st.markdown("""
    ### 🔹 Contract Type

    - Month-to-Month customers show highest churn.
    - Long-term contracts improve retention.

    ### 🔹 Customer Tenure

    - New customers are more likely to churn.
    - Long tenure customers are more loyal.

    ### 🔹 Monthly Charges

    - High monthly charges increase churn probability.

    ### 🔹 Payment Method

    - Electronic Check users show higher churn rates.

    ### 🔹 Business Recommendation

    - Offer discounts for long-term contracts.
    - Create retention programs for new customers.
    - Monitor high monthly charge customers.
    """)

    st.success("""
    Strategic Goal:
    Reduce churn rate through targeted retention campaigns.
    """)