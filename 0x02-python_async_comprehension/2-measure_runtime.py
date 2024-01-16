#!/usr/bin/env python3
"""Run time for four parallel comprehensions"""

import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measure_runtime should measure the total runtime and return it"""
    time_start = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension()
                         )
    time_end = time.perf_counter()
    return time_end - time_start
