"""
Connect by BLEDevice
"""

import asyncio
import platform
import sys

from bleak import BleakClient, BleakScanner
from bleak.exc import BleakError

uuid_battery_service = '0000180f-0000-1000-8000-00805f9b34fb'
uuid_battery_level_characteristic = '00002a19-0000-1000-8000-00805f9b34fb'

ADDRESS = (
    "7D:CB:9E:85:A7:A1"
    if platform.system() != "Darwin"
    else "B9EA5233-37EF-4DD6-87A8-2A875E821C46"
)


async def main(ble_address: str):
    device = await BleakScanner.find_device_by_address(ble_address, timeout=20.0)
    if not device:
        raise BleakError(f"A device with address {ble_address} could not be found.")
    
    async with BleakClient(device) as client:
        print("Services:")
        for service in client.services:
            print(service)
    address = ble_address

    async with BleakClient(address) as client:
        svcs = await client.get_services()
        print("Services:")
        for service in svcs:
            print(service)

    async with BleakClient(address) as client:
        svcs = await client.get_services()
        battery_level = await client.read_gatt_char(uuid_battery_level_characteristic)
        print(int.from_bytes(battery_level,byteorder='big'))


if __name__ == "__main__":
    asyncio.run(main(sys.argv[1] if len(sys.argv) == 2 else ADDRESS))