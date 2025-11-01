"""Output utilities for Click CLI.

This module provides a wrapper around Click's echo function with global
output control capabilities. When global_echo is set to False, all output
is suppressed across the application.
"""
from typing import IO, Any
import click

# Global flag to control all echo output
global_echo = True

def echo(
    message: Any | None = None,
    file: IO[Any] | None = None,
    nl: bool = True,
    err: bool = False,
    color: bool | None = None
):
    """A simple wrapper around click.echo to standardize output handling.
    
    Args:
        message: The message to output (any type that can be converted to string).
        file: The file object to write to (defaults to stdout).
        nl: Whether to add a newline at the end.
        err: Whether to write to stderr instead of stdout.
        color: Whether to enable color output (None = auto-detect).
        
    Note:
        Respects the global_echo flag. When False, no output is produced.
    """
    if not global_echo:
        return

    click.echo(message, file=file, nl=nl, err=err, color=color)