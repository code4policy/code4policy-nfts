import csv
import json
from datetime import datetime

with open('data/NFT_Sales.csv','r') as f:
	reader = csv.DictReader(f)
	all_sales = list(reader)

with open('data/NFT_Sales.json','w') as f:
    json.dump(all_sales,f)

with open('data/NFT_Sales.json', 'r') as f:
    data = json.load(f)
    
with open('data/NFT_Sales_Daily.csv','w') as f:
    writer = csv.writer(f)
    writer.writerow(['date','close'])
    for data in data:
        date = data['Date']
        date_format = ("%Y-%m-%d")
        parsed_date = datetime.strptime(date,date_format)
        new_date = parsed_date.strftime("%d-%b-%y")
        if parsed_date.year < 2021:
            continue
        writer.writerow([new_date,data['Number_of_Sales']])