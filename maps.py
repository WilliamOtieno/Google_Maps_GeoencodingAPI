#We need to import the libraries

from urllib.request import  urlopen as OPEN
from urllib.parse import urlencode as ENCODE
from xml.etree import ElementTree as XML

api_url = 'https://maps.googleapis.com/maps/api/geodode/xml?'

#Next we need to take user input, add the input to the api_url:
address = input("Enter address: ")
if len(address) < 1:
    address = 'Warsaw, Poland'

#encoding to UTF-8 and adding to the API URL:
url = api_url + ENCODE({'address': address})

#Next we need to perform the actual API request, get the lattitude and longitude coordinates from teh response XML:

#getting the data
data = OPEN(url).read()

#digging into the XML tree:
tree = XML.fromstring(data)
res = tree.findall('result')

#dig into the XML tree to find 'latitude and longitude'
lat = res[0].find('geometry').find('location').find('lat').text
lng = res[0].find('geometry').find('location').find('lng').text
