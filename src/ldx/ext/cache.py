"""File caching system with LFU eviction policy.

This module provides a caching layer for JSON configuration files with
automatic eviction using a Least Frequently Used (LFU) policy. Files are
cached in memory and automatically reloaded when modified.

Cache Features:
    - Automatic file loading with mtime tracking
    - LFU eviction when cache is full
    - Access count tracking for each cached file
    - Configurable cache size (default: 1000 files)
"""

import json
import os
import typing

from ldx.core.objs.attr import LDAttr


class FileMeta(typing.TypedDict):
    """Metadata for a cached file.
    
    Attributes:
        mtime: Last modification time of the file.
        ac: Access count (number of times the file has been accessed).
    """
    mtime : int
    ac : int # access count


class AttrMeta(type):
    """Metaclass for managing the file cache.
    
    Class Attributes:
        _opened_files: Dictionary of cached file data.
        _opened_meta: Dictionary of file metadata (mtime, access count).
        _kv: Key-value cache storage.
        _kv_meta: Metadata for key-value cache.
        _total_cached: Maximum number of files to cache (default: 1000).
    """
    _opened_files : typing.Dict[str, dict | list] = {}
    _opened_meta : typing.Dict[str, FileMeta] = {}

    _kv : typing.Dict[str, dict | list] = {}
    _kv_meta : typing.Dict[str, FileMeta] = {}

    _total_cached : int = 1000

class AttrMixin(metaclass=AttrMeta):
    """Mixin class for adding file caching capabilities.
    
    This mixin provides automatic caching of JSON files with LFU eviction.
    Subclasses can use _loadFile() to load and cache JSON files efficiently.
    
    Args:
        path: Either a string path or LDAttr instance.
    """
    def __init__(self, path : typing.Union[str, LDAttr]):
        if isinstance(path, str):
            self.attr = LDAttr(path)
        else:
            self.attr = path

    def __real_load__(self, path : str):
        """Perform the actual file loading and cache storage.
        
        Args:
            path: Path to the JSON file to load.
            
        Returns:
            dict or list: Loaded JSON data.
            
        Note:
            Automatically evicts least frequently used files when cache is full.
        """
        
        # eviction - need to make room for the new file
        if len(AttrMeta._opened_files) >= AttrMeta._total_cached:
            # evict least accessed (LFU - Least Frequently Used)
            sorted_meta = sorted(
                AttrMeta._opened_meta.items(),
                key=lambda item: item[1]["ac"]
            )
            # +1 to make room for the new file we're about to add
            num_to_evict = len(AttrMeta._opened_files) - AttrMeta._total_cached + 1
            to_evict = sorted_meta[:num_to_evict]
            for evict_path, _ in to_evict:
                del AttrMeta._opened_files[evict_path]
                del AttrMeta._opened_meta[evict_path]

        # actual load

        with open(path, "r") as f:
            raw = f.read()
        data = json.loads(raw)
        AttrMeta._opened_files[path] = data
        AttrMeta._opened_meta[path] = FileMeta(
            mtime = os.path.getmtime(path),
            ac = 1
        )

        return data
    

    def _loadFile(self, path : str):
        """Load a JSON file with automatic caching and staleness detection.
        
        Checks if the file is already cached and up-to-date (by comparing mtime).
        If cached and fresh, returns cached data. Otherwise, loads from disk.
        
        Args:
            path: Path to the JSON file to load.
            
        Returns:
            dict, list, or None: Loaded JSON data, or None if file doesn't exist.
            
        Note:
            Increments access count for cache eviction algorithm.
        """
        # if file no longer exists
        if not os.path.exists(path):
            if path in AttrMeta._opened_files:
                del AttrMeta._opened_files[path]
            if path in AttrMeta._opened_meta:
                del AttrMeta._opened_meta[path]
            return None

        if path in AttrMeta._opened_files and AttrMeta._opened_meta.get(path, {}).get("mtime", 0) == os.path.getmtime(path):
            AttrMeta._opened_meta[path]["ac"] += 1
            return AttrMeta._opened_files[path]

        raw = self.__real_load__(path)
        return raw

    