import phonenumbers

from myNumber import number

from phonenumbers import geocoder

sanNumber = phonenumbers.parse(number)

yourLocation = geocoder.description_for_number(sanNumber, "en")
print(yourLocation)