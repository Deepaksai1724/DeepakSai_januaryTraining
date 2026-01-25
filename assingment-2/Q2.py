#QUESTION-2
import numpy as np
import pandas as pd
df = pd.read_csv(r"C:\Users\graju\OneDrive\Documents\AENEXZ\indian_engineering_student_placement.csv")
# 1. Handling Missing Values
num_cols = df.select_dtypes(include=["int64", "float64"]).columns
cat_cols = df.select_dtypes(include=["object"]).columns
for col in num_cols:
    df[col].fillna(df[col].median(), inplace=True)
for col in cat_cols:
    df[col].fillna(df[col].mode()[0], inplace=True)
# 2. Fix incorrect data types
for col in num_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")
# 3. Detect and treat outliers using IQR
for col in num_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    df[col] = np.clip(df[col], lower, upper)
# 4. Remove duplicate records
df = df.drop_duplicates()
# 5. Drop irrelevant features
if "Student_ID" in df.columns:
    df.drop("Student_ID", axis=1, inplace=True)

print("Data Cleaning Completed")
print("Final Shape:", df.shape)
