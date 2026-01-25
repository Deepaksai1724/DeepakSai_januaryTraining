#QUESTION-1
import pandas as pd
df = pd.read_csv(r"C:\Users\graju\OneDrive\Documents\AENEXZ\indian_engineering_student_placement.csv")
# Display basic info
print("Shape of dataset:", df.shape)
print("\nColumn names:\n", df.columns)
print(df.info())
print(df.head())
