import pandas as pd

# Load dataset
df = pd.read_csv('data/student_data.csv')

# Display first 5 rows
print("First 5 rows:")
print(df.head())

# Dataset info
print("\nDataset Info:")
print(df.info())

# Summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Group analysis
print("\nAverage scores by gender:")
print(df.groupby('gender')[['math_score', 'reading_score', 'writing_score']].mean())







