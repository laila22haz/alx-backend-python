#!/usr/bin/env python3
"""9. Let's duck type an iterable object"""

from typing import Tuple, List, Sequence


def element_length(lst: List[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    - lst (list) : list
    Return :
    """
    return [(i, len(i)) for i in lst]
