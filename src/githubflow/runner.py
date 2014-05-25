import click
import sys

from githubflow import __version__, authenticate, github

def print_version(ctx, value):
    if not value:
        return
    click.echo('Version '+__version__)
    ctx.exit()


class ghf(object):
    def __init__(self, ini_file, debug, token, username, password, profile, fields, print_header_row, export_csv, csv_separator):
        self.debug = debug
        self.token = token
        self.profile = profile
        self.fields=fields
        self.print_header_row=print_header_row
        self.export_csv=export_csv
        self.csv_separator=csv_separator
        if token == None:
            token = authenticate.getToken(ini_file,debug)
            self.token = token
            if token == None:
                if username == None:
                    click.echo("Username is required to create your access token")
                    sys.exit()
                if password == None:
                    password = click.prompt('password', hide_input=True, confirmation_prompt=True)
                    if debug: click.echo(password)
                token = authenticate.createToken(username,password)
                if token == None:
                    click.echo('Problem getting your github authentication token')
                    sys.exit(1)
                authenticate.saveToken(ini_file,token)
                self.token = token
        


@click.group()
@click.option('--ini-file', envvar='GHF_INI_FILE', default='~/.ghf.ini', help='which config file to read/write authentication token')
@click.option('--debug/--no-debug', default=False, envvar='GHF_DEBUG', help='turn on/off debug mode')
@click.option('--version', is_flag=True, callback=print_version,expose_value=False, is_eager=True, help='print programs version')
@click.option('--username', '-u', envvar="GHF_USERNAME", default=None, help='github username used to create authentication token')
@click.option('--password', '-p', envvar="GHF_PASSWORD", default=None, help='github password used to create authentication token')
@click.option('--token', '-t', envvar="GHF_TOKEN", default=None, help='explicitly pass in your authentication token')
@click.option('--profile', is_flag=True, default=False, envvar="GHF_PROFILE", help='print out the fields from the return github json object')
@click.option('--fields', '-f', multiple=True, default=(), help='select these fields in your output')
@click.option('--header/--no-header', is_flag=True, default=True, envvar="GHF_HEADER", help='print or don\'t print the header row')
@click.option('--csv', is_flag=True, default=False, envvar="GHF_CSV", help='output data as csv')
@click.option('--csv-separator', default=',', envvar="GHF_CSV_SEPARATOR", help='set the csv separator')
@click.pass_context
def cli(ctx, ini_file, debug, token, username, password, profile, fields, header, csv, csv_separator):
    ctx.obj = ghf(ini_file, debug, token, username, password, profile, fields, header, csv, csv_separator)

# click.prompt('password', hide_input=True, confirmation_prompt=True)
    
@cli.command()
@click.argument('org')
@click.pass_obj
def repos(ghf, org):
    """List all the repos"""
    # click.echo('list repos:'+str(ghf.token))
    gh = github.github(ghf)
    gh.repos(org)
    
if __name__ == '__main__':
    cli()
    

