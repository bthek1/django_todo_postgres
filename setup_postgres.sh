#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

# Load environment variables from .env file
if [ -f .env ]; then
    export $(grep -v '^#' .env | xargs)
else
    echo ".env file not found!"
    exit 1
fi

# Function to install PostgreSQL if it's not already installed
install_postgres() {
    if ! dpkg -l | grep -q postgresql; then
        echo "Installing PostgreSQL..."
        sudo apt update
        sudo apt install -y postgresql postgresql-contrib
    else
        echo "PostgreSQL is already installed."
    fi
}


# Function to start PostgreSQL service
start_postgres() {
    echo "Starting PostgreSQL service..."
    sudo systemctl start postgresql
    sudo systemctl enable postgresql
}

# Function to check if a PostgreSQL user exists
user_exists() {
    sudo -u postgres psql -tAc "SELECT 1 FROM pg_roles WHERE rolname='$DB_USER'" | grep -q 1
}

# Function to check if a PostgreSQL database exists
database_exists() {
    sudo -u postgres psql -tAc "SELECT 1 FROM pg_database WHERE datname='$DB_NAME'" | grep -q 1
}

# Function to create PostgreSQL user
create_user() {
    if user_exists; then
        echo "User $DB_USER already exists."
    else
        sudo -u postgres psql -c "CREATE USER $DB_USER WITH PASSWORD '$DB_PASSWORD';"
        echo "User $DB_USER created."
    fi
}

# Function to create PostgreSQL database
create_database() {
    if database_exists; then
        echo "Database $DB_NAME already exists."
    else
        sudo -u postgres psql -c "CREATE DATABASE $DB_NAME OWNER $DB_USER;"
        echo "Database $DB_NAME created."
    fi
}

# Function to grant privileges
grant_privileges() {
    sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE $DB_NAME TO $DB_USER;"
    echo "Granted all privileges on database $DB_NAME to user $DB_USER."
}

# Main script execution
install_postgres
start_postgres
create_user
create_database
grant_privileges

echo "PostgreSQL setup completed."
