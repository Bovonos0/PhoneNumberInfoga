import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone
import time
time.sleep(0.5)
print ("By Bovonos")
time.sleep(0.5)
print ("GitHub: https://github.com/Bovonos0")
time.sleep(0.5)
ptint ("")
time.sleep(0.5)
number=input("Type a Number: ")
number =phonenumbers.parse(number ,"CH")
country=geocoder.description_for_number(number,"en")
print ("Country: ",country)

num1=str(number)
national_number=num1.replace('National Number:', '')
national_number=national_number.replace('Country Code:', '')
national_number=national_number.replace(' ', '')
print ("Phone Number: ",national_number)

numberscan=phonenumbers.is_possible_number(number)
print ("is possible number: ",numberscan)

numberscan=phonenumbers.is_valid_number(number)
print ("is valid number: ",numberscan)

Line=carrier.name_for_number(number, "en")
print ("Line: ",Line)

location=timezone.time_zones_for_number(number)
print ("TimeZone: ",location)

