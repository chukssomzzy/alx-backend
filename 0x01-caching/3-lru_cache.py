#!/usr/bin/env python3
"""Least Recently Used Cache Implementation"""
from typing import Any, Tuple
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """Implementation of LRUCache"""
    def __init__(self):
        """LRUCache initialization"""
        self._access = 0
        self._access_keys = {}
        super().__init__()

    def put(self, key: str, item: Any) -> None:
        """Get a key and item from cache
        Args:
            key (str): identifies a value by a key
            value (Any): identifies
        """
        if not key or not item:
            return
        if len(self._access_keys) == self.MAX_ITEMS and \
                key not in self._access_keys:
            k, _ = self._get_min_access()
            del self.cache_data[k]
            del self._access_keys[k]
            print("DISCARD: {}".format(k))
        self._access_keys[key] = self._access
        self._access += 1
        self.cache_data[key] = item

    def _get_min_access(self) -> Tuple[str, int]:
        """Get the key with the lowest access"""
        return sorted(self._access_keys.items(), key=lambda x: x[1])[0]

    def get(self, key: str) -> Any:
        """Return an item identified by key from the cache"""
        if not key or key not in self.cache_data:
            return
        self._access_keys[key] = self._access
        self._access += 1
        return self.cache_data[key]
