import asyncio
import sys

from bleak import BleakScanner


# Prints additional info to devices that are listed as Unknown by discover
async def main():
    devices = await BleakScanner.discover()
    for d in devices:
        d_splited_by_colon = str(d).split(':')
        d_splited_by_colon[0]
        device = await BleakScanner.find_device_by_address(
            d_splited_by_colon[0]
        )
        print(device)

if __name__ == "__main__":
    asyncio.run(main())
