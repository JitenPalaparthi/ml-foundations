# Classification Training Project

This project trains a machine learning classification model to predict whether a student will Pass or Fail.

## Files

- `student_pass_fail.csv` - training dataset
- `train_model.py` - trains and saves the model
- `predict.py` - loads saved model and predicts new students
- `requirements.txt` - required Python packages

## Setup

```bash
pip install -r requirements.txt
```

## Train the model

```bash
python train_model.py
```

This creates:

```text
student_result_model.pkl
```

## Predict new data

```bash
python predict.py
```

## Dataset columns

| Column | Meaning |
|---|---|
| hours_studied | Number of hours studied |
| attendance_percent | Attendance percentage |
| previous_marks | Previous exam marks |
| assignment_score | Assignment score |
| result | Target label: Pass or Fail |

## ML Type

This is a classification problem because the output is a category:

```text
Pass or Fail
```
