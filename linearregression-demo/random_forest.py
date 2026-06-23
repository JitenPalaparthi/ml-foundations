import pandas as pd
import numpy as np 
from sklearn.ensemble import RandomForestRegressor  # Changed from LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# 1. Load the data 
df = pd.read_csv("train.csv")

print("Shape:", df.shape)
print(df.head())

# 2. Take the feature sets 
features = ["GrLivArea", "BedroomAbvGr", "TotalBsmtSF", "FullBath", "GarageCars"] 
target = "SalePrice" 

data = df[features + [target]] 

print("Shape:", data.shape)
print(data.head())

# 3. Check missing values
print("\nMissing values:")
print(data.isnull().sum())

# 4. Fill missing values
data = data.fillna(data.median())

# 5. Separate input X and output y 
X = data[features]
y = data[target]

# 6. Split into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Training rows:", X_train.shape[0])
print("Testing rows:", X_test.shape[0])

# 7. Create a model
# Added n_estimators (number of trees) and random_state for consistency
model = RandomForestRegressor(n_estimators=100, random_state=42)

# 8. Train the model
model.fit(X_train, y_train)

# 9. Test model
y_pred = model.predict(X_test)

# 10. Evaluate the model 
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("\nModel Performance")
print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)
print("R2:", r2)

# 11. Show feature importances
# Random Forest uses feature importances instead of linear coefficients
print("\nFeature Importances")
for col, importance in zip(features, model.feature_importances_):
    print(f"{col}: {importance:.4f}")

# 12. Predict a new house
new_house = pd.DataFrame({
"GrLivArea":[1800],
"BedroomAbvGr":[3],
"TotalBsmtSF":[900],
"FullBath":[2],
"GarageCars":[2]
})

# Make the prediction
predicted_price = model.predict(new_house)
print(f"\nPredicted Sale Price for the new house: ${predicted_price[0]:,.2f}")

