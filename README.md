🕹️ Web-Based Light Scheduler using WebSocket and MQTT
A simulated IoT dashboard to schedule a light ON/OFF using a browser interface, WebSocket, MQTT, and Arduino.

🧠 Overview
This project allows you to:

Schedule ON/OFF times for a light from your browser
Send the schedule to a WebSocket server
Forward the schedule to an MQTT broker
Let a Python subscriber send '1' or '0' to an Arduino via serial based on time

🛠️ Tech Stack

Component	Tech Used
Frontend	HTML, CSS, JavaScript
Backend	Python websockets, subprocess
Messaging	Mosquitto MQTT (mosquitto_pub/sub)
Hardware Comm	Python pyserial, Arduino UNO
Protocols	WebSocket, MQTT, Serial

🧩 Project Structure

📁 light-scheduler/
├── frontend/
│   └── index.html              # UI for scheduling ON/OFF times
├── websocket_server.py         # WebSocket backend
├── mqtt_subscriber.py          # MQTT subscriber and serial communicator
├── README.md                   # This file

 How It Works

User Interface (index.html)
You select ON and OFF times and click "Submit".

WebSocket Server (Python)
Receives the schedule, logs it, and runs mosquitto_pub to publish it.

MQTT Subscriber (Python)
Listens for the schedule, compares current time, and sends '1' (ON) or '0' (OFF) to Arduino over serial.

Arduino
Already programmed to trigger relay based on serial input.

Setup Instructions
1. Clone the Repository
   git clone https://github.com/k2albert/urban-lump.git
   cd urban-lump

2. Requirements
🐍 Python 3.7+

Arduino IDE (to install serial drivers)

Mosquitto MQTT broker installed
👉 Download: https://mosquitto.org/download/

Install Python libraries:
    pip install websockets paho-mqtt pyserial

3. Connect Arduino
Plug in the Arduino UNO via USB and check the COM port in Device Manager under "Ports (COM & LPT)".
Update mqtt_subscriber.py:
    SERIAL_PORT = "COM3"  # Change to your actual port

4. Run the System
✅ Start the MQTT Broker
Open a terminal and run:
    mosquitto
✅ Start the WebSocket Server
    python websocket_server.py
✅ Start the MQTT Subscriber
    python mqtt_subscriber.py
✅ Open the Frontend in Browser
Open frontend/index.html in your browser.
Submit ON/OFF times in HH:MM (24hr) format.


author: KWIZERA Albert
Student, [RWANDA CODING ACADEMY]
Contact: k2albert123@gmail.com

