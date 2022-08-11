#https://developer.nrel.gov
#https://developer.nrel.gov/api/alt-fuel-stations/v1.json?fuel_type=E85,ELEC&state=CA&limit=2&api_key=gVl6k04aFcnQ0PU5oiTf2a6ZUKYNANwc8Ogr5bcb
import requests
res=requests.get("https://developer.nrel.gov/api/alt-fuel-stations/v1.json?fuel_type=E85,ELEC&state=CA&limit=2&api_key=gVl6k04aFcnQ0PU5oiTf2a6ZUKYNANwc8Ogr5bcb")
print(res.status_code)
print(res.text)
print(res.json())
print(list(res.json()))



api_address='http://api.openweathermap.org/data/2.5/weather?appid=fe9b9e6ca49163feccd87291232b986f&q='
city = input('City Name :')
url = api_address + city
print(url)
json_data = requests.get(url).json()
print(json_data)
format_add = json_data['weather'][0]['main']
format_add1 = json_data['weather'][0]['description']
print(format_add,"and ",format_add1)


#https://console.cloud.google.com/apis/credentials?project=daring-avenue-313103&folder=&organizationId=

with open('mygoogleapikey') as f:
    api_key1 = f.readline()
    f.close
print(api_key1)


import urllib.request, json
#Google MapsDdirections API endpoint
endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'
api_key = api_key1
#Asks the user to input Where they are and where they want to go.
origin = input('Where are you?: ').replace(' ','+')
destination = input('Where do you want to go?: ').replace(' ','+')
#Building the URL for the request
nav_request = 'origin={}&destination={}&key={}'.format(origin,destination,api_key)
request = endpoint + nav_request
#Sends the request and reads the response.
response = urllib.request.urlopen(request).read()
#Loads response as JSON
directions = json.loads(response)
print(directions)