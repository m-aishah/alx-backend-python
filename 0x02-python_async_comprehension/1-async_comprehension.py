#!/usr/bin/env python3
'''Contais async_comprehension coroutine.'''
from typing import List
from importlib import import_module as using


async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''Creates a list of 10 numbers from async_generator.'''
    return [num async for num in async_generator()]
