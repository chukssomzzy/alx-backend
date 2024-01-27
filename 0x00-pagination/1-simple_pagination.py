#!/usr/bin/env python3
"""Simple Pagination"""
import csv
from typing import List, Optional, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Paginate start and end index
    Args:
        page (int): the page start from
        page_size (int): page size
    Return:
        A tuple with start and end index
    """
    return ((page - 1) * page_size, ((page - 1) * page_size) + page_size)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset: Optional[List[List]] = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0
        i, j = index_range(page, page_size)

        dataset = self.dataset()
        if j < len(dataset) or i > len(dataset):
            return dataset[i:j]
        return []
