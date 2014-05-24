import click

from githubflow import __version__


def print_version(ctx, value):
    if not value:
        return
    click.echo('Version '+__version__)
    ctx.exit()


@click.command()
@click.option('--version', is_flag=True, callback=print_version,expose_value=False, is_eager=True)
def cli():
    """Example script."""
    click.echo('Hello World!')
    

