import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone
number=input("Type a Number: ")
number =phonenumbers.parse(number ,"CH")
country=geocoder.description_for_number(number,"en")
print ("Country: ",country)
print (number)

numberscan=phonenumbers.is_possible_number(number)
print ("is possible number: ",numberscan)

numberscan=phonenumbers.is_valid_number(number)
print ("is valid number: ",numberscan)

Line=carrier.name_for_number(number, "en")
print ("Line: ",Line)

location=timezone.time_zones_for_number(number)
print ("Location: ",location)

