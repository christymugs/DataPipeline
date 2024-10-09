from sqlalchemy import create_engine

# Create a connection to PostgreSQL
engine = create_engine('postgresql://username:password@localhost:5432/mydatabase')

# Load data into PostgreSQL
monthly_sales.to_sql('monthly_sales', engine, if_exists='replace', index=False)

print("Data successfully loaded into PostgreSQL.")
