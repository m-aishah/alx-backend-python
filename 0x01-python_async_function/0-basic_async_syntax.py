'''Contains coroutine that waits for a random number of seconds.'''

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    '''
    Waits for a random number of seconds.
    '''
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)

    return wait_time
