#!/usr/bin/env python3
"""Let's execute multiple coroutines at the same time with async"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Create a list of coroutine objects for wait_random"""
    list = [wait_random(max_delay) for x in range(n)]
    delay = await asyncio.gather(*list)
    return sorted(delay)
