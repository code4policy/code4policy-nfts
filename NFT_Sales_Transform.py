import csv
import json
from pprint import pprint

with open('data/NFT_Sales.csv','r') as f:
	reader = csv.DictReader(f)
	all_sales = list(reader)

with open('data/NFT_Sales.json','w') as f:
    json.dump(all_sales,f)

with open('data/NFT_Sales.json', 'r') as f:
    data = json.load(f)
    
with open('data/NFT_Sales_Daily.csv','w') as f:
    writer = csv.writer(f)
    writer.writerow(['Date','Number_of_Sales'])
    for data in data:
        writer.writerow([data['Date'],data['Number_of_Sales']])