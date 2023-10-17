#!/bin/bash

# MySQL server information
MYSQL_USER="teargas001"
MYSQL_PASSWORD="37890018"
MYSQL_HOST="localhost"

# Run the MySQL command to list databases
mysql -u "$MYSQL_USER" -p"$MYSQL_PASSWORD" -h "$MYSQL_HOST" -e "SHOW DATABASES;"

