import asyncio
from bleak import BleakClient

from scanner import scanner

async def connect(address, MODEL_NBR_UUID):
    try:
        async with BleakClient(address) as client:
            if MODEL_NBR_UUID not in client.services.characteristics:
                raise ValueError(f"Characteristic {MODEL_NBR_UUID} was not found on the device.")
            
            model_number = await client.read_gatt_char(MODEL_NBR_UUID)
            if model_number:
                print("Model Number: {0}".format("".join(map(chr, model_number))))
            else:
                print("Failed to read model number.")

    except Exception as e:
        print(f"Failed to connect to device at address {address}: {e}")
