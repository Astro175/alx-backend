#!/usr/bin/env python3

"""
  A caching system that uses LIFO algorithm
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
     A class LIFOCache that inherits from BaseCaching
     and is a caching system
    """
    def __init__(self):
        """Init method"""
        super().__init__()

    def put(self, key, item):
        """
          Adds a key-value to the cache, but uses LIFO
          algorithm to update the cache
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= LIFOCache.MAX_ITEMS \
                and key not in self.cache_data.keys():
            last = list(self.cache_data.keys())[-1]
            self.cache_data.pop(last)
            print("DISCARD: {}".format(last))
        self.cache_data[key] = item

    def get(self, key):
        """
           Gets an item from a given key in the cache
        """
        keysList = list(self.cache_data.keys())
        if key is None or key not in keysList:
            return None
        item = self.cache_data.get(key)
        return item
