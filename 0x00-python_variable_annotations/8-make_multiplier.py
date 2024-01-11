#!/usr/bin/env python3
"""8. Complex types - functions"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    - multiplier (float): float
    Return : float result
    """
    def multiple(n: float) -> float:
        return n * multiplier
    return multiple
