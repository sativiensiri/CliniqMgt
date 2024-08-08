import sqlite3
import json
import os
from dotenv import load_dotenv

load_dotenv()
database = os.getenv('DATABASE')

connection = sqlite3.connect(database)
cursor = connection.cursor()

from datetime import datetime

# getting the current date and time
current_datetime = datetime.now()
current_date_time = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

# Create Table
# cursor.execute("CREATE TABLE IF NOT EXISTS employee (id INTEGER, name TEXT, department TEXT, telephone TEXT)")
# cursor.execute("CREATE TABLE IF NOT EXISTS department (id INTEGER, name TEXT)")

# Insert data
# cursor.execute("INSERT INTO department VALUES (100, 'management')")
# cursor.execute("INSERT INTO department VALUES (200, 'staff')")
# cursor.execute("INSERT INTO example VALUES (1, 'alice', 20)")
# cursor.execute("INSERT INTO example VALUES (2, 'bob', 30)")
cursor.execute(f"INSERT INTO employee VALUES ('201', 'Siritorn', 'Viensiri', 'staff', '0896690116', '{current_date_time}')")
connection.commit()
#    Full Calendar 2010-01-01T14:30:00
# cursor.execute("SELECT * FROM department")
# columns = [column[0] for column in cursor.description]
# data = [dict(zip(columns, row)) for row in cursor.fetchall()]
# json_data = json.dumps(data, indent=4)
#
# # rows = cursor.fetchall()
# # print("print all rows")
# # print(rows)
# # print("")
# # print("print one row[0]")
# # print(rows[0])
# # print("")
# # print("loop row in rows")
# # for row in rows:
# #     print(f"id: {row[0]}, name: {row[1]}, age: {row[2]}")
#
# print("")
# print("Convert to JSON")
# print(json_data)
# print("")
# jdata = json.loads(json_data)
# for item in jdata:
#     print(item["id"], item["name"])
#
connection.close()