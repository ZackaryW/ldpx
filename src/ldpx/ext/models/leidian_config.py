"""Data models for LDPlayer instance configuration.

This module defines TypedDict and dataclass models for LDPlayer instance
configuration files. These models represent the structure of configuration
JSON files stored in the LDPlayer installation directory.

Configuration Categories:
    - Hotkey settings: Keyboard shortcuts for various emulator functions
    - Resolution settings: Display resolution and DPI
    - Advanced settings: CPU, memory, audio device configuration
    - Basic settings: Window position and size
"""
from dataclasses import asdict, dataclass
from typing import TypedDict, Optional
import typing
from ldpx.ext.utils.dict import parse_dotted_dict, flatten_nested_dict


class HotkeySettings(TypedDict):
    """Hotkey configuration for emulator functions.
    
    Each hotkey is defined as a dictionary containing modifiers and key codes.
    """
    backKey: dict
    homeKey: dict
    appSwitchKey: dict
    menuKey: dict
    zoomInKey: dict
    zoomOutKey: dict
    bossKey: dict
    shakeKey: dict
    operationRecordKey: dict
    fullScreenKey: dict
    showMappingKey: dict
    videoRecordKey: dict
    mappingRecordKey: dict
    keyboardModelKey: dict


class KeyConfig(TypedDict):
    """Key configuration with modifiers.
    
    Attributes:
        modifiers: Bitfield of modifier keys (Ctrl, Alt, Shift, etc.).
        key: Virtual key code.
    """
    modifiers: int
    key: int


class ResolutionSettings(TypedDict):
    """Display resolution configuration.
    
    Attributes:
        width: Screen width in pixels.
        height: Screen height in pixels.
    """
    width: int
    height: int


class AdvancedSettings(TypedDict):
    """Advanced emulator configuration.
    
    Attributes:
        resolution: Display resolution settings.
        resolutionDpi: DPI (dots per inch) setting.
        cpuCount: Number of CPU cores allocated.
        memorySize: Memory size in MB.
        micphoneName: Name of the microphone device (optional).
        speakerName: Name of the speaker device (optional).
    """
    resolution: ResolutionSettings
    resolutionDpi: int
    cpuCount: int
    memorySize: int
    micphoneName: Optional[str]
    speakerName: Optional[str]


class BasicSettings(TypedDict):
    """Basic window and display settings.
    
    Attributes:
        left: X-coordinate of window position.
        top: Y-coordinate of window position.
        width: Window width.
        height: Window height.
        realHeigh: Actual display height.
        realWidth: Actual display width.
        isForstStart: Whether this is the first start (typo in original).
    """
    left: int
    top: int
    width: int
    height: int
    realHeigh: int
    realWidth: int
    isForstStart: bool
    mulFsAddSize: int
    mulFsAutoSize: int
    verticalSync: bool
    fsAutoSize: int
    noiceHypeVOpen: bool
    autoRun: bool
    rootMode: bool
    heightFrameRate: bool
    adbDebug: int
    autoRotate: bool
    isForceLandscape: bool
    standaloneSysVmdk: bool
    lockWindow: bool
    disableMouseFastOpt: bool
    cjztdisableMouseFastOpt_new: int
    HDRQuality: int
    qjcjdisableMouseFast: int
    fps: int
    astc: bool
    rightToolBar: bool


class NetworkSettings(TypedDict):
    networkEnable: bool
    networkSwitching: bool
    networkStatic: bool
    networkAddress: str
    networkGateway: str
    networkSubnetMask: str
    networkDNS1: str
    networkDNS2: str
    networkInterface: Optional[str]


class PropertySettings(TypedDict):
    phoneIMEI: str
    phoneIMSI: str
    phoneSimSerial: str
    phoneAndroidId: str
    phoneModel: str
    phoneManufacturer: str
    macAddress: str
    phoneNumber: Optional[str]


class StatusSettings(TypedDict):
    sharedApplications: str
    sharedPictures: str
    sharedMisc: str
    closeOption: int
    playerName: str


@dataclass
class LeidianConfig:
    propertySettings: PropertySettings
    statusSettings: StatusSettings
    basicSettings: BasicSettings
    networkSettings: NetworkSettings
    advancedSettings: typing.Optional[AdvancedSettings] = None
    hotkeySettings: typing.Optional[HotkeySettings] = None

    @classmethod
    def from_dict(cls, data: dict) -> "LeidianConfig":
        data = parse_dotted_dict(data)
        return cls(**data)

    def to_dict(self) -> dict:
        data = asdict(self)
        data = flatten_nested_dict(data)
        return data