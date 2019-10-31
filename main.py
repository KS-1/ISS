import requests
import json

from datetime import datetime

# Define the used URL
url = "http://api.open-notify.org/iss-pass.json"

def jprint(obj):
    # create a formatted string of the python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

# Get the latitude and longitue from the user
lat = input ("Enter the latitude of your city: ")
lon = input ("Enter the logitude of your city: ")

# Set the lat and lon values in the dict based on the user values
parameters = {
    "lat": float(lat),
    "lon": float(lon)
}

'''
# define parameters for the lat and long of Orlando
parameters = {
    "lat": 28.53,
    "lon": -81.38
}
'''

response = requests.get(url, params=parameters)

pass_times = response.json()['response']

risetimes = []
times = []

for d in pass_times:
    time = d['risetime']
    risetimes.append(time)

for rt in risetimes:
    time = datetime.fromtimestamp(rt)
    times.append(time)
    print(time.strftime("%m-%d-%Y at %H:%M:%S %p"))

#jprint(pass_times)

