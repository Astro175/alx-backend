#!/usr/bin/env python3

"""
Module that uses LRU cache system
"""
from base_caching import BaseCaching
import collections


class LRUCache(BaseCaching):
    """
     A class LRUCache that inherits from BaseCaching
     and is a LRU caching system
    """
    def __init__(self):
        """init method"""
        super().__init__()
        self.usedKeys = []

    def put(self, key, item):
        """
        Must assign to the dictionary self.cache_data
        the item value for the key key
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.usedKeys:
                self.usedKeys.append(key)
            else:
                self.usedKeys.append(
                    self.usedKeys.pop(self.usedKeys.index(key)))
            if len(self.usedKeys) > BaseCaching.MAX_ITEMS:
                discard = self.usedKeys.pop(0)
                del self.cache_data[discard]
                print('DISCARD: {:s}'.format(discard))

    def get(self, key):
        """
        Gets an item from the cache and updates recent
        """
        if key is not None and key in self.cache_data.keys():
            self.usedKeys.append(self.usedKeys.pop(self.usedKeys.index(key)))
            return self.cache_data.get(key)
        return None
