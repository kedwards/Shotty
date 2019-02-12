# Shotty
Python script to manage AWS EC2 instance snapshots.

## About

This script uses boto3 to manage AWS EC2 instance snapshots.

## Configuring

shotty uses the configuration file created by the AWS cli. e.g.

`aws configure --profile shotty`

## Running

`pipenv run python shotty/shotty.py <commmand> <subcommand> <--project=PROJECT>`

*command* can be one of 
- instances
- volumes
- or snapshots

*subcommand*
- depends on command

*Project* is optional
