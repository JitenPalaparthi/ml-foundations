import pandas as pd 

import matplotlib.pyplot as plt

df = pd.read_csv("train.csv")

print(df.shape) # (1460, 81)
print(df.head())

# understand the data

df.info()

missing = df.isnull().sum()

missing = missing[missing>0]

print(missing.sort_values(ascending=False))

# parcentage of missing values

missing_percent = (df.isnull().sum()/len(df))*100 #(missing/len)*100

missing_percent=missing_percent[missing_percent>0]

print(missing_percent.sort_values(ascending=False))

# what do you do with missing data
# >80% Drop the Column
# 30-80% Investigate
# <30% Fill Values

# drop the columns

df.drop(columns=["PoolQC","MiscFeature","Alley","Fence"],inplace=True)

print(">>>>>>>>")
print(df["MasVnrArea"].corr(df["SalePrice"])) # 0 - 1
print("<<<<<<<<")
print(df.shape)

print("max",df["LotFrontage"].max())
print("min:",df["LotFrontage"].min())
print("Mean:",df["LotFrontage"].mean())
print("median:",df["LotFrontage"].median())
print("std:",df["LotFrontage"].std())
    # print("median:",np.median(salary))
    # print("Min:",np.min(salary))
    # print("Max:",np.max(salary))
    # print("Std:",np.std(salary))

df["LotFrontage"]=(df["LotFrontage"].fillna(df["LotFrontage"].median()))

missing = df.isnull().sum()

missing = missing[missing>0]

print(missing.sort_values(ascending=False))

print(df["GarageType"])

df["GarageType"]=(df["GarageType"].fillna(df["GarageType"].mode()[0])) # fill with most frequent value

df.isnull().sum().sort_values(ascending=False).head(20)

# print(df["MasVnrType"].tolist(ascending=False)).head(20)

## details about the target varialbe , Label/ Dependent Variable/Outout Variable/Response Variable

# SalePrice = f(Area.....)

print("Saleprice",df["SalePrice"].describe())
print("median",df["SalePrice"].median())

avg=(df["SalePrice"]>300000).sum()/len(df)*100
print(avg)
# mean > median

# Distribution
df["SalePrice"].hist(bins=50)
#plt.show()


print(">>>>>>>>")

print(df["SalePrice"].skew())



print(">>>>>>>>")


import numpy as np

lst = [10, 100 ,20, 40, 80, 10000 ,100000, 20000 ,50, 60 ,200 ,300 ,500 ,200 ]

print("Mean:",np.mean(lst))
print("median:",np.median(lst))
print("Min:",np.min(lst))
print("Max:",np.max(lst))
print("Std:",np.std(lst))

# 10 20 40 50 60 80 100 200 200 300 500 10000 20000 100000

# 180921 - 79442= 101,xxx
# 180921 + 79442 = 260xxx

# skew 
# 0 Symmetric
# -.5 to .5 some what symmetric
# >1 Highly Skewed
# < -1 high skewed

df['SalePrice_log']=np.log1p(df['SalePrice'])
df['GrLivArea_log']=np.log1p(df['GrLivArea'])


#print(df['SalePrice_log'].tolist())

# 50,000
# 50,000,000

# 10.5 ---
# 17.5 ----

# log10(1000) = clear 
# 10 * 10 * 10 = 1000

# x = 10
# ln(10) = 2.3


print(df['GrLivArea_log'].describe())
# import seaborn as sns 

# sns.scatterplot(x='GrLivArea_log',y='SalePrice_log',data=df)
# plt.show()

print(df[['GrLivArea_log','SalePrice_log']].head())

## creating new variable

df["PricePerSqFt"]= df["SalePrice"]/df["GrLivArea"]

print(df[['SalePrice','GrLivArea',"PricePerSqFt"]].head(20))

print(df.head())
