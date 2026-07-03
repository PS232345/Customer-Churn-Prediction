# Customer Churn Analytics Dashboard

An interactive Streamlit dashboard for analyzing and predicting customer churn using the Telco Customer Churn dataset, powered by a trained Random Forest model.

<img width="1905" height="864" alt="Business Insight png" src="https://github.com/user-attachments/assets/9bffccfd-0f92-4265-beaf-ccc5f6e21356" />
<img width="1903" height="856" alt="Customer Churn Analysis png" src="https://github.com/user-attachments/assets/df4efaba-2d9b-4c07-95ea-76e2e33bb034" />
<img width="1904" height="861" alt="Executive Dashboard png" src="https://github.com/user-attachments/assets/864ae7be-a287-40cc-831c-5586b41907ee" />

---

## 📌 Overview

This project analyzes customer churn patterns for a telecom company and presents the findings through an interactive, multi-page Streamlit dashboard. It combines exploratory data analysis, visual analytics, and a pre-trained machine learning model to help identify why customers leave and what actions can reduce churn.

---

## ✨ Features

- **Executive Dashboard** — Key metrics (total customers, churn rate, average tenure, average monthly charges) with churn distribution and tenure visualizations
- **Churn Analysis** — Deep-dive charts on churn by contract type, payment method, internet service, and tenure vs. monthly charges
- **Business Insights** — Data-driven findings and actionable retention recommendations
- **ML Model Integration** — Loads a pre-trained Random Forest churn prediction model, scaler, and label encoders
- Clean, custom-styled UI with responsive metric cards

---

## 🗂️ Dataset

- **Source:** [Telco Customer Churn Dataset](https://www.kaggle.com/datasets/blastchar/telco-customer-churn) (IBM Sample Data)
- **File:** `Telco-Customer-Churn.csv`
- Contains customer demographics, account information, services subscribed, and churn status

---

## 🛠️ Tech Stack

| Category | Tools |
|---|---|
| Language | Python 3.11 |
| Dashboard/UI | Streamlit |
| Visualization | Plotly Express |
| Data Handling | pandas |
| Machine Learning | scikit-learn (Random Forest) |
| Model Persistence | joblib |

---

## 📊 Model

- **Algorithm:** Random Forest Classifier
- **Accuracy:** 80.2%
- **Artifacts used by the app:**
  - `customer_churn_model.pkl` — trained classifier
  - `scaler.pkl` — feature scaler
  - `label_encoders.pkl` — categorical encoders

> The app runs even without these model files — it will display an "Model Files Not Found" notice on the dashboard and the EDA pages remain fully functional.

---

## 📁 Project Structure

```
Customer Churn Analytics Dashboard/
│
├── app.py                          # main Streamlit application
├── Telco-Customer-Churn.csv        # dataset
├── customer_churn_model.pkl        # trained Random Forest model
├── scaler.pkl                      # feature scaler
├── label_encoders.pkl              # categorical label encoders
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

```bash
# Clone the repository
git clone https://github.com/<your-username>/customer-churn-analytics-dashboard.git
cd customer-churn-analytics-dashboard

# Create a virtual environment
python -m venv .venv
.venv\Scripts\activate      # Windows
source .venv/bin/activate   # macOS/Linux

# Install dependencies
pip install -r requirements.txt
```

### requirements.txt
```
streamlit
pandas
plotly
scikit-learn
joblib
```

---

## ▶️ Usage

1. Place `Telco-Customer-Churn.csv` in the project root.
2. (Optional) Add `customer_churn_model.pkl`, `scaler.pkl`, and `label_encoders.pkl` for full model-status display.
3. Run the app:
   ```bash
   streamlit run app.py
   ```
4. The dashboard opens in your browser with three pages accessible from the sidebar:
   - **Executive Dashboard**
   - **Churn Analysis**
   - **Business Insights**

---

## 📈 Key Insights

- **Contract Type:** Month-to-month customers churn the most; long-term contracts improve retention
- **Tenure:** Newer customers are more likely to churn than long-tenured ones
- **Monthly Charges:** Higher charges correlate with higher churn probability
- **Payment Method:** Electronic check users show elevated churn rates

**Recommendations:** Offer long-term contract discounts, build retention programs for new customers, and monitor high-paying customers proactively.

---

## 🚀 Future Improvements

- Add live churn prediction form (input customer details → get real-time prediction)
- Deploy on Streamlit Community Cloud
- Add model explainability (SHAP/feature importance) to the dashboard
- Experiment with additional models (XGBoost, Logistic Regression) for comparison
- Add filters (date range, customer segment) for interactive slicing

---

## 👤 Author

**Prachi Sable**
B.E. Artificial Intelligence & Data Science, GSMCOE, Pune

---

## 📄 License

This project is licensed under the MIT License.
