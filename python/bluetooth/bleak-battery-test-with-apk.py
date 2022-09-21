import asyncio
from bleak import BleakScanner, BleakClient
from PyObjCTools import KeyValueCoding

uuid_battery_service = '0000180f-0000-1000-8000-00805f9b34fb'
uuid_battery_level_characteristic = '00002a19-0000-1000-8000-00805f9b34fb'


async def main():

    devices = await BleakScanner.discover()
    for d in devices:
        if KeyValueCoding.getKey(d.details,'name') == 'Galaxy M53 5G':
            myDevice = d
            print('Found it')
            
        address = str(KeyValueCoding.getKey(myDevice.details,'identifier'))

    async with BleakClient(address) as client:
        svcs = await client.get_services()
        print("Services:")
        for service in svcs:
            print(service)

        address = str(KeyValueCoding.getKey(myDevice.details,'identifier'))

    async with BleakClient(address) as client:
        svcs = await client.get_services()
        battery_level = await client.read_gatt_char(uuid_battery_level_characteristic)
        print(int.from_bytes(battery_level,byteorder='big'))

asyncio.run(main())