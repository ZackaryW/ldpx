"""Command modules for LDPlayer CLI."""

from ldx.click.commands.simple import simple_group
from ldx.click.commands.query import query_group
from ldx.click.commands.exec import exec_group
from ldx.click.commands.app import app_group
from ldx.click.commands.config import config_group
import click
import logging
import sys
from pathlib import Path

from ldx.core.objs.attr import LDAttr
from ldx.core.objs.console import Console




@click.group(
    name="console", invoke_without_command=False, help="LDPlayer console commands"
)
@click.option(
    "--ldconsole-index",
    type=int,
    help="Specify LDPlayer instance index for commands that require it.",
    default=0
)
@click.pass_context
def cmds(ctx, ldconsole_index):
    """
    LDPlayer Console CLI wrapper.

    Provides command-line access to LDPlayer emulator control functions.
    Supports single and batch operations on emulator instances.
    """

    # Ensure context object exists
    ctx.ensure_object(dict)
    ldconsole_path = ctx.obj.get("ldconsole_path", None)
    # Discover or use provided ldconsole path
    try:
        if ldconsole_path:
            ldconsole_path = Path(ldconsole_path)
            if not ldconsole_path.exists():
                click.echo(f"Error: ldconsole not found at: {ldconsole_path}", err=True)
                sys.exit(1)

            attr = LDAttr(ldconsole_path)
        else:
            attr = LDAttr.from_user(index=ldconsole_index)
    except Exception as e:
        click.echo(f"Error initializing LDAttr: {e}", err=True)
        sys.exit(1)
    ctx.obj["console"] = Console(attr)
    logging.debug(f"Console initialized with: {attr.path}")


for group in [simple_group, query_group, exec_group, app_group, config_group]:
    for cmd in group.commands.values():
        cmds.add_command(cmd)
