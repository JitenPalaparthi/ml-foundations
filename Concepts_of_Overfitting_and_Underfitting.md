# Concepts of Overfitting and Underfitting

## Introduction

One of the most important goals in Machine Learning is to build a model that can generalize well to unseen data.

A model should:

- Learn meaningful patterns from training data.
- Avoid memorizing the training data.
- Perform well on new data.

Two common problems are:

1. Underfitting
2. Overfitting

The ideal situation is called a Good Fit.

---

# 1. What is Underfitting?

Underfitting occurs when a model is too simple to learn the underlying patterns in the data.

The model fails to capture important relationships.

Result:

- Poor performance on training data.
- Poor performance on test data.

---

## Example

Suppose house prices depend on:

- Area
- Location
- Number of Bedrooms
- Age of House

But the model uses only:

Price = Area × Constant

Many important factors are ignored.

The model cannot learn the true relationship.

---

## Characteristics

- High Training Error
- High Testing Error
- Model is too simple
- Poor predictions

---

## Visual Representation

Training Data:

*
**
***
****
*****

Model:

-----------

The straight line does not follow the pattern.

---

## Causes of Underfitting

- Too little training time
- Too few features
- Oversimplified algorithm
- Excessive regularization

---

## Examples

- Using Linear Regression for highly complex data
- Using a shallow Decision Tree
- Using very few features

---

# 2. What is Overfitting?

Overfitting occurs when a model learns the training data too well.

Instead of learning patterns, it memorizes the training data including noise and outliers.

Result:

- Very low training error
- High testing error

---

## Example

Student memorizes answers from previous exams.

Can answer known questions perfectly.

Fails when new questions appear.

This is exactly what an overfitted model does.

---

## Characteristics

- Very low training error
- High test error
- Poor generalization
- Learns noise and outliers

---

## Visual Representation

Training Data:

*
**
***
****
*****

Model:

/\/\/\/\/\/\/\/\/\

The curve tries to pass through every point.

---

## Causes of Overfitting

- Too many features
- Small dataset
- Complex model
- Too many training iterations
- Deep decision trees

---

## Examples

- Deep Decision Trees
- Large Neural Networks
- High-degree Polynomial Regression

---

# 3. Good Fit (Ideal Model)

A good model captures the underlying trend without memorizing noise.

Characteristics:

- Low Training Error
- Low Testing Error
- Good Generalization

---

## Visual Representation

Training Data:

*
**
***
****
*****

Model:

/-----------/

Smooth curve following the trend.

---

# 4. Bias and Variance

Understanding Bias and Variance helps explain underfitting and overfitting.

---

## Bias

Bias is the error caused by incorrect assumptions.

High Bias:

- Model too simple
- Misses important relationships

Example:

Using a straight line for a curved relationship.

Underfitting = High Bias

---

## Variance

Variance measures how much the model changes when trained on different datasets.

High Variance:

- Model too sensitive
- Learns noise

Overfitting = High Variance

---

## Summary

| Situation | Bias | Variance |
|------------|--------|-----------|
| Underfitting | High | Low |
| Good Fit | Balanced | Balanced |
| Overfitting | Low | High |

---

# 5. Training Error vs Test Error

As model complexity increases:

Training Error:
- Continuously decreases

Test Error:
- Decreases initially
- Then starts increasing

This increase indicates overfitting.

---

## Typical Curve

Model Complexity --->

Training Error
\\
 \\
  \\
   \\

Test Error

 \\
  \\
   \\__
       \\
        \\

Lowest Test Error = Best Model

---

# 6. Real Example

Dataset:

House Price Prediction

Features:

- Area
- Bedrooms
- Age
- Location

---

## Underfitted Model

Uses only:

Area

Result:

Training Accuracy = 55%
Testing Accuracy = 50%

---

## Good Model

Uses:

- Area
- Bedrooms
- Age
- Location

Result:

Training Accuracy = 90%
Testing Accuracy = 88%

---

## Overfitted Model

Uses:

- Hundreds of derived features
- Deep decision tree

Result:

Training Accuracy = 100%
Testing Accuracy = 70%

---

# 7. How to Detect Underfitting

Signs:

- Poor training performance
- Poor testing performance
- Model unable to learn patterns

Solution:

- Increase features
- Increase model complexity
- Train longer

---

# 8. How to Detect Overfitting

Signs:

Training Accuracy = 99%

Testing Accuracy = 70%

Large gap between training and testing performance.

Solution:

- Reduce model complexity
- Increase training data
- Apply regularization
- Use cross-validation

---

# 9. Regularization

Regularization prevents overfitting.

It penalizes very complex models.

---

## L1 Regularization (Lasso)

Adds penalty:

Loss + λΣ|w|

Effects:

- Feature selection
- Reduces overfitting

---

## L2 Regularization (Ridge)

Adds penalty:

Loss + λΣ(w²)

Effects:

- Shrinks weights
- Prevents large coefficients

---

# 10. Cross Validation

Cross-validation evaluates model performance on multiple data splits.

Benefits:

- Detects overfitting
- More reliable evaluation

Most common:

K-Fold Cross Validation

---

# 11. Decision Tree Example

Tree Depth = 2

May underfit.

Tree Depth = 5

Often good fit.

Tree Depth = 50

Likely overfit.

---

# 12. Random Forest and Overfitting

Random Forest reduces overfitting by:

- Creating multiple trees
- Using random feature selection
- Using bootstrap sampling

Result:

Better generalization.

---

# 13. Neural Network Example

Too Few Neurons:

Underfitting

Appropriate Neurons:

Good Fit

Too Many Neurons:

Overfitting

---

# 14. Interview Questions

Q1. What is overfitting?

A model performs very well on training data but poorly on unseen data.

---

Q2. What is underfitting?

A model fails to learn patterns even from training data.

---

Q3. How do you detect overfitting?

Compare training and testing performance.

Large gap indicates overfitting.

---

Q4. How can overfitting be reduced?

- More data
- Regularization
- Pruning
- Cross-validation
- Simpler models

---

# 15. Quick Revision Table

| Aspect | Underfitting | Good Fit | Overfitting |
|----------|-------------|-----------|------------|
| Training Error | High | Low | Very Low |
| Test Error | High | Low | High |
| Bias | High | Balanced | Low |
| Variance | Low | Balanced | High |
| Generalization | Poor | Excellent | Poor |
| Complexity | Too Simple | Appropriate | Too Complex |

---

# Golden Rule

A model should learn patterns, not memorize data.

Goal:

Low Training Error + Low Testing Error

This balance produces a model that generalizes well to unseen data.
