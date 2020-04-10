#We need to import the libraries

from urllib.request import  urlopen as OPEN
from urllib.parse import urlencode as ENCODE
from xml.etree import ElementTree as XML

api_url = 'https://maps.googleapis.com/maps/api/geodode/xml?'