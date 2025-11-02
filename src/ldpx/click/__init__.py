"""LDPlayer CLI command-line interface.

This module provides the main CLI entry point for the ldpx command-line tool.
It uses Click to create a command-group structure with support for version display,
help options, and output control.

Main command groups:
    - discover: Auto-discover LDPlayer installation
    - console (cmds): All LDPlayer console commands
"""

import click

@click.group(invoke_without_command=True)
@click.version_option()
@click.help_option('-h', '--help')
@click.option("-np","--no-print", is_flag=True, help="Suppress all output messages.")
@click.option(
    '--ldconsole-path',
    type=click.Path(exists=True),
    required=False,
    envvar='LD_CONSOLE_PATH',
    help='Path to ldconsole.exe (auto-detected if not provided)'
)
@click.pass_context
def cli(ctx : click.Context, no_print, ldconsole_path):
    """LDPlayer command-line interface.
    
    Main entry point for the ldpx CLI tool. Provides access to LDPlayer emulator
    control commands and configuration utilities.
    
    Args:
        ctx: Click context object for passing data between commands.
        no_print: Flag to suppress all output messages globally.
        ldconsole_path: Optional path to ldconsole.exe executable.
    """
    if no_print:
        import ldpx.click.utils_echo as click_override
        click_override.global_echo = False

    if not click.get_current_context().invoked_subcommand:
        click.echo(cli.get_help(click.get_current_context()))



    ctx.ensure_object(dict)
    if ldconsole_path:
        ctx.obj['ldconsole_path'] = ldconsole_path


from ldpx.click.discover import discover # noqa E402
cli.add_command(discover)

from ldpx.click.commands import cmds # noqa E402
cli.add_command(cmds)
