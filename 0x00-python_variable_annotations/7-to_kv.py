#!/usr/bin/env python3
"""7. Complex types - string and int/float to tuple"""

from typing import List, Union, Set, Dict, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    - k (str): string
    - v (int | float): Union[int, float
    Return : tuple result
    """
    return (k, pow(v, 2))
