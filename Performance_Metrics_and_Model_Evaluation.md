# Performance Metrics and Model Evaluation

## Introduction
Performance Metrics and Model Evaluation help us measure how well a Machine Learning model performs on unseen data.

## Why Model Evaluation is Important
- Measure prediction quality
- Compare multiple models
- Detect overfitting
- Detect underfitting
- Select the best algorithm

## Regression Metrics

### Mean Absolute Error (MAE)
MAE = Average(|Actual - Predicted|)

### Mean Squared Error (MSE)
MSE = Average((Actual - Predicted)^2)

### Root Mean Squared Error (RMSE)
RMSE = sqrt(MSE)

### R-Squared (R²)
R² = 1 - (SSres / SStot)

Interpretation:
- 1.0 = Perfect
- 0.0 = No predictive power
- Negative = Worse than predicting the mean

## Classification Metrics

### Confusion Matrix

| | Predicted Positive | Predicted Negative |
|---|---|---|
| Actual Positive | TP | FN |
| Actual Negative | FP | TN |

### Accuracy
Accuracy = (TP + TN) / Total

### Precision
Precision = TP / (TP + FP)

### Recall
Recall = TP / (TP + FN)

### F1 Score
F1 = 2 × (Precision × Recall) / (Precision + Recall)

### ROC-AUC
Measures model discrimination capability across thresholds.

## Cross Validation

### 5-Fold Cross Validation
1. Split data into 5 folds
2. Train on 4 folds
3. Test on 1 fold
4. Repeat 5 times
5. Average the scores

## Training, Validation and Test Sets

Typical split:
- 70% Training
- 15% Validation
- 15% Testing

## Overfitting

Training Accuracy: 99%
Testing Accuracy: 65%

Model memorizes data and fails to generalize.

## Underfitting

Training Accuracy: 60%
Testing Accuracy: 58%

Model cannot learn useful patterns.

## Bias-Variance Tradeoff

### High Bias
- Underfitting
- Oversimplified model

### High Variance
- Overfitting
- Overly complex model

## Choosing the Right Metric

### Regression
- MAE
- RMSE
- R²

### Classification
- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC

## Summary
Performance metrics quantify model quality and help compare algorithms before deployment.
