#!/usr/bin/env python3
"""
simple paginate helper
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Paginate start and end index
    Args:
        page (int): the page start from
        page_size (int): page size
    Return:
        A tuple with start and end index
    """
    return ((page - 1) * page_size, ((page - 1) * page_size) + page_size)
