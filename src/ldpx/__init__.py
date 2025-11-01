"""LDPlayer CLI wrapper and automation toolkit.

This package provides Python bindings and CLI tools for interacting with
LDPlayer Android emulator instances. It supports batch operations, emulator
management, app installation/control, and configuration modifications.

Configuration:
    User configuration is stored in ~/.ldpx/
    LDPlayer paths are managed in ~/.ldpx/ld/config.json
"""

import pathlib

from ldpx.core.utils.json import touch_json

# User configuration directory
# User configuration directory
CONFIG_DIR = pathlib.Path.home() / ".ldpx"

CONFIG_DIR.mkdir(parents=True, exist_ok=True)

# LDPlayer-specific configuration directory
# LDPlayer-specific configuration directory
LD_CONFIG_DIR = CONFIG_DIR / "ld" 

LD_CONFIG_DIR.mkdir(parents=True, exist_ok=True)

# LDPlayer configuration file path
LD_CONFIG_FILE = LD_CONFIG_DIR / "config.json"

# Load or create LDPlayer configuration with default structure
LD_CONFIG = touch_json(LD_CONFIG_FILE, default_data={"path" : []})