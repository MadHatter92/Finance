import requests
import json

#API Key:  579b464db66ec23bdd00000118b816c7379c43c14ae999d440dad64e

data_url = 'https://api.data.gov.in/resource/9ef84268-d588-465a-a308-a864a43d0070?api-key=579b464db66ec23bdd00000118b816c7379c43c14ae999d440dad64e&format=json&offset=0&limit=1000'
response = requests.get(data_url)

# print(json.dumps(response.json(), indent=4, sort_keys=True))

data_list = response.json()['records']
# print(data_list[0])
states, commodities, districts, markets = set(), set(), set(), set()
for item in data_list:
	states.add(item.get('state'))
	commodities.add(item.get('commodity'))
	districts.add(item.get('district'))
	markets.add(item.get('market'))

print(str(len(commodities))+' commodities across '+str(len(states))+' states '+str(len(districts))+' districts and '+str(len(markets))+' markets.')

# for value in commodities:
# 	print(value, end = '\n')

# print(len(commodities))