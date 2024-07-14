# Hyundai Flask API

This Flask application provides an API to control various functions of your car using the BlueLink service. The API includes endpoints to start and stop the engine, lock and unlock the doors, check the odometer, and find the car's location.

## Prerequisites

- Python 3.6+

## Installation

1. Clone the repository or copy the code to your local machine.

2. Install the required Python packages using `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

3. Create a `.env` file in the root directory of your project and add your BlueLink credentials and OpenCage API key:

    ```
    EMAIL=your_email@example.com
    PASSWORD=your_password
    PIN=your_pin
    VIN=your_car_vin
    API_KEY=your_opencage_api_key
    ```

4. Ensure that `.env` is added to your `.gitignore` file:

    ```
    # .gitignore

    .env
    ```

## Usage

1. Start the Flask server:

    ```bash
    python app.py
    ```

2. The server will run on `http://0.0.0.0:5000/`.

3. You can now use the following API endpoints:

### Endpoints

#### Start Engine

- **URL**: `/start-engine`
- **Method**: `GET`
- **Response**:
  ```json
  {
    'status': 'Engine started successfully',
    'speech': 'Your car has been started.'
  }

#### Stop Engine

- **URL**: `/stop-engine`
- **Method**: `GET`
- **Response**:
  ```json
  {
    'status': 'Engine stopped successfully',
    'speech' : 'Your car has been stopped.'
  }

#### Lock Doors

- **URL**: `/lock-doors`
- **Method**: `GET`
- **Response**:
  ```json
  {
    'status': 'Doors locked successfully',
    'speech': 'The doors have been locked successfully.'
  }

#### Unlock Doors

- **URL**: `/unlock-doors`
- **Method**: `GET`
- **Response**:
  ```json
  {
    'status': 'Doors unlocked successfully',
    'speech': 'The doors have been unlocked successfully.'
  }

#### Odometer

- **URL**: `/odometer`
- **Method**: `GET`
- **Response**:
  ```json
  {
    'odometer': odometer,
    'speech': f'The odometer reading is {odometer} miles.'
  }

#### Find Car

- **URL**: `/find-car`
- **Method**: `GET`
- **Response**:
  ```json
  {
    'latitude': latitude,
    'longitude': longitude,
    'location': location_name,
    'speech': f'Your car is located at {location_name}.'
  }

## Setting Up Siri Shortcuts

To use Siri Shortcuts with the BlueLink Car Control API, follow these steps:

1. **Open the Shortcuts App**:
   - Open the Shortcuts app on your iPhone.
   - Tap the "+" icon to create a new shortcut.

2. **Create a Shortcut for Each Endpoint**:

### Example for Locking Doors

1. **Add Action - Get Contents of URL**:
   - Tap "Add Action".
   - Search for "Get Contents of URL" and select it.
   - Set the URL to `http://your-server/lock-doors` (replace `your-server` with your actual server address).
   - Tap "Show More".
   - Ensure "Method" is set to `GET`.

2. **Add Action - Get Dictionary from Input**:
   - Tap "Add Action".
   - Search for "Get Dictionary from Input" and select it.

3. **Add Action - Get Dictionary Value**:
   - Tap "Add Action".
   - Search for "Get Dictionary Value" and select it.
   - Tap on the "Key" field and set it to `speech`.

4. **Add Action - Speak Text**:
   - Tap "Add Action".
   - Search for "Speak Text" and select it.
   - Tap on "Text" and set it to the dictionary value you retrieved in the previous step.

5. **Test the Shortcut**:
   - Tap the play button to test the shortcut.
   - Siri should now read the `speech` value from the response aloud.

### Example for Other Endpoints

Follow similar steps for other endpoints by changing the URL in step 1 to the appropriate endpoint URL:

- Start Engine: `http://your-server/start-engine`
- Stop Engine: `http://your-server/stop-engine`
- Unlock Doors: `http://your-server/unlock-doors`
- Get Odometer: `http://your-server/odometer`
- Find Car: `http://your-server/find-car`

### Notes

- Ensure that your Flask server is accessible from your iPhone (both should be on the same network if using a local server).
- If running the server locally and you need remote access, consider using a tool like `ngrok` to expose your local server to the internet.
