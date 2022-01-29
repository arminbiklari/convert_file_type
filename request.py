import requests
import re 
from bs4 import BeautifulSoup
import pandas 
import csv 
import json
import convert
json_req ={
    "userId": "3",
    "movieId": "1010",
    "tag": "funny",
    "timestamp": "1445714994"
}

if type(json_req) != str:
    print("yes")
# convert.make_json("/home/xubuntu/pt/python_project/ml-latest-small/links.csv", "/home/xubuntu/pt/python_project/phone_price/json.json")
convert.maske_csv(json_req, "/home/xubuntu/pt/python_project/phone_price/csv.csv")