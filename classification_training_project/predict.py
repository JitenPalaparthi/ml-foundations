import joblib
import pandas as pd


def main():
    model = joblib.load("student_result_model.pkl")

    # New student data
    new_student = pd.DataFrame(
        [
            {
                "hours_studied": 3,
                "attendance_percent": 55,
                "previous_marks": 40,
                "assignment_score": 38
            },
            {
                "hours_studied": 8,
                "attendance_percent": 90,
                "previous_marks": 82,
                "assignment_score": 88
            }
        ]
    )

    prediction = model.predict(new_student)

    new_student["predicted_result"] = prediction

    print("\nPrediction result:")
    print(new_student)


if __name__ == "__main__":
    main()