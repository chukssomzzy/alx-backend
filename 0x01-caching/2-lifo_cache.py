#!/usr/bin/env python3
"""LIFO cache implementation
"""
from collections import deque
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """implements LIFOCache"""

    def __init__(self):
        """Initialize LIFOCache"""
        self._stack = deque(maxlen=self.MAX_ITEMS)
        super().__init__()

    def put(self, key, item):
        """Add item to the stack

        Args:
            key (str): identifier for an item in stackk
            item: item to put in cache
        """
        if not key or not item:
            return

        if len(self._stack) == self.MAX_ITEMS and key not in self.cache_data:
            stack_key = self._stack.pop()
            del self.cache_data[stack_key]
            print("DISCARD: {}".format(stack_key))
        if key not in self.cache_data:
            self._stack.append(key)
        else:
            self._stack.remove(key)
            self._stack.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """Get an item identified by key from cache
        Args:
            key: identifier to the item to get from cache if exists
        Returns:
            if key exists in cache return item else None
        """
        if not key or key not in self.cache_data:
            return
        return self.cache_data[key]
