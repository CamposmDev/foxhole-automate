#!/bin/python3
from PyInstaller.__main__ import run

PROG_NAME = 'foxhole-auto'
SOURCE = 'src/main.py'

if __name__ == '__main__':
    opts = ['-F', f'--name={PROG_NAME}', SOURCE]
    run(opts)