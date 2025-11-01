"""JSON file utilities for configuration management.

This module provides utilities for working with JSON configuration files,
including automatic file creation with default data and safe loading/saving.
"""
import json
import pathlib

def touch_json(path, default_data = {}):
    """Load a JSON file, creating it with default data if it doesn't exist.
    
    Args:
        path: Path to the JSON file (string or Path object).
        default_data: Default data to write if file doesn't exist (default: {}).
        
    Returns:
        dict or list: The loaded JSON data from the file.
        
    Note:
        Creates parent directories if they don't exist.
        Uses UTF-8 encoding with pretty-printed JSON.
    """
    path = pathlib.Path(path)

    if not path.exists():
        with open(path, "w", encoding="utf-8") as f:
            json.dump(default_data, f, indent=4, ensure_ascii=False)

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

def save_json(path, data):
    """Save data to a JSON file with pretty formatting.
    
    Args:
        path: Path to the JSON file (string or Path object).
        data: Data to save (must be JSON-serializable).
        
    Note:
        Uses UTF-8 encoding with 4-space indentation.
        Non-ASCII characters are preserved (ensure_ascii=False).
    """
    path = pathlib.Path(path)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)    