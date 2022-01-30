from urllib import request
import mysql.connector 
from mysql.connector import connect
import requests

#req = requests.get('https://www.digikala.com/search/category-mobile-phone/?q=%d8%a7%d9%be%d9%84&entry=mm')


try:
    print("connecting to database ...")
    connection= mysql.connector.connect(user='behnam', password='123', host='192.168.1.40')    
    print("connected !! ")
except:
    print("connot connect to database !!")
# def create_db(databasename):
#     cursor = connection.cursor()
#     try:
#         cursor.execute("CREATE DATABASE %s" % databasename)
#     except:
#         print("database not create because its exist !!")

#     connection.commit()

# create_db(input("Enter your database name for create : "))
# ## define a function for show databases 
# def show_db():
#     cursor = connection.cursor()
#     try: 
#         cursor.execute("SHOW DATABASES;")
#         for database in cursor: # iterat for each line to print database
#             print(database)
#     except:
#         print("connot show databases !!")
 