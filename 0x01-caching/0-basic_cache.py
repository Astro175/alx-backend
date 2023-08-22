#!/usr/bin/env python3

"""
  A module that implements a basic caching system
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    A class BasicCache that inherits from BaseCaching
    and is a caching system
    """
    def put(self, key, item):
        """
        Must assign to the dictionary self.cache_data the item
        value for the key
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        keysList = list(self.cache_data.keys())
        if key is None or key not in keysList:
            return None
        item = self.cache_data.get(key)
        return item
