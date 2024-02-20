#!/usr/bin/env python3
'''Contains measure_runtime coroutine.'''
import asyncio
import time
from importlib import import_module as using


async_comprehension = using('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''Runs async_comprehension 4 times and calculates the runtime.'''
    start_time = time.time()
    await asyncio.gather(
        *(async_comprehension() for _ in range(4))
    )

    return time.time() - start_time
