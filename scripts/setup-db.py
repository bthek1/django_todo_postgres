import os
import dj_database_url
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def generate_sql(database_url):
    # Parse the DATABASE_URL
    db_info = dj_database_url.parse(database_url)
    
    # Extract the necessary components
    db_user = db_info['USER']
    db_password = db_info['PASSWORD']
    db_name = db_info['NAME']
    
    # Generate SQL commands as a string
    sql_commands = f"""
    CREATE USER {db_user} WITH PASSWORD '{db_password}';
    CREATE DATABASE {db_name} OWNER {db_user};
    GRANT ALL PRIVILEGES ON DATABASE {db_name} TO {db_user};
    ALTER ROLE {db_user} SET client_encoding TO 'utf8';
    ALTER ROLE {db_user} SET default_transaction_isolation TO 'read committed';
    ALTER ROLE {db_user} SET timezone TO 'UTC';
    ALTER ROLE {db_user} CREATEDB;
    
    """
    
    return sql_commands.strip()

def main():
    # Get the DATABASE_URL from the environment
    database_url = os.getenv("DATABASE_URL")
    if not database_url:
        raise ValueError("DATABASE_URL is not set in the environment variables.")

    # Generate the SQL script
    sql_script = generate_sql(database_url)
    
    # Print the SQL script to stdout
    print(sql_script)

if __name__ == "__main__":
    main()
