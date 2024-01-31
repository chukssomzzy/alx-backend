#!/usr/bin/env python3
"""Least Frequently used item in cache implementation"""

from typing import Any, Tuple
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """Implements LFU cache policy"""
    def __init__(self):
        """Initializes LFUCache"""
        self._freq_key = {}
        super().__init__()

    def put(self, key: str, item: Any) -> None:
        """Put an item in the cache"""
        if not key or not item:
            return
        if len(self._freq_key) == self.MAX_ITEMS and \
                key not in self._freq_key:
            k, _ = self._get_min_freq_item()
            del self.cache_data[k]
            del self._freq_key[k]
            print("DISCARD: {}".format(k))
        self._freq_key[key] = 0
        self.cache_data[key] = item

    def _get_min_freq_item(self) -> Tuple[str, int]:
        """Return item with the minimum frequency of access"""
        return sorted(self._freq_key.items(), key=lambda x: x[1])[0]

    def get(self, key) -> Any:
        """Return item identified by key
        Args:
            key (str): str identifier
        Returns:
            None or key
        """
        if not key or key not in self._freq_key:
            return
        self._freq_key[key] += 1
        return self.cache_data[key]
