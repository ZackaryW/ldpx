"""Data models for LDPlayer settings metadata (SMP files).

This module defines the SMP (Settings MetaData Profile) TypedDict which
stores user preferences and UI state for keyboard/joystick mapping features.
"""
from typing import TypedDict


class SMP(TypedDict):
    """Settings metadata profile for mapping features.
    
    Attributes:
        reduceInertia: Whether to reduce input inertia.
        keyboardShowGreet: Show greeting message for keyboard mapping.
        joystickShowGreet: Show greeting message for joystick mapping.
        keyboardFirstGreet: First-time greeting shown for keyboard.
        joystickFirstGreet: First-time greeting shown for joystick.
        keyboardShowHints: Show keyboard mapping hints overlay.
        joystickShowHints: Show joystick mapping hints overlay.
        keyboardIgnoreVersion: Keyboard mapping version to ignore updates for.
        joystickIgnoreVersion: Joystick mapping version to ignore updates for.
        noticeTimes: Number of times notices have been shown.
        noticeHash: Hash of the last shown notice.
        resolutionRelatives: Resolution-relative settings dictionary.
    """
    reduceInertia: bool
    keyboardShowGreet: bool
    joystickShowGreet: bool
    keyboardFirstGreet: bool
    joystickFirstGreet: bool
    keyboardShowHints: bool
    joystickShowHints: bool
    keyboardIgnoreVersion: int
    joystickIgnoreVersion: int
    noticeTimes: int
    noticeHash: int
    resolutionRelatives: dict