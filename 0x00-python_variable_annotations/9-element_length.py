#!/usr/bin/env python3
"""9. Let's duck type an iterable object"""

from typing import Tuple, List, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    - lst (list) : list
    Return :
    """
    return [(i, len(i)) for i in lst]
