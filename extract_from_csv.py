import pandas as pd

# Load data from a CSV file
file_path = "sales_data.csv"

# Specify dtype for specific columns if known
dtype_spec = {
    'Order ID': str,  # Example: change to str if IDs are alphanumeric
    # Add more columns if necessary
}

# Read CSV with specified options
sales_data = pd.read_csv(file_path, dtype=dtype_spec, low_memory=False)

# Display first 5 rows of data
print(sales_data.head())
