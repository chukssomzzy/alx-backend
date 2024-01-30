#!/usr/bin/env python3
"""Implements a FIFO cache"""

from typing import Any
import queue
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Implements a first in first out cache"""

    def __init__(self):
        """initialize the fifo queue"""
        self._queue = queue.Queue(maxsize=self.MAX_ITEMS)
        super().__init__()

    def put(self, key: str, item: Any) -> None:
        """Add an item to cache
        Args:
            key (str): identifier to the value to be added to cache
            item (Any): item to be added to the cache
        Returns:
             None
        """
        if not key or not item:
            return
        if self._queue.full() and key not in self.cache_data:
            queue_key = self._queue.get()
            del self.cache_data[queue_key]
            print("DISCARD: {}".format(queue_key))
        if key not in self.cache_data:
            self._queue.put(key)
        self.cache_data[key] = item

    def get(self, key: str) -> Any:
        """Get an item from the FIFOcache
        Args:
            key (str): identifier to the value to get from cache
        Returns:
            None
        """
        if not key or key not in self.cache_data:
            return
        return self.cache_data[key]
