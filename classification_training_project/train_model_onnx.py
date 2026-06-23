import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from skl2onnx import convert_sklearn
from skl2onnx.common.data_types import FloatTensorType

FEATURES = [
    "hours_studied",
    "attendance_percent",
    "previous_marks",
    "assignment_score",
]

def main():
    df = pd.read_csv("student_pass_fail.csv")

    X = df[FEATURES].astype("float32")
    y = df["result"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
    print("Report:\n", classification_report(y_test, y_pred))

    joblib.dump(model, "student_result_model.pkl")

    initial_type = [("float_input", FloatTensorType([None, 4]))]

    onnx_model = convert_sklearn(
        model,
        initial_types=initial_type,
        options={id(model): {"zipmap": False}}
    )

    with open("student_result_model.onnx", "wb") as f:
        f.write(onnx_model.SerializeToString())

    print("Saved: student_result_model.onnx")

if __name__ == "__main__":
    main()