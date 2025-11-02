# Tech Context: LDPX

## Technologies

### Core Dependencies
- **Python 3.12+**: Modern Python with latest type hints
- **psutil 7.1.2+**: Process discovery and management
- **click 8.3.0+**: CLI framework (optional extra)

### Build System
- **uv_build**: Modern Python build backend
- Package manager: uv (fast pip alternative)

## Development Setup

### Installation
```bash
# Clone repository
git clone <repo-url>
cd ldpx

# Install with CLI support
uv sync --all-extras

# Or basic install
uv sync
```

### Project Structure
```
ldpx/
├── pyproject.toml          # Project metadata and dependencies
├── src/ldpx/                # Source code
├── memory-bank/            # Project documentation
└── README.md               # Public documentation
```

### Environment
- Python version specified in `.python-version`: 3.12
- Dependencies managed via pyproject.toml
- Entry point: `ldpx` command (maps to `ldpx.click:cli`)

## Technical Constraints

### Platform Support
- **Windows Only**: LDPlayer is Windows-exclusive
- Process creation uses Windows-specific flags:
  - `DETACHED_PROCESS`
  - `CREATE_NEW_PROCESS_GROUP`
  - `CREATE_BREAKAWAY_FROM_JOB`

### LDPlayer Requirements
- ldconsole must be executable
- Expected directory structure:
  - `dnconsole.exe`
  - `vms/` (virtual machines folder)
  - `vms/config/` (configuration files)
  - `vms/customizeConfigs/` (custom keyboard mappings)
  - `vms/recommendedConfigs/` (recommended mappings)
  - `vms/operationRecords/` (macro recordings)

### Encoding
- Default subprocess encoding: `gbk` (Chinese Windows)
- JSON files: UTF-8 with BOM support
- Config files use UTF-8

## Dependencies Detail

### psutil
- Used for: Process iteration and discovery
- Key functions:
  - `process_iter()`: Enumerate running processes
  - `proc.name()`: Get process name
  - `proc.exe()`: Get executable path

### click (Optional)
- Used for: CLI implementation only
- Imported conditionally in `ldpx.click` module
- Not required for Python API usage
- Features used:
  - Command groups
  - Options with validation
  - Context passing
  - Help generation

## Tool Usage Patterns

### Configuration Management
```python
# User config location
~/.ldpx/ld/config.json

# Structure
{
    "path": [
        "C:/path/to/LDPlayer",
        "D:/another/installation"
    ]
}
```

### Logging
- Standard Python logging module
- Debug level for subprocess commands
- Info level for batch operations
- Error level for failures

### Type Checking
- Full type hints throughout codebase
- TypedDict for configuration structures
- Generic types for batch operations
- Union types for flexible parameters

### Caching Strategy
- LFU (Least Frequently Used) eviction
- Metadata: mtime (modification time), ac (access count)
- Cache size: 1000 files default
- Automatic staleness detection via mtime comparison
