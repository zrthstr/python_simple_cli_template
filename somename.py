#!/usr/bin/env python3

import argparse
import logging

def logger():
    log = logging.getLogger()
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(name)-12s %(levelname)-8s %(message)s')
    handler.setFormatter(formatter)
    log.addHandler(handler)
    return log


def parse_commandline():
    parser = argparse.ArgumentParser()
    parser.add_argument('--verbose', '-v', action='count')
    parser.add_argument('--version', '-V')
    parser.add_argument('action', choices=['auth', 'list', 'post', 'clear'])
    return parser


if __name__ == "__main__":
    args = parse_commandline()
    log = logger()
    print(args) 
    log.error(args)