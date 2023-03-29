
# importing the module
import sqlite3
 
# connect with the myTable database
connection = sqlite3.connect("test.db")
 
# cursor object
crsr = connection.cursor()
 
# execute the command to fetch all the data from the table emp
command = "create table TRAINS(TRAIN_NO INT(6) NOT NULL, DEPARTURE VARCHAR(20) NOT NULL, DESTINATION VARCHAR(20) NOT NULL, DISTANCE INT(3) NOT NULL);"
crsr.execute(command)

command = """INSERT INTO TRAINS VALUES(000001,"CHENNAI","BANGALORE",350);"""
crsr.execute(command)

command = """INSERT INTO TRAINS VALUES(000002,"MADURAI","CHENNAI",500);"""
crsr.execute(command)

command = """INSERT INTO TRAINS VALUES(000003,"CHENNAI","COIMBATORE",450);"""
crsr.execute(command)

command = """INSERT INTO TRAINS VALUES(000004,"COIMBATORE","BANGALORE",550);"""
crsr.execute(command)

command = """INSERT INTO TRAINS VALUES(000005,"CHENNAI","TRICHY",350);"""
crsr.execute(command)

command = """INSERT INTO TRAINS VALUES(000006,"TRICHY","TIRUNELVELI",355);"""
crsr.execute(command)

command = """INSERT INTO TRAINS VALUES(000007,"TIRUNELVELI","CHENNAI",600);"""
crsr.execute(command)

command = """INSERT INTO TRAINS VALUES(000008,"TAMBARAM","TUTICORINE",500);"""
crsr.execute(command)

command = """INSERT INTO TRAINS VALUES(000009,"CHENNAI","COCHIN",600);"""
crsr.execute(command)

command = """INSERT INTO TRAINS VALUES(000010,"BANGALORE","TRIVANDRUM",750); """
crsr.execute(command)


connection.commit()
connection.close()