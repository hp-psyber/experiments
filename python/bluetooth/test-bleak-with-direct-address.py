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
    "56:21:1C:BE:DD:44"
    if platform.system() != "Darwin"
    else "B9EA5233-37EF-4DD6-87A8-2A875E821C46"
)

async def main(wanted_name: str):
    device = await BleakScanner.find_device_by_filter(
        lambda d, ad: d.name and d.name.lower() == wanted_name.lower()
    )
    print(device)
    splitted_string = str(device).split()
    address = splitted_string[0]
    address = address[:-1]

    if(address != 'Non'):
        async with BleakClient(address) as client:
            battery_level = await client.read_gatt_char(uuid_battery_level_characteristic)
            print(int.from_bytes(battery_level,byteorder='big'))
    else:
        print('BLE name not found')

    


if __name__ == "__main__":
    asyncio.run(main(sys.argv[1] if len(sys.argv) == 2 else "Galaxy M53 5G"))