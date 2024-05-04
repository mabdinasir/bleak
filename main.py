import asyncio
from scanner import scanner
from connect import connect

async def main():
    devices = await scanner()
    desired_device = next((d for d in devices if d.address == "135CB61E-49D2-2D37-0F50-0B7DA189328E"), None)
    MODEL_NBR_UUID = "00002a24-0000-1000-8000-00805f9b34fb"
    if desired_device:
        print(f"Connecting to {desired_device.name} - {desired_device.address}")
        await connect(desired_device.address, MODEL_NBR_UUID)
    else:
        print("Desired device not found.")

asyncio.run(main())
