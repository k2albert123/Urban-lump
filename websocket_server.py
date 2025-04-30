import asyncio
import websockets
import json
import subprocess

# MQTT configuration
MQTT_TOPIC = "light/schedule"
MQTT_BROKER = "localhost"  # change if using a different broker address

async def handler(websocket):
    async for message in websocket:
        print(f"Received schedule: {message}")
        try:
            schedule = json.loads(message)
            on_time = schedule.get("on")
            off_time = schedule.get("off")

            # Validate times
            if not on_time or not off_time:
                await websocket.send("Error: Missing schedule fields.")
                continue

            mqtt_payload = json.dumps({"on": on_time, "off": off_time})

            # Use mosquitto_pub to send MQTT message
            subprocess.run([
                "mosquitto_pub",
                "-h", MQTT_BROKER,
                "-t", MQTT_TOPIC,
                "-m", mqtt_payload
            ])

            await websocket.send("Schedule forwarded to MQTT.")
            print(f"Published to MQTT: {mqtt_payload}")

        except json.JSONDecodeError:
            await websocket.send("Invalid JSON format.")

async def main():
    async with websockets.serve(handler, "localhost", 8765):
        print("WebSocket server running on ws://localhost:8765")
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
