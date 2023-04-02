'''import csv
import pymysql

# Connect to MySQL database
conn = pymysql.connect(host='127.0.0.1', user='root', password='Cumafrank4me@', db='test', port=3306)

# Create a cursor object
cursor = conn.cursor()

# Open CSV file and read data
with open('datasheet.csv', 'r') as file:
    csv_data = csv.reader(file)

    # Loop through each row and insert data into MySQL database
    for row in csv_data:
        cursor.execute('INSERT INTO table_name (column1, column2, column3) VALUES (%s, %s, %s)', row)

# Commit changes to the database
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()'''

import csv
import pymysql

# Connect to MySQL database
conn = pymysql.connect(host='localhost', user='test', password='password', db='athena',charset = "utf8")

# Create a cursor object
cursor = conn.cursor()

# Open CSV file and read data
with open('datasheet.csv', 'r') as file:
    csv_data = csv.reader(file)

    # Loop through each row and insert data into MySQL database
    for row in csv_data:
        cursor.execute('INSERT INTO table_name (column1, column2, column3) VALUES (%s, %s, %s)', row)

# Commit changes to the database
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()