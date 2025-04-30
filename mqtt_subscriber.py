import paho.mqtt.client as mqtt
import serial
import time
import json
from datetime import datetime

# === CONFIGURATION ===
MQTT_BROKER = "localhost"
MQTT_TOPIC = "light/schedule"
SERIAL_PORT = "COM3"      # Replace with your Arduino port (e.g., COM4, /dev/ttyUSB0)
BAUD_RATE = 9600

# === STATE ===
on_time = None
off_time = None

# Connect to Arduino
try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    print(f"Connected to Arduino on {SERIAL_PORT}")
except Exception as e:
    print(f"Serial connection failed: {e}")
    ser = None

# MQTT Callback
def on_message(client, userdata, msg):
    global on_time, off_time
    try:
        payload = msg.payload.decode()
        schedule = json.loads(payload)
        on_time = schedule.get("on")
        off_time = schedule.get("off")
        print(f"Received schedule: ON={on_time}, OFF={off_time}")
    except Exception as e:
        print(f"Failed to parse message: {e}")

# MQTT Setup
client = mqtt.Client()
client.connect(MQTT_BROKER, 1883, 60)
client.subscribe(MQTT_TOPIC)
client.on_message = on_message
client.loop_start()

print("Listening for schedules...")

# === Main Loop ===
try:
    while True:
        now = datetime.now().strftime("%H:%M")
        if ser:
            if on_time == now:
                ser.write(b'1')
                print(f"[{now}] Sent ON (1) to Arduino")
                time.sleep(60)  # Prevent multiple triggers in one minute
            elif off_time == now:
                ser.write(b'0')
                print(f"[{now}] Sent OFF (0) to Arduino")
                time.sleep(60)
        time.sleep(1)
except KeyboardInterrupt:
    print("Shutting down...")
finally:
    if ser:
        ser.close()
    client.loop_stop()
    client.disconnect()
