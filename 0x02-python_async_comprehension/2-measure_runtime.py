#!/usr/bin/env python3
"""Run time for four parallel comprehensions"""

import asyncio
import time
from typing import List


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    time_start = time.time()
    for _ in range(4):
        await asyncio.gather(async_comprehension())
    time_end = time.time()
    return time_end - time_start
