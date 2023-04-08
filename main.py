import os
from dotenv import load_dotenv
import mysql.connector

import config.database as database

load_dotenv()

# Create a connection to the database
connection = mysql.connector.connect(
    user     = os.getenv('DB_USER'), 
    password = os.getenv('DB_PASSWORD'),
    host     = os.getenv('DB_HOST'),
    database = os.getenv('DB_DATABASE')
)

print(database.get_connection())

#The cursor object, we can execute the SQL queries and fetch the results. The cursor object is an instance of the Cursor class. The cursor object is used to traverse the records from the result set. The cursor object is created by calling the cursor() method of the connection object.

# Create a cursor to execute queries
cursor = connection.cursor()

# Execute a query
query = "SELECT * FROM users LIMIT 1"
cursor.execute(query)

# print(cursor)
# print(type (cursor))

# Retrieve the results
for fila in cursor:
    print(fila)
    # print(type (fila))

# Close the cursor and the connection
cursor.close()
connection.close()
