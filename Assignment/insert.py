# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 17:33:38 2023

@author: HP
"""
import MySQLdb

# Connect Python to PuTTY
db = MySQLdb.connect("cscdata.centre.edu", "gabe", "G@be123!", "gabe_grades")
cursor = db.cursor() # Initiate cursor
f_file = open("grades.csv", mode = "r") # Open csv file to read
l_file = f_file.readlines() # Save all row content in list
del l_file[0] # Delete the header

# Loop through every record
for i in range(len(l_file)): 
    # Initiate an empty list to hold values to insert
    # Initiate the first part of the query
    data_to_insert, sql = [], "INSERT INTO students "

    data = l_file[i].strip().split(",") # Extract every cell from the rows
    for i in range(9): # Collect only the first 9 entities to match the table
        try: # Computation to assign appropraite data type
            data[i] = int(data[i])
        except:
            print("Incompatible data type")
        data_to_insert.append(data[i])
            
    data_to_insert = tuple(data_to_insert) # This data type is most convenient
    sql += "VALUES" + str(data_to_insert) # Complete the rest of the query
    if not "" in data_to_insert: # Ignore empty records
        print(data_to_insert)
        cursor.execute(sql) # Upload record into table
        db.commit() # Save change

db.close() # Terminate connection to PuTTY
f_file.close() # Close file
