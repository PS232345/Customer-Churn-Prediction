import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# =====================================
# LOAD DATASET
# =====================================

df = pd.read_csv("Telco-Customer-Churn.csv")

print("Dataset Loaded Successfully!")
print("Shape:", df.shape)

# =====================================
# DATA CLEANING
# =====================================

# Remove customerID column
if "customerID" in df.columns:
    df.drop("customerID", axis=1, inplace=True)

# Convert TotalCharges to numeric
df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"],
    errors="coerce"
)

# Fill missing values
df["TotalCharges"] = df["TotalCharges"].fillna(
    df["TotalCharges"].median()
)

# =====================================
# ENCODE ALL OBJECT COLUMNS
# =====================================

label_encoders = {}

object_columns = df.select_dtypes(include=["object"]).columns

print("\nObject Columns Found:")
print(object_columns)

for column in object_columns:

    le = LabelEncoder()

    df[column] = le.fit_transform(
        df[column].astype(str)
    )

    label_encoders[column] = le

# =====================================
# VERIFY ENCODING
# =====================================

print("\nRemaining Object Columns:")
print(df.select_dtypes(include=["object"]).columns)

# =====================================
# FEATURES & TARGET
# =====================================

X = df.drop("Churn", axis=1)
y = df["Churn"]

# =====================================
# FEATURE SCALING
# =====================================

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

# =====================================
# TRAIN TEST SPLIT
# =====================================

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# =====================================
# MODEL TRAINING
# =====================================

model = RandomForestClassifier(
    n_estimators=300,
    max_depth=10,
    random_state=42
)

model.fit(X_train, y_train)

# =====================================
# PREDICTIONS
# =====================================

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy:", round(accuracy * 100, 2), "%")

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# =====================================
# SAVE FILES
# =====================================

joblib.dump(
    model,
    "customer_churn_model.pkl"
)

joblib.dump(
    scaler,
    "scaler.pkl"
)

joblib.dump(
    label_encoders,
    "label_encoders.pkl"
)

print("\nModel Saved Successfully!")
print("customer_churn_model.pkl")
print("scaler.pkl")
print("label_encoders.pkl")