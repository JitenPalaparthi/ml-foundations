import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


def main():
    # 1. Load training data
    df = pd.read_csv("student_pass_fail.csv")

    print("\nFirst 5 records:")
    print(df.head())

    print("\nDataset shape:")
    print(df.shape)

    print("\nMissing values:")
    print(df.isnull().sum())

    # 2. Separate input features and target label
    X = df[
        [
            "hours_studied",
            "attendance_percent",
            "previous_marks",
            "assignment_score"
        ]
    ]

    y = df["result"]

    # 3. Split data into training and testing data
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.25,
        random_state=42,
        stratify=y
    )

    # 4. Create classification model
    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    # 5. Train the model
    model.fit(X_train, y_train)

    # 6. Test the model
    y_pred = model.predict(X_test)

    # 7. Evaluate the model
    print("\nAccuracy:")
    print(accuracy_score(y_test, y_pred))

    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))

    # 8. Save trained model
    joblib.dump(model, "student_result_model.pkl")
    print("\nModel saved as student_result_model.pkl")


if __name__ == "__main__":
    main()