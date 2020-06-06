#!/usr/bin/env python
import click


@click.group()
@click.version_option()
def cli():
    pass


@cli.command()
@click.argument('input', default='Hello, world!')
def echo(input):
    click.echo(input)


@cli.group()
def math():
    pass


@math.command()
@click.argument('a', type=int, default=3)
@click.argument('b', type=int, default=4)
def add(a, b):
    click.echo(f'{a} + {b} = {a+b}')


@math.command()
@click.argument('a', type=int)
def factorial(a):
    from math import factorial as calculate_factorial
    click.echo(f'{a}! = {calculate_factorial(a)}')


if __name__ == '__main__':
    cli()
