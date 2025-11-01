"""Data models for macro/script recording in ext module.

This module provides ext-specific record models. Note that similar models
exist in ldpx.core.models.record - this module is for extended functionality.
"""
from dataclasses import dataclass, field
from typing import List, Optional, TypedDict


@dataclass
class Point:
    """A touch point in a recorded operation.
    
    Attributes:
        id: Unique identifier for the point.
        x: X-coordinate of the touch point.
        y: Y-coordinate of the touch point.
        state: Optional state value for the point.
    """
    id: int
    x: int
    y: int
    state: Optional[int] = None


@dataclass
class Operation:
    """A recorded operation (touch, swipe, text input, etc.).
    
    Attributes:
        timing: Timestamp of when the operation occurs.
        operationId: Unique identifier for the operation type.
        points: List of touch points involved in the operation.
        text: Optional text data (for text input operations).
    """
    timing: int
    operationId: str
    points: List[Point] = field(default_factory=list)
    text: Optional[str] = field(default=None)


class RecordInfo(TypedDict):
    """Metadata for a recorded macro/script.
    
    Attributes:
        loopType: Type of loop (0=no loop, 1=count, 2=duration).
        loopTimes: Number of times to loop.
        circleDuration: Duration of each loop cycle.
        loopInterval: Interval between loop iterations.
        loopDuration: Total duration of looping.
        accelerateTimes: Playback speed multiplier.
        accelerateTimesEx: Extended acceleration setting.
        recordName: Name of the recorded macro.
        createTime: ISO timestamp of when the recording was created.
        playOnBoot: Whether to play this macro on emulator boot.
        rebootTiming: Timing for rebooting during playback.
    """
    loopType: int
    loopTimes: int
    circleDuration: int
    loopInterval: int
    loopDuration: int
    accelerateTimes: int
    accelerateTimesEx: int
    recordName: str
    createTime: str
    playOnBoot: bool
    rebootTiming: int


class ReturnInfo(TypedDict):
    """Information returned from record operations.
    
    Attributes:
        file: Path to the recording file.
        info: Metadata about the recording.
    """
    file: str
    info: RecordInfo


@dataclass
class Record:
    """A complete recorded macro/script with metadata and operations.
    
    Attributes:
        recordInfo: Metadata about the recording.
        operations: List of operations in the recording.
    """
    recordInfo: RecordInfo
    operations: List[Operation] = field(default_factory=list)