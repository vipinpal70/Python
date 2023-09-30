import mysql.connector

    # // connected to the mysql here
    
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="vipin10"  
# )

    # for executing operation at this connected mysql
    
# mycursor = mydb.cursor()


    # creating new database

# mycursor.execute("CREATE DATABASE animesh")


    # show all database in the connection

# mycursor.execute("SHOW DATABASES")

# for x in mycursor:
#   print(x)


    # Try connecting to the database "mydatabase":

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="",
#   database="mydatabase"
# )

# mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

    # with primary key 
# mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

    # for edit already exit table 
    
# mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

# mycursor.execute("SHOW TABLES")

# for x in mycursor:
#   print(x)
    
  
    # for insert single value
    
# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("John", "Highway 21")
# mycursor.execute(sql, val)

    # for insert many values
    
# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = [
#   ('Peter', 'Lowstreet 4'),
#   ('Amy', 'Apple st 652'),
#   ('Hannah', 'Mountain 21'),
#   ('Michael', 'Valley 345'),
#   ('Sandy', 'Ocean blvd 2'),
#   ('Betty', 'Green Grass 1'),
#   ('Richard', 'Sky st 331'),
#   ('Susan', 'One way 98'),
#   ('Vicky', 'Yellow Garden 2'),
#   ('Ben', 'Park Lane 38'),
#   ('William', 'Central st 954'),
#   ('Chuck', 'Main Road 989'),
#   ('Viola', 'Sideway 1633')
# ]

# mycursor.executemany(sql, val)

# mydb.commit()

# print(mycursor.rowcount, "record inserted.")

    # for show all records int the table
    
# mycursor.execute("SELECT * FROM customers")

    # for selected few attributes from the table
    
# mycursor.execute("SELECT name, address FROM customers")

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)

  
''' If you are only interested in one row, you can use the fetchone() method.

The fetchone() method will return the first row of the result:    '''


# myresult = mycursor.fetchone()

# print(myresult)