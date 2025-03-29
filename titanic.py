import pandas as pd  

# Load the dataset
df = pd.read_csv("Titanic-Dataset.csv")  # Ensure the file is in the same directory as this script

# Display first 5 rows
print("First 5 rows of the dataset:")
print(df.head())

# Display dataset info
print("\nDataset Info:")
print(df.info())

# Display summary statistics
print("\nSummary Statistics:")
print(df.describe())
# Check for missing values
print("\nMissing Values in Each Column:")
print(df.isnull().sum())
# Fill missing 'Age' values with median
df['Age'].fillna(df['Age'].median(), inplace=True)

# Drop 'Cabin' column (too many missing values)
df.drop(columns=['Cabin'], inplace=True)

# Fill missing 'Embarked' values with the most common value (mode)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

# Check if there are still missing values
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())
C: