import requests

URL = 'https://restcountries.com/v2/all'

r = requests.get(URL)
#print(r.json())


countries = r.json()
mappedCountryData = []

for country in countries:
    #print(country['name'])
    mappedCountryData.append({'nom': country['name']})

#print(mappedCountryData)

for data in mappedCountryData:
    flag = {'flag': country['flag']}
    for country in countries:
     data.update() 