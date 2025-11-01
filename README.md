# LDX - LDPlayer Automation Toolkit

A powerful Python abstraction layer and CLI tool for controlling LDPlayer Android emulator instances. Manage multiple emulators programmatically with comprehensive batch operation support.

[![Python Version](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

## Features

- 🐍 **Python API**: Complete wrapper for all ldconsole commands
- 🚀 **Batch Operations**: Execute commands across multiple instances simultaneously
- 🔍 **Auto-Discovery**: Automatically detect LDPlayer installations
- ⚙️ **Configuration Management**: Read and modify emulator configs programmatically
- 🎯 **Flexible Targeting**: Select instances by name, index, list, or lambda filter
- 💾 **Smart Caching**: LFU cache for configuration files with automatic staleness detection
- 📝 **Type-Safe**: Full type hints and comprehensive docstrings
- 🛠️ **CLI Tool**: Intuitive command-line interface built with Click

## Installation

### Using uv (recommended)
```bash
# With CLI support
uv add ldx[click]

# API only
uv add ldx
```

### Using pip
```bash
# With CLI support
pip install ldx[click]

# API only
pip install ldx
```

## Quick Start

### Auto-Discovery
```bash
# Discover LDPlayer installation automatically
ldx discover

# Verify configuration
ldx console query list2
```

### Python API

```python
from ldx.core.objs.attr import LDAttr
from ldx.core.objs.console import Console

# Initialize (auto-discover or load from config)
attr = LDAttr.discover()
console = Console(attr)

# Single instance operations
console.launch(name="instance1")
console.installapp(index=0, filename="app.apk")

# Batch operations - by list
console.launch([0, 1, 2])

# Batch operations - by lambda filter
console.launch(instances=lambda x: x.name.startswith('game'))

# Query instances
instances = console.list2()
for inst in instances:
    print(f"{inst['name']}: {inst['id']}")
```

### CLI Usage

```bash
# Launch single instance
ldx console exec launch --name instance1

# Batch launch by indices
ldx console exec launch -bs "0,1,2"

# Batch launch by lambda filter
ldx console exec launch -bl "lambda x: x['name'].startswith('game')"

# Install app on multiple instances
ldx console app installapp --filename app.apk -bs "0,1,2"

# Query instance information
ldx console query list2
ldx console query isrunning --name instance1

# Modify instance settings
ldx console config modify --name instance1 --resolution "1920x1080" --cpu 4 --memory 4096
```

## Command Categories

### Query Commands
Get information about emulator instances:
- `list` - List all instances (simple format)
- `list2` - List all instances (detailed metadata)
- `list3` - Query single instance details
- `runninglist` - List running instances
- `isrunning` - Check if instance is running
- `getprop` - Get system property value
- `operatelist` - List operations for instance
- `operateinfo` - Get operation information

### Execution Commands
Control emulator lifecycle:
- `launch` - Start an emulator instance
- `quit` - Stop an emulator instance
- `reboot` - Reboot an emulator instance
- `quitall` - Stop all running instances
- `add` - Create new emulator instance
- `copy` - Clone an existing instance
- `remove` - Delete an emulator instance
- `rename` - Rename an emulator instance

### App Management
Manage Android applications:
- `installapp` - Install APK file or app by package name
- `uninstallapp` - Uninstall app by package name
- `runapp` - Launch an app
- `killapp` - Stop a running app
- `launchex` - Launch app with extended options
- `backupapp` - Backup app and its data
- `restoreapp` - Restore app and its data

### Configuration
Modify emulator settings:
- `modify` - Change instance settings (CPU, memory, resolution, device info, etc.)
- `globalsetting` - Configure global settings (FPS, audio, etc.)
- `operaterecord` - Execute recorded macro/script

### File Operations
Transfer files between host and emulator:
- `pull` - Download files from emulator
- `push` - Upload files to emulator

### Simple Commands
Utility commands:
- `rock` - Shake the emulator window
- `zoomIn` - Zoom in the emulator window
- `zoomOut` - Zoom out the emulator window
- `sortWnd` - Sort and arrange emulator windows

## Batch Operations

Batch operations allow you to execute commands on multiple instances at once.

### By Comma-Separated List
```bash
# Indices
ldx console exec launch -bs "0,1,2"

# Names
ldx console exec launch -bs "instance1,instance2,instance3"
```

### By Lambda Filter
```bash
# Filter by name pattern
ldx console exec launch -bl "lambda x: x['name'].startswith('game')"

# Filter by running status
ldx console exec quit -bl "lambda x: x['android_started_int'] == 1"
```

### Python API Batch
```python
# List of indices
console.launch([0, 1, 2])

# List of names
console.launch(["instance1", "instance2"])

# Lambda filter
console.launch(instances=lambda x: x['name'].startswith('test'))

# Custom function
console.launch(console_func=lambda c: c.launch(name='specific'))
```

## Configuration Management

```python
from ldx.ext.obj.leidian import LeidianFile

# Initialize
leidian_file = LeidianFile(attr)

# Get global configuration
global_config = leidian_file.getLeidiansConfig()

# Get instance configuration
instance_config = leidian_file.getLeidianConfig(0)

# Modify and save
instance_config.basicSettings['fps'] = 120
leidian_file.dumpLeidianConfig(instance_config)
```

## Advanced Features

### Keyboard Mapping Management
```python
from ldx.ext.obj.kmp import KMPFile

kmp_file = KMPFile(attr)

# List available mappings
mappings = kmp_file.customizeList()

# Load a mapping
mapping = kmp_file.getCustomize("game_mapping.kmp")

# Modify and save
# ... modify mapping ...
kmp_file.dump("game_mapping.kmp", mapping)
```

### Macro/Script Management
```python
from ldx.ext.obj.record import RecordFile

record_file = RecordFile(attr)

# List recordings
recordings = record_file.recordList()

# Load a recording
record = record_file.getRecord("automation.record")

# Execute on instance
console.operaterecord(name="instance1", content=record)
```

## Requirements

- Python 3.12 or higher
- Windows OS (LDPlayer is Windows-only)
- LDPlayer installed
- psutil for process discovery
- click for CLI (optional)

## Configuration

LDX stores configuration in `~/.ldx/ld/config.json`:

```json
{
    "path": [
        "C:/path/to/LDPlayer",
        "D:/another/installation"
    ]
}
```

Add paths manually or use `ldx discover` for automatic detection.

## Documentation

Full API documentation with docstrings is available in the source code. Each module, class, and function includes comprehensive documentation.

## Contributing

Contributions welcome! Please ensure:
- Code follows existing patterns
- Type hints are included
- Docstrings are comprehensive
- Tests pass (when test suite is added)

## License

MIT License - see LICENSE file for details

## Acknowledgments

- LDPlayer for providing the ldconsole CLI tool
- Click framework for CLI capabilities
- psutil for process management

## Support

For issues, questions, or contributions, please visit the project repository.

---

**Note**: This tool requires LDPlayer to be installed and is Windows-only due to LDPlayer platform constraints.
