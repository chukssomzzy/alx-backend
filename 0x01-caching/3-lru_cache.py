#!/usr/bin/env python3
"""Least Recently Used Cache Implementation"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """Implementation of LRUCache"""
    def __init__(self):
        """LRUCache initialization"""
        self._access = 0
        self._accessKeys = {}
        super().__init__()

    def put(self, key, item):
        """Get a key and item from cache
        Args:
            key (str): identifies a value by a key
            value (Any): identifies
        """
        if len(self._accessKeys) == self.MAX_ITEMS and \
                key not in self._accessKeys:
            k, _ = self._getMinAccess()
            del self.cache_data[k]
            del self._accessKeys[k]
            print("DISCARD: {}".format(k))
        self._accessKeys[key] = self._access
        self._access += 1
        self.cache_data[key] = item

    def _getMinAccess(self):
        """Get the key with the lowest access"""
        return sorted(self._accessKeys.items(), key=lambda x: x[1])[0]

    def get(self, key):
        """Return an item identified by key from the cache"""
        if not key or key not in self.cache_data:
            return
        self._accessKeys[key] = self._access
        self._access += 1
        return self.cache_data[key]
