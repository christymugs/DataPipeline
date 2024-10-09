import pandas as pd
import warnings

# Suppress warnings
warnings.filterwarnings("ignore")

# Load data from a CSV file
file_path = "sales_data.csv"

# Specify dtype for specific columns if known
dtype_spec = {
    'Order ID': str,  
}

# Read CSV with specified options
sales_data = pd.read_csv(file_path, dtype=dtype_spec, low_memory=False)

# Drop rows with missing values
cleaned_data = sales_data.dropna()

# Convert 'Date' to datetime using a specific format (modify the format as necessary)
cleaned_data['Date'] = pd.to_datetime(cleaned_data['Date'], format='%m-%d-%y')  


monthly_sales = cleaned_data.resample('ME', on='Date').sum(numeric_only=True)  

print("\n--- Monthly Sales Summary ---\n")
print(monthly_sales.to_string(index=True, float_format='${:,.2f}'.format))
print("\nTotal Sales: ${:,.2f}".format(monthly_sales.sum().sum()))
