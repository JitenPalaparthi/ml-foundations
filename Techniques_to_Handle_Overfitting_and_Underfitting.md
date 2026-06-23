# Techniques to Handle Overfitting and Underfitting

## Introduction

In Machine Learning, the goal is to create a model that performs well on both training data and unseen data.

Two common problems are:

1. Underfitting
2. Overfitting

This document explains how to identify and handle both problems.

---

# 1. Understanding Underfitting

Underfitting occurs when a model is too simple to learn the underlying patterns in the data.

Characteristics:

- High training error
- High testing error
- Poor accuracy
- High bias

---

## Example

Predicting house prices using only:

Price = Area × Constant

Ignoring:

- Location
- Bedrooms
- Age
- Amenities

The model cannot learn the actual relationship.

---

# 2. Understanding Overfitting

Overfitting occurs when a model learns training data too well.

It memorizes:

- Patterns
- Noise
- Outliers

Characteristics:

- Very low training error
- High testing error
- Poor generalization
- High variance

---

## Example

A decision tree with 100 levels.

It perfectly memorizes training records but performs poorly on new data.

---

# 3. Identifying Underfitting and Overfitting

| Situation | Training Accuracy | Testing Accuracy |
|------------|------------------|------------------|
| Underfitting | Low | Low |
| Good Fit | High | High |
| Overfitting | Very High | Low |

---

# 4. Techniques to Handle Underfitting

Underfitting means the model is too simple.

Solution:

Increase learning capability.

---

## Technique 1: Increase Model Complexity

Example:

Instead of:

Linear Regression

Use:

- Polynomial Regression
- Decision Tree
- Random Forest
- XGBoost

Reason:

Complex models can learn more patterns.

---

## Technique 2: Add More Features

Bad Features:

- Area

Better Features:

- Area
- Bedrooms
- Bathrooms
- Age
- Location

More relevant information improves learning.

---

## Technique 3: Reduce Regularization

Excessive regularization can make the model too simple.

Example:

Very high Lambda (λ)

Result:

Weights become too small.

Solution:

Decrease Lambda.

---

## Technique 4: Train Longer

Common in Neural Networks.

Insufficient epochs can cause underfitting.

Example:

Training stopped at 5 epochs.

Try:

- 50 epochs
- 100 epochs

Monitor validation loss.

---

## Technique 5: Feature Engineering

Create useful derived features.

Example:

PricePerSqFt = Price / Area

AgeGroup = CurrentYear - BuiltYear

Better features improve model performance.

---

## Technique 6: Reduce Noise Removal

Sometimes aggressive preprocessing removes useful information.

Example:

Removing too many features.

Solution:

Retain informative attributes.

---

# 5. Techniques to Handle Overfitting

Overfitting means the model is too complex.

Solution:

Reduce complexity and improve generalization.

---

## Technique 1: More Training Data

More data reduces memorization.

Example:

100 Samples → High Overfitting

10000 Samples → Better Generalization

---

## Technique 2: L1 Regularization (Lasso)

Formula:

Loss + λΣ|w|

Benefits:

- Removes unnecessary features
- Produces sparse models

---

## Technique 3: L2 Regularization (Ridge)

Formula:

Loss + λΣ(w²)

Benefits:

- Shrinks weights
- Reduces variance

---

## Technique 4: Elastic Net

Combines:

- L1
- L2

Benefits:

- Feature selection
- Weight shrinkage

---

## Technique 5: Cross Validation

Use:

K-Fold Cross Validation

Benefits:

- Detects overfitting
- Better model evaluation

---

## Technique 6: Early Stopping

Used in Neural Networks.

Stop training when:

Validation Loss starts increasing.

Example:

Epoch 10 → Validation Loss = 0.12

Epoch 20 → Validation Loss = 0.09

Epoch 30 → Validation Loss = 0.14

Stop at Epoch 20.

---

## Technique 7: Dropout

Randomly disables neurons during training.

Example:

100 neurons

Dropout = 50%

Only 50 neurons active each iteration.

Benefits:

- Prevents neuron dependency
- Improves generalization

---

## Technique 8: Data Augmentation

Generate additional training samples.

Image Examples:

- Rotation
- Zoom
- Flip
- Brightness Change

Benefits:

- More data
- Less overfitting

---

## Technique 9: Tree Pruning

Used in Decision Trees.

Remove unnecessary branches.

Benefits:

- Simpler tree
- Better generalization

---

## Technique 10: Reduce Model Complexity

Instead of:

Depth = 50

Use:

Depth = 5

Benefits:

- Less memorization
- Better test performance

---

## Technique 11: Feature Selection

Remove irrelevant features.

Benefits:

- Lower variance
- Faster training
- Better generalization

---

# 6. Random Forest Against Overfitting

Random Forest reduces overfitting through:

- Bootstrap Sampling
- Random Feature Selection
- Multiple Trees

Result:

Lower variance.

---

# 7. XGBoost Against Overfitting

XGBoost provides:

- L1 Regularization
- L2 Regularization
- Learning Rate Control
- Tree Depth Control

This helps prevent overfitting.

---

# 8. Neural Network Solutions

### Underfitting

Increase:

- Hidden Layers
- Neurons
- Epochs

---

### Overfitting

Use:

- Dropout
- Early Stopping
- L2 Regularization
- Data Augmentation

---

# 9. Bias and Variance Relationship

## Underfitting

High Bias
Low Variance

---

## Overfitting

Low Bias
High Variance

---

## Goal

Balanced Bias and Variance

This produces the best generalization.

---

# 10. Real House Price Example

Features:

- Area
- Bedrooms
- Bathrooms
- Age
- Location

---

## Underfitting Model

Linear Regression

Training Accuracy:

60%

Testing Accuracy:

58%

Solution:

Use Random Forest.

---

## Overfitting Model

Decision Tree Depth = 100

Training Accuracy:

100%

Testing Accuracy:

72%

Solution:

Prune tree or use Random Forest.

---

## Good Fit

Random Forest Depth = 10

Training Accuracy:

92%

Testing Accuracy:

89%

---

# 11. Decision Guide

If Training Accuracy Low
AND Testing Accuracy Low

→ Underfitting

Actions:

- Add Features
- Increase Complexity
- Train Longer

---

If Training Accuracy High
AND Testing Accuracy Low

→ Overfitting

Actions:

- Regularization
- More Data
- Feature Selection
- Cross Validation

---

# 12. Quick Revision Table

| Problem | Symptoms | Solution |
|-----------|-----------|-----------|
| Underfitting | Low Train, Low Test Accuracy | Increase Complexity |
| Underfitting | Too Few Features | Add Features |
| Underfitting | High Bias | Complex Model |
| Overfitting | High Train, Low Test Accuracy | Regularization |
| Overfitting | High Variance | More Data |
| Overfitting | Deep Trees | Pruning |
| Overfitting | Large Neural Network | Dropout |

---

# 13. Interview Questions

## Q1. How do you identify underfitting?

Training and testing errors are both high.

---

## Q2. How do you identify overfitting?

Training error is low but testing error is high.

---

## Q3. What is the best technique to reduce overfitting?

- More data
- Regularization
- Cross Validation
- Early Stopping

---

## Q4. How can underfitting be fixed?

- Increase model complexity
- Add features
- Train longer

---

# Golden Rule

Underfitting:
Model is too simple.

Overfitting:
Model is too complex.

Goal:

Find the balance where the model learns patterns without memorizing noise.
