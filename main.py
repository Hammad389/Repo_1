import sqlite3  #imported the sql lite library

conn = sqlite3.connect("employee.db")   #created a database with name employee.db and saved it in conn
c = conn.cursor()   #creating a cursor to iterate through database

# c.execute("""CREATE TABLE employees(  #added the columns to the database
#             first_name text,
#             last_name text,
#             pay integer)""")
c.execute("INSERT INTO employees VALUES ('Hammad', 'Hussain', 50000)")    #inserting elements into database
c.execute("SELECT * FROM employees WHERE last_name = 'Hussain'")          #selecting from database
print(c.fetchone())         #fetching the one entry
conn.commit()           #commiting the database
conn.close()

