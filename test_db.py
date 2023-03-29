# importing the module
import sqlite3
 
# connect with the myTable database
connection = sqlite3.connect("test.db")
 
# cursor object
crsr = connection.cursor()
 
# execute the command to fetch all the data from the table emp
command = "SELECT * FROM TRAINS;"
crsr.execute(command)


data = crsr.fetchall() 

for i in range(len(data)):
    print(data[i])

connection.close()