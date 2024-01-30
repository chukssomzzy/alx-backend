#!/usr/bin/env python3

"""Basic caching"""
from typing import Any
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Caching system
    """
    def put(self, key: str, item: Any) -> None:
        """Add item to the cache
        Args:
            key (str): identifier for the value to put in the cache
            value (any): value to put in the cache
        """
        if not key or not item:
            return
        self.cache_data[key] = item

    def get(self, key: str) -> Any:
        """Get an item from cache
        Args:
            key (str): identifies an item to be removed from cache

        """
        if not key or key not in self.cache_data:
            return
        return self.cache_data[key]
