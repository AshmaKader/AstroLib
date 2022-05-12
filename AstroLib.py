import sqlite3 as sq
 
# Import pandas module into
# this program as pd
import pandas as pd
   
# Create a connection object,
# Make a new db if not exist already 
# and connect it, if exist then connect.2
def Astrolib(date):
  connection = sq.connect('./Sq4 few data.db')
  # Create a cursor object
  curs = connection.cursor()
  
  curs.execute("SELECT * FROM Planets WHERE Date=?", (date,))
  rows=curs.fetchall() 
  for row in rows:
    print("Sun: "+str(row[1]))
    print("Moon: "+str(row[2]))
    print("Mercury: "+str(row[3]))
    print("Venus "+str(row[4]))
    print("Mars "+str(row[5]))
    print("Jupiter "+str(row[6]))
    print("Saturn "+str(row[7]))
    print("Uranus "+str(row[8]))
    print("Neptune"+str(row[9]))
    print("Pluto "+str(row[10]))
    print("Mean Node "+str(row[11]))
    print("")
  # Close connection to SQLite database
  connection.close()
date=input("Enter Date(IN YYYYMMDD Format):")  #Testing:Enter Date 20000102
Astrolib=Astrolib(date)
