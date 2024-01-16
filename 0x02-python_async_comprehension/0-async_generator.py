#!/usr/bin/env python3
"""Async Generator"""

import asyncio
from random import uniform
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """coroutine will loop 10 times, each time asynchronously wait 1 second"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)
