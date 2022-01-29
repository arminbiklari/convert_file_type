import json 
import csv
import pandas as pd 
import mysql.connector
 # function for convert csv to json 
def make_json(csvpath, jsonpath): # input 2 parameters for path of files (csv and json)
    jdict = {} # create dictionary for insert data from json 
    with open(csvpath, encoding='utf_8') as csvreader: # open file with handler
        csvr = csv.DictReader(csvreader)
        counter = 0
        for row in csvr:
            counter +=1 # counter for cout number of lines 
            # key = row[counter]
            jdict[str(counter)] = row # input in dictionary keys is number of line 

    with open(jsonpath,'w', encoding='utf_8') as jsonreader: # oprn file for write json 
        jsonreader.write(json.dumps(jdict, indent=0)) # dump dictionary into json file 
# create list for keep path of jsons files         
jsonlist =["/home/xubuntu/pt/python_project/convert_file_type/test.json", "/home/xubuntu/pt/python_project/convert_file_type/test2.json"]
# function for convert json to csv 
def maske_csv(jsonlist, csvpath):
    # print(type(jsonlist))
    ## check if jdsonlist is a dictionary or a path 
    if type(jsonlist) != dict: 
        if len(jsonlist) < 2: # condition for check if json files more than 1 
            for items in jsonlist:
                # print(items)   # item is path of json      
                jsonr = pd.read_json(items, orient='index')
                print(jsonr) # jsonr is dictionary
                csvr =jsonr.to_csv(csvpath, index=False)
        else: # else condition for merge jsons to a single csv file 
            for items in jsonlist:
                jsonr = pd.read_json(items, orient='index') # input json file in jsonr as a handler
                csvr =jsonr.to_csv(csvpath, mode='a', index=False) # append result to csv 
    else:
        # redirect dictionary in csv file 
        with open(csvpath, 'w', encoding='utf_8') as csvwriter:
            headers = [] # create a list for header of csv file
            for key in jsonlist.keys():
                headers.append(key) # append keys for header 
            csvw = csv.DictWriter(csvwriter, fieldnames= headers)
            csvw.writeheader()
            csvw.writerow(jsonlist)
def creat_db(databasename):
    try:
        print("connecting to database ...")
        connection= mysql.connector.connect(user='armin', password='QWEr!@#4', host='127.0.0.1')    
        print("connected !! ")
    except:
        print("connot connect to database !!")
    cursor = connection.cursor()
    try:
        cursor.execute("CREATE DATABASE %s" % databasename)
    except:
        print("database not create because its exist !!")

        connection.commit()


# make_json("/home/xubuntu/pt/python_project/test.csv", "test.json")
# maske_csv(jsonlist, "/home/xubuntu/pt/python_project/convert_file_type/test.csv")
