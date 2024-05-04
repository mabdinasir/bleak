import asyncio
import warnings
from bleak import BleakScanner

async def scanner():
    devices = await BleakScanner.discover()
    desired_device = next((d for d in devices if d.name == "MINI-02-2F6A"), None)
    if desired_device:
        print("Device Information:")
        print(f"  Name: {desired_device.name}")
        print(f"  Address: {desired_device.address}")
        # Suppress FutureWarning for BLEDevice.rssi
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=FutureWarning)
            print(f"  RSSI: {desired_device.rssi}")
            print(f"  Detals: {desired_device.details}")
            print("  Advertisement data:")
            print(f"    - UUIDs: {desired_device.metadata['uuids']}")
            print("    - Manufacturer Data:")
            for key, value in desired_device.metadata['manufacturer_data'].items():
                print(f"        - {key}: {value}")
        # return devices
    else:
        print("MINI-02-2F6A device not found.")

asyncio.run(scanner())

