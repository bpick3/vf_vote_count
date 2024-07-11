import pandas as pd

# Load the CSV file
csv_file = 'Private-PSR-Vote-History-C0-2024-07-01.csv'  # Replace with your CSV file name

# Read the CSV file, skipping bad lines
try:
    df = pd.read_csv(csv_file, on_bad_lines='skip')
    # Ensure that the column E (5th column, zero-indexed) exists
    if df.shape[1] >= 5:
        column_name = df.columns[4]  # Column E (5th column)
        non_null_count = df[column_name].count()
        print(f"The number of non-null values in column 'E' is: {non_null_count}")
    else:
        print("The CSV file does not have enough columns.")
except Exception as e:
    print(f"Error reading the CSV file: {e}")
