# System Patterns: LDX

## Architecture Overview

```
ldx/
├── core/           # Core functionality (command execution, batch ops)
│   ├── enums/      # Command categorization
│   ├── interfaces/ # IConsole interface definition
│   ├── models/     # Data models (List2Meta, Record)
│   ├── objs/       # Console, LDAttr implementations
│   └── utils/      # Utilities (batch, subprocess, discovery, json)
├── click/          # CLI implementation
│   ├── commands/   # Command groups (app, exec, query, config, simple)
│   └── discover.py # Auto-discovery command
└── ext/            # Extended functionality (config management)
    ├── cache.py    # LFU file caching
    ├── models/     # Config file models (leidian_config, kmp, smp)
    ├── obj/        # Config file managers
    └── utils/      # Dictionary utilities
```

## Key Technical Decisions

### 1. Interface-Based Design
- `IConsole` interface defines all ldconsole operations
- `Console` implements interface with dynamic method generation
- Commands categorized by type (simple/varied, exec/query, batchable)

### 2. Batch Processing via Mixin
- `BatchMixin` adds batch capabilities to Console
- `__getattribute__` intercepts batchable commands
- Supports list targets, lambda filters, custom functions

### 3. Dynamic Command Generation
- Methods generated from interface signatures
- Factory functions create Click commands programmatically
- Reduces boilerplate and ensures consistency

### 4. Configuration Caching
- `AttrMixin` provides LFU cache via metaclass
- Tracks file mtime to detect changes
- Automatic eviction when cache limit reached

### 5. Type Safety Throughout
- TypedDict for config structures
- Dataclasses for complex models
- Full type hints in all modules

## Design Patterns

### Factory Pattern
`command_factory.py` creates Click commands dynamically:
- `create_simple_command`: No-parameter commands
- `create_query_command`: Query commands with optional targeting
- `create_batchable_command`: Commands supporting batch operations
- `create_exec_command`: Standard execution commands

### Mixin Pattern
- `BatchMixin`: Adds batch execution to Console
- `AttrMixin`: Adds file caching to config managers

### Strategy Pattern
Batch execution supports multiple targeting strategies:
- List of indices/names
- Lambda filter function
- Custom console function

## Component Relationships

### Console Execution Flow
```
CLI Command → Click Handler → Console Method → 
    ↓
Batch Check (if batchable) →
    ↓
batch_execute() → Multiple ldconsole calls
    OR
Single ldconsole call
```

### Configuration Access Flow
```
Config Manager (LeidianFile/KMPFile/etc) →
    ↓
AttrMixin._loadFile() →
    ↓
Cache Check (mtime) →
    ↓
Return cached OR Load from disk + cache
```

## Critical Implementation Paths

### Auto-Discovery
1. `discover_process()` scans running processes
2. Finds dnplayer.exe or dn-prefixed processes
3. Traverses directory tree to find LDPlayer root
4. Validates installation with ldconsole execution test

### Batch Execution
1. Command called with list or filter
2. `_is_batch_call()` detects batch mode
3. `_execute_batch()` prepares arguments
4. `batch_execute()` iterates targets
5. Respects `interval_between_batches` setting

### Command Parsing
1. CLI receives command with options
2. Factory-generated handler validates parameters
3. Parameters mapped to Console method arguments
4. Mutual exclusivity validated (name vs index, batch vs single)
5. Method invoked with proper targeting
