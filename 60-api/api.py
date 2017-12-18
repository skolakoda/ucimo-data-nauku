import requests

# http://open-notify.org/Open-Notify-API/
parameters = {"lat": 37.78, "lon": -122.41}

# nemam pojma sta predstavljaju podaci
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
# response.status_code

content = response.content
json_data = response.json()
first_pass_duration = json_data["response"][0]["duration"]

print(content)
print(first_pass_duration)

# koliko je ljudi u svemiru trenutno?
response = requests.get("http://api.open-notify.org/astros.json")
json_data = response.json()
in_space_count = json_data["number"]

print("Trenutno ima %d osobe u svemiru." % in_space_count)
