# Managing and Understanding Input Data

## Numeric Data and Nominal Data in Machine Learning

---

# Introduction

Machine Learning models learn patterns from data.

The quality and type of input data directly affect:

- Model accuracy
- Training speed
- Feature engineering
- Algorithm selection

Before building any model, we must understand the input data.

Input data generally falls into two major categories:

1. Numeric Data
2. Nominal Data

Understanding these data types is essential for proper preprocessing and algorithm selection.

---

# 1. What is Input Data?

Input data consists of features (independent variables) used by the model to make predictions.

Example:

House Price Dataset

| Area | Bedrooms | Location | Price |
|--------|-----------|------------|--------|
| 1200 | 2 | Urban | 50L |
| 1800 | 3 | Urban | 80L |
| 900 | 1 | Rural | 25L |

Features:

- Area
- Bedrooms
- Location

Target:

- Price

---

# 2. Types of Input Data

Machine Learning data can be classified into:

### Numeric Data

Contains numbers with measurable quantities.

### Categorical Data

Contains categories or labels.

Nominal data belongs to categorical data.

---

# 3. Numeric Data

Numeric data represents measurable values.

Arithmetic operations can be performed on numeric data.

Examples:

- Age
- Salary
- Height
- Weight
- Temperature
- House Area

---

## Example Dataset

| Age | Salary |
|-------|---------|
| 25 | 40000 |
| 30 | 60000 |
| 35 | 80000 |

Arithmetic operations are meaningful.

Example:

Average Age:

(25 + 30 + 35) / 3

= 30

---

# 4. Types of Numeric Data

Numeric data is further divided into:

1. Discrete Data
2. Continuous Data

---

# 5. Discrete Data

Countable values.

Usually integers.

Examples:

- Number of Bedrooms
- Number of Children
- Number of Employees
- Number of Cars

Example:

Bedrooms:

1, 2, 3, 4, 5

No intermediate values.

You cannot have:

2.5 bedrooms

---

# 6. Continuous Data

Can take any value within a range.

Examples:

- Height
- Weight
- Temperature
- House Area

Example:

Height:

170.5 cm
170.55 cm
170.555 cm

Infinite precision possible.

---

# 7. Characteristics of Numeric Data

Supports:

- Addition
- Subtraction
- Multiplication
- Division

Statistical Operations:

- Mean
- Median
- Mode
- Variance
- Standard Deviation

---

## Example

Salary Data

40000
50000
60000
70000

Mean:

(40000 + 50000 + 60000 + 70000) / 4

= 55000

---

# 8. Common Operations on Numeric Data

### Scaling

Convert values into a standard range.

### Normalization

Convert values between:

0 and 1

### Standardization

Transform values using:

(X - Mean) / Standard Deviation

---

## Why?

Features may have different scales.

Example:

Age = 30

Salary = 800000

Salary dominates distance calculations.

Scaling solves this issue.

---

# 9. What is Nominal Data?

Nominal data represents categories without any inherent order.

Values are labels only.

Examples:

- Gender
- Country
- City
- Color
- Product Category

---

## Example

| Gender |
|-----------|
| Male |
| Female |
| Male |
| Female |

These are labels.

Arithmetic operations are meaningless.

Male + Female

No meaning.

---

# 10. Characteristics of Nominal Data

Cannot perform:

- Addition
- Subtraction
- Multiplication
- Division

Can only:

- Group
- Count
- Compare

---

# 11. Examples of Nominal Data

### Gender

- Male
- Female

---

### Country

- India
- USA
- Germany

---

### Blood Group

- A
- B
- AB
- O

---

### Color

- Red
- Blue
- Green

---

# 12. Why Nominal Data Cannot Be Used Directly

Machine Learning algorithms work with numbers.

Example:

Gender:

Male
Female

Algorithm cannot process text directly.

Need encoding.

---

# 13. Label Encoding

Convert categories into numbers.

Example:

Male = 0

Female = 1

---

## Problem

The model may incorrectly assume:

Female > Male

Which is not true.

Therefore Label Encoding is not always suitable for nominal data.

---

# 14. One-Hot Encoding

Best approach for nominal data.

Example:

Gender

Male
Female

Becomes:

| Male | Female |
|---------|---------|
| 1 | 0 |
| 0 | 1 |

No ordering introduced.

---

# 15. Real Example

Original Dataset

| City |
|--------|
| Delhi |
| Mumbai |
| Chennai |

One-Hot Encoding

| Delhi | Mumbai | Chennai |
|----------|----------|----------|
| 1 | 0 | 0 |
| 0 | 1 | 0 |
| 0 | 0 | 1 |

---

# 16. Numeric vs Nominal Data

| Property | Numeric Data | Nominal Data |
|------------|-------------|-------------|
| Contains Numbers | Yes | No |
| Arithmetic Possible | Yes | No |
| Mean Calculation | Yes | No |
| Scaling Needed | Often | No |
| Encoding Needed | No | Yes |
| Examples | Age, Salary | Gender, City |

---

# 17. House Price Example

Dataset:

| Area | Bedrooms | Location | Price |
|---------|---------|----------|--------|
| 1200 | 2 | Urban | 50L |
| 1800 | 3 | Rural | 60L |

Numeric Features:

- Area
- Bedrooms

Nominal Feature:

- Location

---

## Preprocessing

Area:

Normalize or Standardize

Location:

One-Hot Encode

Urban = [1,0]

Rural = [0,1]

---

# 18. Algorithm Considerations

Some algorithms handle nominal data better.

### Decision Trees

Can work effectively with encoded categories.

---

### Random Forest

Handles mixed data well.

---

### XGBoost

Requires encoded categories.

---

### Linear Regression

Requires numerical inputs.

---

# 19. Common Mistakes

### Treating Nominal Data as Numeric

Bad:

Red = 1
Blue = 2
Green = 3

Model assumes:

Green > Blue > Red

Incorrect.

---

### Ignoring Scaling

Age = 30

Salary = 1000000

Salary dominates calculations.

Scale features properly.

---

# 20. Real-World Examples

### Employee Dataset

Numeric:

- Age
- Experience
- Salary

Nominal:

- Department
- Gender
- Location

---

### E-Commerce Dataset

Numeric:

- Product Price
- Quantity Sold

Nominal:

- Product Category
- Brand
- Color

---

# 21. Interview Questions

## Q1. What is Numeric Data?

Data representing measurable quantities.

Example:

Age, Salary, Height.

---

## Q2. What is Nominal Data?

Categorical data without any order.

Example:

Gender, City, Country.

---

## Q3. Why is One-Hot Encoding used?

To convert nominal data into numbers without introducing order.

---

## Q4. Why is Scaling important?

To prevent large-valued features from dominating smaller-valued features.

---

# 22. Quick Revision Table

| Data Type | Examples | Operations |
|------------|------------|------------|
| Numeric | Age, Salary, Height | Arithmetic |
| Discrete | Bedrooms, Children | Counting |
| Continuous | Weight, Area | Measurement |
| Nominal | Gender, City, Color | Categorization |

---

# Golden Rule

Before training any Machine Learning model:

1. Identify Numeric Features.
2. Identify Nominal Features.
3. Scale Numeric Data if needed.
4. Encode Nominal Data properly.
5. Verify data quality before training.

Good input data leads to better Machine Learning models.
