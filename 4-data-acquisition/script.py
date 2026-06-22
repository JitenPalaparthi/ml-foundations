import pandas as pd 
import numpy as np
from csv import QUOTE_NONNUMERIC

def read_students():
    data = pd.read_csv("students.csv")
    print(data.head())

def read_employees():
    df = pd.read_csv("employees.csv")
    df = df.drop_duplicates() # data cleaning
    print(df.head())
    print(df.isnull().sum()) # missing values 
    df["name"]= df["name"].fillna("Unknown") # if name is NaN -> give it as unknown
    print(df.head())

    df=df[df["age"]<=110]
    print(df.head())

    # --- CONVERT SALARY TO NUMERIC ---
    # 1. Remove non-numeric characters like '$' and ',' 
    df["salary"] = df["salary"].astype(str).str.replace(r"[^\d.]", "", regex=True)
    # 2. Convert to numeric, turning unconvertible values into NaN
    df["salary"] = pd.to_numeric(df["salary"], errors="coerce")

    # Calculate mean (automatically skips NaN values)
    avg_sal = df["salary"].mean() 
    print(f"avg:{avg_sal}")  # Fixed: Added 'f' prefix for string formatting
    df["salary"]=df["salary"].fillna(avg_sal)
    print(df.head())

def get_basic_stats():
    salary = [15000,18000,20000,25000,30000,250000]
    print("Mean:",np.mean(salary))
    print("median:",np.median(salary))
    print("Min:",np.min(salary))
    print("Max:",np.max(salary))
    print("Std:",np.std(salary))

if __name__=="__main__":
    read_students()
    read_employees()
    get_basic_stats()


