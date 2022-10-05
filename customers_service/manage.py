#! /usr/bin/env python

import os
import json
import signal
import subprocess

import click


docker_compose_file = "docker/development.yml"
docker_compose_cmdline = ["docker-compose", "-f", docker_compose_file]


def setenv(variable, default):
    os.environ[variable] = os.getenv(variable, default)


# Default value for APPLICATION_CONFIG
setenv("APPLICATION_CONFIG", "development")


# Read configuration from JSON file
config_json_filename = os.getenv("APPLICATION_CONFIG") + ".json"
with open(os.path.join("config", config_json_filename)) as f:
    config = json.load(f)


# Set environment variables from JSON config
config = {setting['name']: setting['value'] for setting in config}
for key, value in config.items():
    setenv(key, value)


# Click CLI
@click.group()
def cli():
    pass


# Wrapper for Flask commands
@cli.command(context_settings={"ignore_unknown_options": True})
@click.argument("subcommand", nargs=-1, type=click.Path())
def flask(subcommand):
    cmdline = ["flask"] + list(subcommand)

    try:
        p = subprocess.Popen(cmdline)
        p.wait()
    except KeyboardInterrupt:
        p.send_signal(signal.SIGINT)
        p.wait()


# Wrapper for Docker Compose commands
@cli.command(context_settings={"ignore_unknown_options": True})
@click.argument("subcommand", nargs=-1, type=click.Path())
def compose(subcommand):
    cmdline = docker_compose_cmdline + list(subcommand)

    try:
        p = subprocess.Popen(cmdline)
        p.wait()
    except KeyboardInterrupt:
        p.send_signal(signal.SIGINT)
        p.wait()


# Add Click commands
cli.add_command(flask)
cli.add_command(compose)


if __name__ == "__main__":
    cli()
