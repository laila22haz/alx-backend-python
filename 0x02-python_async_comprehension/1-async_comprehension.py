#!/usr/bin/env python3
"""Async Comprehensions"""

import asyncio
from random import uniform
from typing import List


async_generator = __import__('0-async_generator').async_generator


def async_comprehension() -> List:
    """collect 10 random numbers using an async comprehensing"""
    return [number for number in async_generator()]
