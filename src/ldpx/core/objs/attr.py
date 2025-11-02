"""LDPlayer installation attributes and path management.

This module provides the LDAttr class for managing LDPlayer installation
paths and validating the installation structure. Supports auto-discovery
and user configuration-based initialization.
"""
from dataclasses import dataclass
from functools import cached_property
import os
import subprocess
import typing

@dataclass
class LDAttr:
    """Attributes and paths for an LDPlayer installation.
    
    This class represents a validated LDPlayer installation directory
    and provides convenient access to all important paths and executables.
    
    Attributes:
        path: Absolute path to the LDPlayer installation directory.
        validate: Whether to validate the installation on initialization.
        interval_between_batches: Seconds to wait between batch operations.
        
    Raises:
        ValueError: If validate=True and the path is not a valid LDPlayer installation.
    """
    path : str
    validate : bool = True
    interval_between_batches : float = 5.0
    
    def __post_init__(self):
        """Validate the LDPlayer installation after initialization."""
        self.path = os.path.abspath(self.path)
        if self.validate and not self.isValid:
            raise ValueError(f"Invalid LDPlayer path: {self.path}")


    @classmethod
    def from_user(cls, index : int = 0) -> 'LDAttr':
        """Create an LDAttr instance from user configuration.
        
        Loads LDPlayer installation paths from the user's configuration file
        (~/.ldpx/ld/config.json) and creates an LDAttr for the specified index.
        
        Args:
            index: Index of the installation path in the config (default: 0).
            
        Returns:
            LDAttr: Configured LDAttr instance.
            
        Raises:
            ValueError: If no paths are configured or index is out of range.
        """
        from ldpx import LD_CONFIG
        from ldpx.core.objs.attr import LDAttr

        if not LD_CONFIG["path"] or index >= len(LD_CONFIG["path"]):
            raise ValueError("LDPlayer installation directory not found.")
        else:
            path = LD_CONFIG["path"][index]

        return LDAttr(path)

    @classmethod
    def discover(cls, fallback_user_config: bool = True) -> typing.Optional['LDAttr']:
        """Discover LDPlayer installation by scanning running processes.
        
        Attempts to automatically locate LDPlayer by examining running processes.
        If discovery fails and fallback_user_config is True, falls back to user config.
        
        Args:
            fallback_user_config: Whether to fall back to user config if discovery fails.
            
        Returns:
            LDAttr or None: Discovered LDAttr instance, or None if not found.
        """
        from ldpx.core.utils.discover import discover_process
        path = discover_process()
        if not path:
            # If no path is found, fall back to user config
            if fallback_user_config:
                return cls.from_user()
            return None
        return LDAttr(path)

    def __eq__(self, other: "LDAttr"):
        return self.path == other.path

    def __hash__(self):
        return hash(self.path)

    @cached_property
    def dnconsole(self) -> str:
        """Path to dnconsole.exe executable."""
        return os.path.join(self.path, "dnconsole.exe")

    @cached_property
    def ldconsole(self) -> str:
        """Path to ldconsole executable (without .exe extension)."""
        return os.path.join(self.path, "ldconsole")

    @cached_property
    def vmfolder(self) -> str:
        """Path to the virtual machines folder."""
        return os.path.join(self.path, "vms")

    @cached_property
    def customizeConfigs(self) -> str:
        """Path to the custom configurations folder."""
        return os.path.join(self.vmfolder, "customizeConfigs")

    @cached_property
    def recommendedConfigs(self) -> str:
        """Path to the recommended configurations folder."""
        return os.path.join(self.vmfolder, "recommendConfigs")

    @cached_property
    def operationRecords(self) -> str:
        """Path to the operation records folder (macros/scripts)."""
        return os.path.join(self.vmfolder, "operationRecords")

    @cached_property
    def config(self) -> str:
        """Path to the main configuration folder."""
        return os.path.join(self.vmfolder, "config")

    @property
    def isValid(self) -> bool:
        """Check if this is a valid LDPlayer installation.
        
        Validates the installation by checking for required files and folders,
        and verifying that ldconsole can be executed.
        
        Returns:
            bool: True if the installation is valid, False otherwise.
        """
        s = subprocess.run(self.ldconsole, capture_output=True, text=True)
        code = s.returncode

        return all(
            [
                os.path.exists(self.dnconsole),
                os.path.exists(self.vmfolder),
                os.path.exists(self.customizeConfigs),
                os.path.exists(self.recommendedConfigs),
                os.path.exists(self.operationRecords),
                os.path.exists(self.config),
                code == 0,
            ]
        )
