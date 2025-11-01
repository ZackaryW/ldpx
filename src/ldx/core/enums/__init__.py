"""Command categories and enumerations for LDPlayer console operations.

This module defines all available LDPlayer console commands organized by type:
- Simple execution: Commands with no parameters
- Varied execution: Commands with parameters
- Simple queries: Query commands with no parameters
- Varied queries: Query commands with parameters
- Batchable commands: Commands that support batch execution
- Other commands: Special commands with custom handling
"""

# Simple execution commands (no parameters)
SIMPLE_EXEC_LIST = ["rock", "zoomOut", "zoomIn", "sortWnd", "quitall"]


# Varied execution commands (with parameters)
VARIED_EXEC_LIST = [
    "quit",
    "launch",
    "reboot",
    "copy",
    "add",
    "remove",
    "rename",
    "installapp",
    "uninstallapp",
    "runapp",
    "killapp",
    "locate",
    "adb",
    "setprop",
    "downcpu",
    "backup",
    "restore",
    "action",
    "scan",
    "pull",
    "push",
    "backupapp",
    "restoreapp",
    "launchex",
]


# Simple query commands (no parameters, return information)
SIMPLE_QUERY_LIST = ["list", "runninglist"]

# Varied query commands (with parameters, return information)
VARIED_QUERY_LIST = ["isrunning", "getprop", "operatelist", "operateinfo", "list3"]

# Commands that support batch execution (multiple instances at once)
BATCHABLE_COMMANDS = [
    "modify",
    "quit",
    "launch",
    "reboot",
    "installapp",
    "uninstallapp",
    "runapp",
    "killapp",
    "pull",
    "push",
    "backupapp",
    "restoreapp",
    "launchex",
    "operaterecord",
]

# Special commands with custom handling logic
OTHER_COMMANDS = ["list2", "modify", "globalsetting", "operaterecord"]

# Complete list of all available commands
FULL_COMMANDS_LIST = (
    SIMPLE_EXEC_LIST
    + VARIED_EXEC_LIST
    + SIMPLE_QUERY_LIST
    + VARIED_QUERY_LIST
    + OTHER_COMMANDS
)