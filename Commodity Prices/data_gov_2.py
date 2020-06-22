import requests
import csv

#API Key:  579b464db66ec23bdd00000118b816c7379c43c14ae999d440dad64e

CSV_URL = 'https://api.data.gov.in/resource/9ef84268-d588-465a-a308-a864a43d0070?api-key=579b464db66ec23bdd00000118b816c7379c43c14ae999d440dad64e&format=csv&offset=0&limit=1000'

with requests.Session() as s:
    download = s.get(CSV_URL)

    decoded_content = download.content.decode('utf-8')

    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    data_list = list(cr)
    for row in data_list:
        print(row[1])

# print(data_list[0])