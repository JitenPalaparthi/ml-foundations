Titanic KNN Offline Project With Prediction

Files:
1. titanic.csv
   Offline Titanic-style training data.

2. train_knn.py
   Trains the KNN model and saves:
   - knn_titanic_model.pkl
   - titanic_scaler.pkl
   - feature_columns.pkl

3. predict.py
   Loads the saved model and predicts survival for a new passenger.

Install:
    pip install pandas scikit-learn joblib

Run training first:
    python train_knn.py

Then run prediction:
    python predict.py

Important:
KNN uses distance, so scaling is very important.
That is why train_knn.py saves titanic_scaler.pkl.
predict.py must use the same scaler.

Change prediction input:
Open predict.py and modify this block:

new_passenger = {
    "pclass": 1,
    "sex": "female",
    "age": 25,
    "sibsp": 0,
    "parch": 0,
    "fare": 100.0,
    "embarked": "C"
}

Column meanings:
survived:
    0 = Did Not Survive
    1 = Survived

pclass:
    1 = First class
    2 = Second class
    3 = Third class

sex:
    male or female

age:
    Passenger age

sibsp:
    Number of siblings/spouse aboard

parch:
    Number of parents/children aboard

fare:
    Ticket fare

embarked:
    C = Cherbourg
    Q = Queenstown
    S = Southampton
