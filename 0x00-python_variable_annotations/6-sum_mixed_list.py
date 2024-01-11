#!/usr/bin/env python3
"""6. Complex types - mixed list"""

from typing import List, Union, Set, Dict, Tuple


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    - input_list (List): List
    Return : float result
    """
    return sum(mxd_lst)
