import os
import dj_database_url
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def generate_remove_sql(database_url):
    # Parse the DATABASE_URL
    db_info = dj_database_url.parse(database_url)
    
    # Extract the necessary components
    db_user = db_info['USER']
    db_name = db_info['NAME']
    
    # Generate SQL commands as a string
    sql_commands = f"""
    REVOKE ALL PRIVILEGES ON DATABASE {db_name} FROM {db_user};
    DROP DATABASE IF EXISTS {db_name};
    DROP USER IF EXISTS {db_user};
    """
    
    return sql_commands.strip()

def main():
    # Get the DATABASE_URL from the environment
    database_url = os.getenv("DATABASE_URL")
    if not database_url:
        raise ValueError("DATABASE_URL is not set in the environment variables.")

    # Generate the SQL script
    sql_script = generate_remove_sql(database_url)
    
    # Print the SQL script to stdout
    print(sql_script)

if __name__ == "__main__":
    main()
