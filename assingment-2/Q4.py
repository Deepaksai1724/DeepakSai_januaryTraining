#QUESTION-4
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, MaxAbsScaler, StandardScaler, Normalizer
df = pd.read_csv(r"C:\Users\graju\OneDrive\Documents\AENEXZ\indian_engineering_student_placement.csv")
num_cols = df.select_dtypes(include=["int64", "float64"]).columns

# 1. Min-Max Scaling
minmax = MinMaxScaler()
df_minmax = df.copy()
df_minmax[num_cols] = minmax.fit_transform(df_minmax[num_cols])

# 2. Max Absolute Scaling
maxabs = MaxAbsScaler()
df_maxabs = df.copy()
df_maxabs[num_cols] = maxabs.fit_transform(df_maxabs[num_cols])

# 3. Vector Normalization
normalizer = Normalizer()
df_normalized = df.copy()
df_normalized[num_cols] = normalizer.fit_transform(df_normalized[num_cols])

# 4. Z-score Standardization
scaler = StandardScaler()
df_standardized = df.copy()
df_standardized[num_cols] = scaler.fit_transform(df_standardized[num_cols])

print("Feature Scaling Completed!")
