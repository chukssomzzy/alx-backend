#!/usr/bin/env python3
"""Most Recently Used Cache Implementation"""
from typing import Any, Tuple
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """implements mru cache"""
    def __init__(self):
        """Intializes the mru cache"""
        self._access = 0
        self._access_key = {}
        super().__init__()

    def put(self, key: str, item: Any) -> None:
        """Put an item in the cache
        Args:
            key (str): identifier for item
            item (Any): item to be cached
        Returns:
            None
        """
        if not key or not item:
            return
        if len(self._access_key) == self.MAX_ITEMS and \
                key not in self._access_key:
            k, _ = self._get_max_key()
            del self.cache_data[k]
            del self._access_key[k]
            print("DISCARD: {}".format(k))
        self._access_key[key] = self._access
        self._access += 1
        self.cache_data[key] = item

    def _get_max_key(self) -> Tuple[str, int]:
        """Return max accessed key"""
        return sorted(self._access_key.items(), key=lambda x: x[1])[-1]

    def get(self, key: str) -> Any:
        """Returns item from cache"""
        if not key or key not in self.cache_data:
            return
        self._access_key[key] = self._access
        self._access += 1
        return self.cache_data[key]
