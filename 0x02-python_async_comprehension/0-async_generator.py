#!/usr/bin/env python3
'''coroutine async_generator that takes no arguments.
'''
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''this func makes a seq ten num.
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
