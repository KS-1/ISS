import requests
import json

from datetime import datetime

def jprint(obj):
    # create a formatted string of the python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

# define parameters for the lat and long of Orlando
parameters = {
    "lat": 28.53,
    "lon": -81.38
}

url = "http://api.open-notify.org/iss-pass.json"

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
    print(time)

#jprint(pass_times)

