from bluelink import BlueLink
from flask import Flask, jsonify
import os
import dotenv
import requests

# Load environment variables
dotenv.load_dotenv()
EMAIL = os.environ.get('EMAIL')
PASSWORD = os.environ.get('PASSWORD')
PIN = os.environ.get('PIN')
VIN = os.environ.get('VIN')
API_KEY = os.environ.get('API_KEY')

# Initialize Flask app
app = Flask(__name__)

# Logins to BlueLink. You may also choose to set the username, password, 
# and pin via environment variables (same convention as the CLI) and
# leave the arguments blank.
bl = BlueLink(email=EMAIL, password=PASSWORD, pin=PIN)
bl.login()


# Gets my car
car = bl.cars[VIN]  

@app.route('/', methods=["GET"])
def home():
    return "hello world"

@app.route('/start-engine', methods=['GET'])
def start_engine():
    try:
        car.start(duration=10, 
                    temp="70", 
                    defrost= False)
        return jsonify({'status': 'Engine started successfully',
                        'speech' : 'Your car has been started.'})
    except Exception as e:
        return jsonify({'error': str(e), 'speech' : 'I could not start your car, please try again.'}), 500
    
@app.route('/stop-engine', methods=['GET'])
def stop_engine():
    try:
        car.stop()
        return jsonify({'status': 'Engine stopped successfully',
                        'speech' : 'Your car has been stopped.'})
    except Exception as e:
        return jsonify({'error': str(e),
                        'speech' : 'I could not shut off your car, please try again.'}), 500

@app.route('/lock-doors', methods=['GET'])
def lock_doors():
    try:
        car.lock()
        return jsonify({'status': 'Doors locked successfully',
                        'speech': 'The doors have been locked successfully.'})
    except Exception as e:
        return jsonify({'error': str(e), 'speech': 'I could not lock the doors, please try again.'}), 500

@app.route('/unlock-doors', methods=['GET'])
def unlock_doors():
    try:
        car.unlock()
        return jsonify({'status': 'Doors unlocked successfully',
                        'speech': 'The doors have been unlocked successfully.'})
    except Exception as e:
        return jsonify({'error': str(e), 'speech': 'I could not unlock the doors, please try again.'}), 500

@app.route('/odometer', methods=['GET'])
def get_odometer():
    try:
        odometer = car.odometer
        return jsonify({'odometer': odometer,
                        'speech': f'The odometer reading is {odometer} miles.'})
    except Exception as e:
        return jsonify({'error': str(e), 'speech': 'I could not get the odometer reading, please try again.'}), 500
    

# helper function using OpenCage Geocoding API
def get_location_name(lat, lon, api_key):
    url = f"https://api.opencagedata.com/geocode/v1/json?q={lat}+{lon}&key={api_key}"
    response = requests.get(url)
    data = response.json()
    if data['results']:
        return data['results'][0]['formatted']
    else:
        return "Unknown location"


@app.route('/find-car', methods=['GET'])
def find_car():
    try:
        latitude, longitude = car.find()
        location_name = get_location_name(latitude, longitude, API_KEY)
        return jsonify({
            'latitude': latitude,
            'longitude': longitude,
            'location': location_name,
            'speech': f'Your car is located at {location_name}.'
        })
    except Exception as e:
        return jsonify({'error': str(e), 'speech': 'I could not find your car, please try again.'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
        