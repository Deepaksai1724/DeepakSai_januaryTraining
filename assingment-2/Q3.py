#QUESTION-3
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OrdinalEncoder
df = pd.read_csv(r"C:\Users\graju\OneDrive\Documents\AENEXZ\indian_engineering_student_placement.csv")
cat_cols = df.select_dtypes(include=["object"]).columns

# 1. One-Hot Encoding
df_onehot = pd.get_dummies(df, columns=cat_cols, drop_first=True)

# 2. Label Encoding
le = LabelEncoder()
df_label = df.copy()
for col in cat_cols:
    df_label[col] = le.fit_transform(df_label[col])

# 3. Ordinal Encoding 
ordinal_cols = ["family_income_level", "extracurricular_involvement"]

ordinal_mapping = [
    ["Low", "Medium", "High"],
    ["Low", "Medium", "High"]
]

oe = OrdinalEncoder(categories=ordinal_mapping)
df[ordinal_cols] = oe.fit_transform(df[ordinal_cols])

# 4. Frequency Encoding
df_freq = df.copy()
for col in cat_cols:
    freq = df_freq[col].value_counts()
    df_freq[col] = df_freq[col].map(freq)

# 5. Target Encoding (example using placement status)
if "placed" in df.columns:
    df_target = df.copy()
    for col in cat_cols:
        mean_map = df.groupby(col)["placed"].mean()
        df_target[col] = df[col].map(mean_map)

print("Categorical Encoding Completed!")
