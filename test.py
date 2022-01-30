import json
import pandas as pd 
jsonpath = "/home/xubuntu/pt/python_project/phone_price/json.json"
with open(jsonpath, encoding='utf_8') as jsonreader:
    list = []
    # json_data = pd.read_json(jsonreader, orient='index').to_dict()
    json_data = json.load(jsonreader)
    print(json_data)
    print(type(json_data))
    for val in json_data.values():
        for i in val.items():
            val.keys()
            val.values()
        for key in val.keys():
            if key in list:
                pass
            else:
                list.append(key)


print(valuelist)
print(list)