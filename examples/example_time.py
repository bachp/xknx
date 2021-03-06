"""Example for Time device."""
import asyncio
from xknx import XKNX
from xknx.devices import Time


async def main():
    """Connect to KNX/IP device and broadcast time."""
    xknx = XKNX()
    time = Time(xknx, 'TimeTest', group_address='1/2/3')
    xknx.devices.add(time)
    print("Sending time to KNX bus every hour")
    await xknx.start(daemon_mode=True, state_updater=True)
    await xknx.stop()

# pylint: disable=invalid-name
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
