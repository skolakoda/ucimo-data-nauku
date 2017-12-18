import json
import requests

url = "http://ws.audioscrobbler.com/2.0/?method=geo.gettopartists&country=serbia&api_key=7cae540c521b580877caaad274a995cb&format=json"

data = requests.get(url).text
data = json.loads(data)

print "Najslusaniji izvodjac u izabranoj zemlji je"
print data['topartists']['artist'][0]['name']
