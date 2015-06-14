import urllib.request
from urllib.error import  URLError
import json
import ssl

ccode = input("Enter a country code: ")
# A little trickery to bypass certification
context = ssl._create_unverified_context()
#urllib.urlopen("https://no-valid-cert", context=context)

try:
    page = urllib.request.urlopen("https://restcountries.eu/rest/v1/alpha/" + ccode, context=context)
    code=page.getcode()
    if(code == 200):
        content=page.read()
        content_string = content.decode("utf-8")
        json_data = json.loads(content_string)
        print("Country: " + json_data["name"])
        print("Capital: " + json_data["capital"])
              
except URLError as e:
        print("Invalid country code")

