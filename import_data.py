# save this as app.py
import mysql.connector
import pandas as pd

#Connect to mysql
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)
mycursor = mydb.cursor()

#Create the DB (if not already exists)
mycursor.execute("CREATE DATABASE IF NOT EXISTS SERIAL_KILLERS")

#Create the table for the csv data (if not exists)
mycursor.execute("""
  CREATE TABLE IF NOT EXISTS SERIAL_KILLERS.Killers (
    Name VARCHAR(30) NOT NULL,
    Country Text,
    Years Active Text,
    Proven Victims Text,
    Possible Victims Text,
    Notes Text,
    PRIMARY KEY (Name)
  );""")

#Delete data from the table Clsh_Unit
mycursor.execute("DELETE SERIAL.KILLERS.Killelrs")
mydb.commit()

#Read data from a csv file
killers_data = pd.read_csv('./cr-unit-attributes.csv', index_col=False, delimiter = ',')
killers_data = killers_data.fillna('Null')
print(killers_data.head(20))

#Fill the table
for i,row in killers_data.iterrows():
    cursor = mydb.cursor()
    #here %S means string values 
    sql = "INSERT INTO SERIAL_KILLERS.Killers VALUES (%s,%s,%s,%s,%s,%s)"
    cursor.execute(sql, tuple(row))
    print("Record inserted")
    # the connection is not auto committed by default, so we must commit to save our changes
    mydb.commit()

#Check if the table has been filled
mycursor.execute("SELECT * FROM SERIAL_KILLERS.Killers")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)