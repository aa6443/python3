from geopy.geocoders import Nominatim
from geopy import distance

geocoder=Nominatim(user_agent="I know Python")
a=str(input("enter the 1st location:"))
b=str(input("enter the 2nd location:"))
location1=a
location2=b

coordinates1=geocoder.geocode(location1)
coordinates2=geocoder.geocode(location2)

print("latitude of coordinate 1 is :",coordinates1.latitude)
print("latitude of coordinate 2 is :",coordinates2.latitude)
print("longitude of coordinate 1 is:",coordinates1.longitude)
print("longitude of coordinate 2 is:",coordinates2.longitude)

print('\n')
lat1,long1=(coordinates1.latitude),(coordinates1.longitude)
lat2,long2=(coordinates2.latitude),(coordinates2.longitude)

place1=(lat1,long1)
place2=(lat2,long2)

print(distance.distance(place1,place2))
