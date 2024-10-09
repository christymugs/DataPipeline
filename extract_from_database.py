from sqlalchemy import create_engine

# Define connection string to PostgreSQL
engine = create_engine('postgresql://username:password@localhost:5432/mydatabase')

# Extract data from the database
query = "SELECT * FROM sales_table"
sales_data_db = pd.read_sql(query, engine)

# Display first 5 rows of data from the database
print(sales_data_db.head())
