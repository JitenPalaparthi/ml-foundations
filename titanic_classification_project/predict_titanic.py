import pandas as pd
import joblib


def main():
    model = joblib.load("titanic_survival_model.pkl")

    new_passengers = pd.DataFrame([
        {
            "Pclass": 1,
            "Sex": "female",
            "Age": 25,
            "SibSp": 0,
            "Parch": 0,
            "Fare": 100,
            "Embarked": "C"
        },
        {
            "Pclass": 3,
            "Sex": "male",
            "Age": 30,
            "SibSp": 0,
            "Parch": 0,
            "Fare": 8,
            "Embarked": "S"
        }
    ])

    predictions = model.predict(new_passengers)
    probabilities = model.predict_proba(new_passengers)

    new_passengers["Prediction"] = predictions
    new_passengers["Prediction_Label"] = new_passengers["Prediction"].map({
        0: "Did not survive",
        1: "Survived"
    })
    new_passengers["Survival_Probability"] = probabilities[:, 1]

    print("\nPrediction result:")
    print(new_passengers)


if __name__ == "__main__":
    main()

    #  0 1
    # [5 0] 0
    # [2 3] 1

    #   [5 0]
    #   [0 5]