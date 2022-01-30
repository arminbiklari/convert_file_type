from textwrap import indent
import mysql.connector
import convert
import json
import pandas as pd 
databaseuser = 'root'
databasePassword = '87tZ#Ub4tE^m!8Ka=anK3z9gnnnR-JJa'
databasehost= '192.168.1.10'
databasename = 'test2'

#convert.create_db(databasename, databasePassword, databaseuser, databasehost)

print(list)    
def create_table(dbseuser, dbpassword, dbhost, dbname, jsonpath):
    with open(jsonpath, encoding='utf_8') as jsonreader:
        json_data = json.load(jsonreader)
    list = [] # create  a list for insert column in table 
    for value in json_data.values(): # loop in main dictionary
        for key in value.keys(): # loop for values of main (value as a dictionary)
            if key in list: # check key is exist or not for removing duplicate in list
                pass # if exist just pass
            else:
                list.append(key) # if not exist append to list 
    try:
        print('connecting to database ...')
        connection = mysql.connector.connect(user=dbseuser, password=dbpassword, host=dbhost, db= dbname) # conection to db
        print('connected .')
        cursor = connection.cursor() #  create a cursor for execute queries
        for i in range(len(list)):
            list[i] += " varchar(255)"
        liststring = ", ".join(list) ## make a string for create table with this string name of column
        cursor.execute("CREATE TABLE movies (%s) ;" % (liststring))
        for value in json_data():
            for key, value in value.items():
                cursor.execute("INSERT INTO ")

    except:
        print('connot connect to database !!')

