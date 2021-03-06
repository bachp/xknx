"""Example for Sensor device."""
import asyncio
from xknx import XKNX
from xknx.devices import Sensor, BinarySensor


async def main():
    """Connect to KNX/IP device and read the value of a temperature and a motion sensor."""
    xknx = XKNX()
    await xknx.start()

    sensor1 = BinarySensor(
        xknx,
        'DiningRoom.Motion.Sensor',
        group_address='6/0/2',
        device_class='motion')
    await sensor1.sync()
    print(sensor1)

    sensor2 = Sensor(
        xknx,
        'DiningRoom.Temperatur.Sensor',
        group_address='6/2/1',
        value_type='float',
        device_class='temperature')
    await sensor2.sync()
    print(sensor2)

    await xknx.stop()


# pylint: disable=invalid-name
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
