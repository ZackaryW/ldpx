"""Data models for LDPlayer global configuration (leidians.config).

This module defines the LeidiansConfig dataclass which represents the main
configuration file for all LDPlayer instances. This file stores global
settings, window management preferences, and multi-instance options.
"""
from dataclasses import asdict, dataclass
from typing import TypedDict
import typing
from ldpx.ext.utils.dict import parse_dotted_dict, flatten_nested_dict


class WindowsPosition(TypedDict):
    """Window position coordinates.
    
    Attributes:
        x: X-coordinate.
        y: Y-coordinate.
    """
    x: int
    y: int


class BasicSettings(TypedDict):
    """Basic global settings.
    
    Attributes:
        lastIp: Last IP address used (optional).
    """
    lastIp: typing.Optional[str]


@dataclass
class LeidiansConfig:
    """Global configuration for all LDPlayer instances.
    
    This configuration stores global preferences, window management settings,
    update preferences, and multi-instance behavior.
    
    Attributes:
        nextCheckupdateTime: Timestamp for next update check.
        hasPluginLast: Whether plugin was last used.
        strp: String parameter.
        lastZoneArea: Last selected zone area.
        lastZoneName: Last selected zone name.
        vipMode: Whether VIP mode is enabled.
        isBaseboard: Whether baseboard mode is active.
        basicSettings: Basic settings dictionary.
        noiceUserRed: Notice user read flag.
        isFirstInstallApk: Whether this is first APK install.
        cloneFromSmallDisk: Whether to clone from small disk.
        languageId: Language identifier.
        mulTab: Multi-tab mode enabled.
        exitFullscreenEsc: Exit fullscreen with ESC key.
        disableMouseRightOpt: Disable mouse right-click options.
        nextUpdateTime: Timestamp for next update.
        ignoreVersion: Version to ignore for updates.
        framesPerSecond: FPS setting (default: 60).
        reduceAudio: Whether to reduce audio.
        displayMode: Display mode flag.
        vmdkFastMode: VMDK fast mode enabled.
        windowsAlignType: Window alignment type.
        windowsRowCount: Number of window rows.
        windowsAutoSize: Auto-size windows.
        sortwndnotoutscreen: Sort windows to stay on screen.
        moreScreenSortInSame: Sort multi-screen windows together.
        windowsOrigin: Origin position for window grid.
        windowsOffset: Offset between windows.
        batchStartInterval: Interval between batch starts (seconds).
        batchNewCount: Count of batch new instances.
        batchCloneCount: Count of batch clones.
        windowsRecordPos: Record window positions.
        multiPlayerSort: Multi-player sort mode.
        isSSD: Whether using SSD storage.
        fromInstall: Whether from fresh install.
        productLanguageId: Product language ID.
        channelOpenId: Channel open ID.
        channelLastOpenId: Last channel open ID.
        operaRecordFirstDo: First operation record flag.
        remoteEntranceVersion: Remote entrance version.
    """
    nextCheckupdateTime: int = 0
    hasPluginLast: bool = False
    strp: str = ""
    lastZoneArea: str = ""
    lastZoneName: str = ""
    vipMode: bool = False
    isBaseboard: bool = False
    basicSettings: BasicSettings = None
    noiceUserRed: bool = False
    isFirstInstallApk: bool = False
    cloneFromSmallDisk: bool = False
    languageId: str = ""
    mulTab: bool = False
    exitFullscreenEsc: bool = False
    disableMouseRightOpt: bool = False
    nextUpdateTime: int = 0
    ignoreVersion: str = ""
    framesPerSecond: int = 60
    reduceAudio: bool = False
    displayMode: bool = False
    vmdkFastMode: bool = False
    windowsAlignType: int = 0
    windowsRowCount: int = 0
    windowsAutoSize: bool = False
    sortwndnotoutscreen: bool = False
    moreScreenSortInSame: bool = False
    windowsOrigin: WindowsPosition = None
    windowsOffset: WindowsPosition = None
    batchStartInterval: int = 5
    batchNewCount: int = 0
    batchCloneCount: int = 0
    windowsRecordPos: bool = False
    multiPlayerSort: int = 0
    isSSD: bool = False
    fromInstall: bool = False
    productLanguageId: str = ""
    channelOpenId: str = ""
    channelLastOpenId: str = ""
    operaRecordFirstDo: bool = False
    remoteEntranceVersion: int = 0

    @classmethod
    def from_dict(cls, data: dict):
        """Create LeidiansConfig from a dictionary.
        
        Parses dotted keys and filters to only include valid dataclass fields.
        
        Args:
            data: Dictionary loaded from leidians.config file.
            
        Returns:
            LeidiansConfig: Parsed configuration instance.
        """
        data = parse_dotted_dict(data)
        data = {k: v for k, v in data.items() if k in cls.__dataclass_fields__}

        return cls(**data)

    def to_dict(self) -> dict:
        """Convert LeidiansConfig to a dictionary with dotted keys.
        
        Returns:
            dict: Configuration as a flat dictionary with dotted keys.
        """
        data = asdict(self)
        data = flatten_nested_dict(data)
        return data