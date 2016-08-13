import requests
import json
import ast
import os
from flask import Flask

# Run a flask endpoint
app = Flask(__name__)
SPARK_SVC_ENDPOINT = os.environ['SPARK_SVC_ENDPOINT']

@app.route('/')
def confirm_service():
    return "Service OK"

@app.route('/getnearby', methods=["GET", "POST"])
def getnearby():
    locations = json.loads(get_nearby_locations())
    result = package_nearby_locations(locations)
    request_params = {'message' : result}
    r = requests.post(SPARK_SVC_ENDPOINT, params=request_params)
    return "Ok"

def get_nearby_locations():
    API_KEY = os.environ['API_KEY']
    location = "-33.8670522,151.1957362"
    endpoint = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=" + location + "&radius=500&type=restaurant&key=" + API_KEY
    r = requests.get(url=endpoint)
    return r.text

def package_nearby_locations(message):
    for result in message['results']:
        return result['name'] + ", which is near " + result['vicinity']

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5500, debug=True)
