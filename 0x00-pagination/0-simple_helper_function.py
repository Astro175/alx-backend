#!/usr/bin/env python3
from typing import Tuple
"""
The module should return a tuple of size two containing a start index
and an end index corresponding to the range of indexes to return in a
list for those particular pagination parameters
"""


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    This function returns start_index and end_index for a range
    in a particular pagination parameters
    """
    start_index = (page - 1) * page_size
    end_index = page_size * page
    return (start_index, end_index)
