import csv
import json
from datetime import datetime

# Read NFT Sales data in original CSV file
with open('data/NFT_Sales.csv','r') as f:
	reader = csv.DictReader(f)
	all_sales = list(reader)

# Convert to JSON format
with open('data/NFT_Sales.json','w') as f:
    json.dump(all_sales,f)

# Read JSON file as a List
with open('data/NFT_Sales.json', 'r') as f:
    data = json.load(f)

# Create a new CSV with only the date and Number of Sales, while converting the date format
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