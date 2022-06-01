import csv
import time
import requests
import json

dat = {}
fp = "D:\\PWR\\Visual Studio\\systemy_informatyczne_internetu_rzeczy\\lista5\\datasets\\data1.csv"
input_file = csv.DictReader(open(fp))
header = next(input_file)
for row in input_file:
    row['time'] = time.time()
    print(row)
    break
    