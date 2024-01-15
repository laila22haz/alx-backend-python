#!/usr/bin/env python3
"""The basics of async"""

import asyncio
from random import uniform


async def wait_random(max_delay=10) -> float:
    """function that Write an asynchronous coroutine"""
    random_number = uniform(0, max_delay)
    await asyncio.sleep(random_number)
    return random_number
