import pandas as pd

# Creating a Data Series
data_series = pd.Series([10, 20, 30, 40, 50], index=['A', 'B', 'C', 'D', 'E'])
print("Data Series:")
print(data_series)

# Creating a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
data_frame = pd.DataFrame(data)
print("\nDataFrame:")
print(data_frame)

# Accessing a specific column
print("\nAccessing 'Name' column:")
print(data_frame['Name'])

# Accessing a specific row by index
print("\nAccessing the row with index 1:")
print(data_frame.iloc[1])