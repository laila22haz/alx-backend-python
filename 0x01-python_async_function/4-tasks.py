#!/usr/bin/env python3
"""Tasks"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ new function task_wait_n"""
    list = []
    for x in range(n):
        list.append((task_wait_random(max_delay)))
        delay = await asyncio.gather(*list)
    return sorted(delay)
