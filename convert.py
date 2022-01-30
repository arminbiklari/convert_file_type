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
def create_db(databasename, password, user, host):
    try:
        print("connecting to database ...")
        connection= mysql.connector.connect(user=user, password=password, host=host)    
        cursor = connection.cursor()
        print("connected !! ")
    except:
        print("connot connect to database !!")
    try:
        cursor.execute("CREATE DATABASE %s DEFAULT CHARACTER SET utf8;" % databasename)
        connection.commit()
    except:
        print("database not create because its exist !!")

def json_to_excel(execlpath, jsonpath):
    with open(jsonpath, encoding='utf_8') as jsonreader : # open file for read json file 
        data = json.load(jsonreader) ## load json data in Dictionary
        df =pd.DataFrame(data) ## create a dataframe 
        df.to_excel(execlpath) ## insert dataframe in e excel

    pass      
def excel_to_json(excelpath, jsonpath):
    excel_dataframe = pd.read_excel(excelpath).to_dict()  ## insert exce ldataframe in a variable as a dictionary 
    with open(jsonpath, 'w', encoding='utf_8') as jsonwriter:
        jsonwriter.write(json.dumps(excel_dataframe, indent=0))
jsonlist =["/home/xubuntu/pt/python_project/convert_file_type/test.json", "/home/xubuntu/pt/python_project/convert_file_type/test2.json"]
excelpath = "/home/xubuntu/pt/python_project/phone_price/test.xlsx" ## path of exel 
jsonpath = "/home/xubuntu/pt/python_project/phone_price/json2.json" ## path of json 
