import pandas as pd
import joblib

# --------------------------------------------------
# 1. Load saved model, scaler, and feature columns
# --------------------------------------------------
model = joblib.load("knn_titanic_model.pkl")
scaler = joblib.load("titanic_scaler.pkl")
feature_columns = joblib.load("feature_columns.pkl")

# --------------------------------------------------
# 2. New passenger input
# Change these values and run again
# --------------------------------------------------
new_passenger = {
    "pclass": 1,
    "sex": "female",
    "age": 25,
    "sibsp": 0,
    "parch": 0,
    "fare": 100.0,
    "embarked": "C"
}

# --------------------------------------------------
# 3. Convert new passenger into DataFrame
# --------------------------------------------------
df = pd.DataFrame([new_passenger])

# Encode sex
df["sex"] = df["sex"].map({"male": 0, "female": 1})

# One-hot encode embarked manually
df["embarked_C"] = 1 if new_passenger["embarked"] == "C" else 0
df["embarked_Q"] = 1 if new_passenger["embarked"] == "Q" else 0
df["embarked_S"] = 1 if new_passenger["embarked"] == "S" else 0

# Select same feature order used during training
X_new = df[feature_columns]

print("Input used for prediction:")
print(X_new)

# --------------------------------------------------
# 4. Scale input
# Important: use the same scaler saved from training
# --------------------------------------------------
X_new_scaled = scaler.transform(X_new)

# --------------------------------------------------
# 5. Predict
# --------------------------------------------------
prediction = model.predict(X_new_scaled)
probability = model.predict_proba(X_new_scaled)

print("\nPrediction Result:")

if prediction[0] == 1:
    print("Survived")
else:
    print("Did Not Survive")

print("\nPrediction Probability:")
print("Did Not Survive:", probability[0][0])
print("Survived:", probability[0][1])
