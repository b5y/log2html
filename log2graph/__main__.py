# -*- coding: utf-8 -*-
import sys
import os.path

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import logging
import click
import plotly.tools as tls

from log2graph.log2html import draw_graph

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


@click.group(context_settings=dict(help_option_names=["-h", "--help"]))
def cli():
    pass


@cli.command()
@click.argument('log_file_s',
                required=True,
                nargs=1,
                type=click.Path(exists=True, resolve_path=True),
                metavar="<path or file>")
@click.argument('auto_open', required=False, nargs=1)
@click.argument('plotly_login', required=False, nargs=1)
@click.argument('api_key', required=False, nargs=1)
def run(log_file_s=basestring, auto_open=None, plotly_login=None, api_key=None):
    if not tls.get_credentials_file():
        print 'Please set your plotly login and api_key or give as additional arguments'
    if plotly_login and api_key:
        tls.set_credentials_file(plotly_login, api_key)
        logger.info('\nCredentials file is updated')
    draw_graph(log_file_s, auto_open=auto_open)
    logger.info('\nGraphs was drawn successfully\n')


def main():
    cli()


if __name__ == '__main__':
    main()
