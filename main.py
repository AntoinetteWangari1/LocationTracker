import phonenumbers

import folium

from myNumber import number

from phonenumbers import geocoder

Key = "aede581ade5b44d2aec93db5ffca8f0a"

sanNumber = phonenumbers.parse(number)

yourLocation = geocoder.description_for_number(sanNumber, "en")
print(yourLocation)


#Get service provider
from phonenumbers import carrier

service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))


#Get lat and lon and put in a map

from opencage.geocoder import OpenCageGeocode
geocoder = OpenCageGeocode(Key)

query= str(yourLocation)

results = geocoder.geocode(query)
#print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat,lng)

myMap = folium.Map(location =[lat, lng], zoom_start=9)

folium.Marker([lat,lng], popup =yourLocation).add_to((myMap))

#save map in html file

myMap.save("myLocation.html")