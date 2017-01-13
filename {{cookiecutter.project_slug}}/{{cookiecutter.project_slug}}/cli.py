# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function, unicode_literals)
import click


@click.command()
def main(args=None):
    """Console script for {{cookiecutter.project_slug}}"""
    click.echo("Replace this message by putting your code into "
               "{{cookiecutter.project_slug}}.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")


if __name__ == "__main__":
    main()
