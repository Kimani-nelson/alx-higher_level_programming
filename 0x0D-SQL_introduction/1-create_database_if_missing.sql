#!/bin/bash

# MySQL server information
MYSQL_USER="your_username"
MYSQL_PASSWORD="your_password"
MYSQL_HOST="localhost"

# Database name to create
DB_NAME="hbtn_0c_0"

# Check if the database already exists
EXISTING_DB=$(mysql -u "$MYSQL_USER" -p"$MYSQL_PASSWORD" -h "$MYSQL_HOST" -e "SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = '$DB_NAME';" --skip-column-names)

if [ -z "$EXISTING_DB" ]; then
    # The database doesn't exist, so create it
    mysql -u "$MYSQL_USER" -p"$MYSQL_PASSWORD" -h "$MYSQL_HOST" -e "CREATE DATABASE $DB_NAME;"
    echo "Database $DB_NAME created successfully."
else
    # The database already exists
    echo "Database $DB_NAME already exists."
fi

