"""Data models for LDPlayer keyboard mapping configuration (KMP files).

This module defines dataclass models for keyboard mapping files used by
LDPlayer. KMP files define how keyboard inputs are mapped to touch screen
actions, gestures, and other Android inputs.

Keyboard Mapping Types:
    - Point mappings: Single touch at a specific point
    - Curve mappings: Swipe/gesture along a path
    - Resolution patterns: Different mappings per resolution
"""
from dataclasses import dataclass, field, asdict
from typing import List, Union


@dataclass(slots=True)
class Point:
    """A 2D point coordinate.
    
    Attributes:
        x: X-coordinate.
        y: Y-coordinate.
    """
    x: int
    y: int


@dataclass(slots=True)
class CurvePoint:
    """A point along a curve/gesture path with timing.
    
    Attributes:
        x: X-coordinate.
        y: Y-coordinate.
        timing: Timestamp of this point in the gesture (milliseconds).
    """
    x: int
    y: int
    timing: int


@dataclass(slots=True)
class ResolutionPattern:
    """Resolution specification for resolution-dependent mappings.
    
    Attributes:
        width: Screen width in pixels.
        height: Screen height in pixels.
    """
    width: int
    height: int


@dataclass
class BaseKeyboardData:
    """Base class for keyboard mapping data.
    
    Attributes:
        key: Primary key code.
        secondKey: Secondary/modifier key code.
        extraData: Additional data string.
        description: User-visible description.
        moreDescription: Extended description.
        hintVisible: Whether to show the hint overlay.
        hintOffset: Offset for hint display position.
    """
    key: int
    secondKey: int
    extraData: str = ""
    description: str = ""
    moreDescription: str = ""
    hintVisible: bool = True
    hintOffset: Point = field(default_factory=lambda: Point(x=0, y=0))


@dataclass
class KeyboardCurveData(BaseKeyboardData):
    """Keyboard mapping that follows a curve/gesture path.
    
    Used for swipe gestures, drag operations, etc.
    
    Attributes:
        curve: List of points defining the gesture path.
    """
    curve: List[CurvePoint] = field(default_factory=list)


@dataclass
class KeyboardPointData(BaseKeyboardData):
    """Keyboard mapping for single-point touch actions.
    
    Used for simple tap/press actions at a specific location.
    
    Attributes:
        point: The touch point location.
        type: Mapping type identifier.
        downDuration: Duration of press-down action (milliseconds).
        upDuration: Duration of release action (milliseconds).
        downDurationEx: Extended press-down duration.
        upDurationEx: Extended release duration.
    """
    point: Point = field(default_factory=lambda: Point(x=0, y=0))
    type: int = 0
    downDuration: int = 0
    upDuration: int = 0
    downDurationEx: int = 0
    upDurationEx: int = 0


@dataclass
class KeyboardEntry:
    class_name: str
    data: Union[KeyboardCurveData, KeyboardPointData]

    @classmethod
    def from_dict(cls, data: dict) -> "KeyboardEntry":
        # Rename 'class' to 'class_name' if present
        if "class" in data:
            data["class_name"] = data.pop("class")
        if "curve" in data["data"]:
            data["data"] = KeyboardCurveData(**data["data"])
        else:
            data["data"] = KeyboardPointData(**data["data"])
        return cls(**data)

    def to_dict(self) -> dict:
        """Converts the KeyboardEntry object to a dictionary, handling any necessary field renames for external use."""
        result = asdict(self)
        result["class"] = result.pop("class_name")
        return result


@dataclass
class ConfigInfo:
    version: int = 0
    versionMessage: str = ""
    packageNameType: int = 0
    packageNamePattern: str = ""
    resolutionType: int = 0
    resolutionPattern: ResolutionPattern = field(
        default_factory=lambda: ResolutionPattern(width=0, height=0)
    )
    priority: int = 0
    search: str = ""


@dataclass
class KeyboardConfig:
    mouseCenter: Point = field(default_factory=lambda: Point(x=0, y=0))
    mouseScrollType: int = 0
    discType: int = 0
    advertising: bool = False
    advertiseDuration: int = 0
    advertiseText: str = ""
    cancelPoint: Point = field(default_factory=lambda: Point(x=0, y=0))
    cancelKey: int = 0
    cancelMode: int = 0
    cursor: str = "defaultCursor"
    extraData: str = ""


@dataclass
class KeyboardMapping:
    configInfo: ConfigInfo
    keyboardConfig: KeyboardConfig
    keyboardMappings: List[KeyboardEntry] = field(default_factory=list)

    @classmethod
    def from_dict(cls, data: dict) -> "KeyboardMapping":
        configInfo = ConfigInfo(**data["configInfo"])
        keyboardConfig = KeyboardConfig(**data["keyboardConfig"])
        keyboardMappings = [
            KeyboardEntry.from_dict(entry) for entry in data["keyboardMappings"]
        ]
        return cls(
            keyboardMappings=keyboardMappings,
            configInfo=configInfo,
            keyboardConfig=keyboardConfig,
        )

    def to_dict(self) -> dict:
        configInfo = asdict(self.configInfo)
        keyboardConfig = asdict(self.keyboardConfig)
        keyboardMappings = [entry.to_dict() for entry in self.keyboardMappings]
        return {
            "configInfo": configInfo,
            "keyboardConfig": keyboardConfig,
            "keyboardMappings": keyboardMappings,
        }