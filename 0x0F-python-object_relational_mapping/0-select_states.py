#!/usr/bin/python3
import MySQLdb
import sys

# Get MySQL credentials from command line arguments
username = sys.argv[1]
password = sys.argv[2]
database_name = sys.argv[3]

# Connect to MySQL server
db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database_name)

# Create a cursor object using cursor() method
cursor = db.cursor()

# Execute SQL query to fetch states sorted by id
cursor.execute("SELECT * FROM states ORDER BY id ASC")

# Fetch all the rows using fetchall() method
data = cursor.fetchall()

# Display results
for row in data:
    print(row)

# Disconnect from server
db.close()

