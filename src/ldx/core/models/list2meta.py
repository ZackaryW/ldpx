"""Data models for LDPlayer emulator instance metadata.

This module defines the List2Meta TypedDict that represents metadata
for LDPlayer emulator instances, including process IDs, window handles,
and runtime status information.
"""
import typing


class List2Meta(typing.TypedDict):
    """Metadata for an LDPlayer emulator instance.
    
    Attributes:
        id: Unique identifier for the emulator instance.
        name: Display name of the emulator instance.
        top_window_handle: Handle to the top-level window.
        bind_window_handle: Handle to the bound window.
        android_started_int: Integer flag indicating if Android has started (1=running, 0=stopped).
        pid: Process ID of the emulator.
        pid_of_vbox: Process ID of the VirtualBox process.
    """
    id: int
    name: str
    top_window_handle: int
    bind_window_handle: int
    android_started_int: int
    pid: int
    pid_of_vbox: int


def list2alias(data: List2Meta) -> dict:
    """Create a dictionary with multiple alias keys for List2Meta fields.
    
    Provides convenient access to List2Meta fields using various naming conventions
    (camelCase, snake_case, abbreviated forms).
    
    Args:
        data: List2Meta instance to create aliases for.
        
    Returns:
        dict: Dictionary with all original keys plus their aliases.
    """
    return {
        "id": data["id"],
        "name": data["name"],
        "top_window_handle": data["top_window_handle"],
        "twh": data["top_window_handle"],
        "topWindowHandle": data["top_window_handle"],
        "bind_window_handle": data["bind_window_handle"],
        "bwh": data["bind_window_handle"],
        "bindWindowHandle": data["bind_window_handle"],
        "android_started_int": data["android_started_int"],
        "isStarted": data["android_started_int"],
        "pid": data["pid"],
        "pid_of_vbox": data["pid_of_vbox"],
        "vboxPid": data["pid_of_vbox"],
        "pidOfVbox": data["pid_of_vbox"],
    }