import pandas as pd

# Demonstrating a Pandas Series
# Creating a Series from a list
data = [10, 20, 30, 40, 50]
series = pd.Series(data, index=['A', 'B', 'C', 'D', 'E'])
print("Pandas Series:")
print(series)
print()

# Accessing elements in the Series
print("Accessing elements in the Series:")
print("Element at index 'C':", series['C'])
print("First three elements:\n", series[:3])
print()

# Demonstrating a Pandas DataFrame
# Creating a DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 27, 22, 32],
    'Grade': ['A', 'B', 'C', 'A']
}
df = pd.DataFrame(data)
print("Pandas DataFrame:")
print(df)
print()

# Accessing DataFrame elements
print("Accessing elements in the DataFrame:")
print("Row 1:\n", df.iloc[1])  # Accessing the second row
print("Column 'Name':\n", df['Name'])  # Accessing the 'Name' column
print()

# Adding a new column to the DataFrame
df['Score'] = [85, 90, 75, 88]
print("DataFrame after adding a new column 'Score':")
print(df)
print()

# Filtering data in the DataFrame
print("Filtering students with grade 'A':")
print(df[df['Grade'] == 'A'])
print()

# Summary statistics of the DataFrame
print("Summary statistics of the DataFrame:")
print(df.describe())
