#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import Dict, List, Optional


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            # truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: Optional[int] = None,
                        page_size: int = 10) -> Dict:
        """Get hypermedia by seek pagination"""
        ds = self.indexed_dataset()
        dl = len(ds)
        index = index if index else 0
        assert type(page_size) is int and type(index) is int
        assert index >= 0 and page_size > 0
        assert index + (page_size) <= dl

        data = []
        for i in range(index, (index + page_size)):
            if i in ds:
                data.append(ds[i])
        return {
            "index": index,
            "next_index": index + page_size,
            "page_size": page_size,
            "data": data
        }
