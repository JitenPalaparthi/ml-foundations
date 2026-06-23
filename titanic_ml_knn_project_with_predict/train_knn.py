import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# --------------------------------------------------
# 1. Load offline Titanic CSV
# --------------------------------------------------
df = pd.read_csv("titanic.csv")

print("Dataset:")
print(df.head())

# --------------------------------------------------
# 2. Encode categorical columns manually
# male = 0, female = 1
# embarked_C = 0/1
# embarked_Q = 0/1
# embarked_S = 0/1
# --------------------------------------------------
df["sex"] = df["sex"].map({"male": 0, "female": 1})

df = pd.get_dummies(df, columns=["embarked"])

# Make sure all expected embarked columns exist
for col in ["embarked_C", "embarked_Q", "embarked_S"]:
    if col not in df.columns:
        df[col] = 0

# Keep fixed column order
feature_columns = [
    "pclass",
    "sex",
    "age",
    "sibsp",
    "parch",
    "fare",
    "embarked_C",
    "embarked_Q",
    "embarked_S",
]

X = df[feature_columns]
y = df["survived"]

# --------------------------------------------------
# 3. Train/test split
# --------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)

# --------------------------------------------------
# 4. Scale data
# KNN needs scaling because it uses distance
# --------------------------------------------------
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# --------------------------------------------------
# 5. Train KNN model
# --------------------------------------------------
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train_scaled, y_train)

# --------------------------------------------------
# 6. Evaluate
# --------------------------------------------------
y_pred = model.predict(X_test_scaled)

print("\nAccuracy:", accuracy_score(y_test, y_pred))
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# --------------------------------------------------
# 7. Save model, scaler, and feature order
# --------------------------------------------------
joblib.dump(model, "knn_titanic_model.pkl")
joblib.dump(scaler, "titanic_scaler.pkl")
joblib.dump(feature_columns, "feature_columns.pkl")

print("\nSaved files:")
print("knn_titanic_model.pkl")
print("titanic_scaler.pkl")
print("feature_columns.pkl")
