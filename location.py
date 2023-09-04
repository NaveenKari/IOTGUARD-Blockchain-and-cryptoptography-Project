from geopy.geocoders import Nominatim
from geopy.distance import geodesic

# Input IP addresses
def checkLocation(ip):
    # Get the approximate latitude and longitude of the IP addresses
    geolocator = Nominatim(user_agent='myapp')
    location1 = geolocator.geocode(ip)
    location2 = geolocator.geocode(ip)

# Calculate the distance between the two locations using the Haversine formula
    distance = geodesic((location1.latitude, location1.longitude), (location2.latitude, location2.longitude)).km
    print(f"The distance between {ip} and {ip} is approximately {distance:.2f} kilometers.")
    return distance




