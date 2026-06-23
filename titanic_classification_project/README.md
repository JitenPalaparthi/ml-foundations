# Titanic Classification Project

This is a ready-to-run Titanic survival classification project.

It predicts whether a passenger survived or not.

## Files

- `titanic_train.csv` - Titanic-style training dataset
- `train_titanic_model.py` - trains the model
- `predict_titanic.py` - predicts new passengers
- `requirements.txt` - Python packages

## Install

```bash
pip install -r requirements.txt
```

## Train

```bash
python train_titanic_model.py
```

This creates:

```text
titanic_survival_model.pkl
```

## Predict

```bash
python predict_titanic.py
```

## Target Column

```text
Survived
```

Meaning:

```text
0 = Did not survive
1 = Survived
```

## Features Used

- Pclass
- Sex
- Age
- SibSp
- Parch
- Fare
- Embarked

## ML Type

This is a classification problem because the output is a class/category:

```text
Survived / Did not survive
```

## Notes

This package contains a compact Titanic-style dataset for offline practice.
You can replace `titanic_train.csv` with the full Kaggle Titanic `train.csv` later.
