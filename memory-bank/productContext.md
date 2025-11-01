# Product Context: LDX

## Why This Project Exists

### Problem Statement
LDPlayer is a popular Android emulator for Windows, but controlling multiple instances programmatically is challenging:
- ldconsole CLI is command-line only with no Python bindings
- No built-in support for batch operations across instances
- Configuration files are complex JSON structures without schemas
- Manual path configuration required for each installation

### Solution
LDX bridges the gap by providing:
- Pythonic API wrapping ldconsole functionality
- Powerful batch execution with filtering (by index, name, or lambda)
- Type-safe configuration models with docstrings
- Auto-discovery of LDPlayer installations
- CLI tool with intuitive command structure

## How It Should Work

### For Python Developers
```python
from ldx.core.objs.attr import LDAttr
from ldx.core.objs.console import Console

# Auto-discover or load from config
attr = LDAttr.discover()
console = Console(attr)

# Single instance operations
console.launch(name="instance1")
console.installapp(index=0, filename="app.apk")

# Batch operations
console.launch([0, 1, 2])  # Launch by indices
console.launch(instances=lambda x: x.name.startswith('test'))  # Lambda filter
```

### For CLI Users
```bash
# Auto-discover installation
ldx discover

# Single instance commands
ldx console launch --name instance1
ldx console query list2

# Batch operations
ldx console exec launch -bs "0,1,2"  # Comma-separated
ldx console exec launch -bl "lambda x: x['name'].startswith('game')"  # Lambda

# App management
ldx console app installapp --name instance1 --filename app.apk -bs "0,1,2"
```

## User Experience Goals

### Developer Experience
- **Intuitive API**: Methods mirror ldconsole commands with clear names
- **Type Safety**: Full type hints and TypedDict models
- **Comprehensive Docs**: Every class/function has detailed docstrings
- **Flexible Targeting**: Target instances by name, index, list, or filter

### CLI Experience
- **Logical Grouping**: Commands organized by category (query, exec, app, config)
- **Batch-First Design**: All applicable commands support batch operations
- **Clear Output**: Informative messages and error handling
- **Consistency**: Unified parameter patterns across commands

### Configuration Management
- **Read Access**: Parse all LDPlayer config files (instance, global, mappings)
- **Type Safety**: Dataclass models with field documentation
- **Caching**: LFU cache for performance on repeated access
- **Modification**: Load, modify, and save configurations programmatically
