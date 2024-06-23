#!/bin/python3
from PyInstaller.__main__ import run
import subprocess
import platform

PROG_NAME = 'foxhole-auto'
ENTRY_POINT = 'src/main.py'
ZIP_NAME = f'{PROG_NAME}.zip'
TAR_GZ_NAME = f'{PROG_NAME}.tar.gz'
ZIP_LINUX_CMD = ['zip', '-r', '-j', ZIP_NAME, f'dist/{PROG_NAME}']
TAR_GZ_CMD = ['tar', '-czf', TAR_GZ_NAME, '-C', 'dist', f'{PROG_NAME}']

def compress_to_zip():
    try:
        print('Compressing to zip... ', end='')
        subprocess.run(ZIP_LINUX_CMD, check=True)
        print('Good.')
    except subprocess.CalledProcessError:
        print('FAILED.')

def compress_to_tar_gz():
    try:
        print('Compressing to tar.gz... ', end='')
        subprocess.run(TAR_GZ_CMD, check=True)
        print('Good.')
    except subprocess.CalledProcessError:
        print('FAILED.')

if __name__ == '__main__':
    # Production Build
    opts = ['-F', f'--name={PROG_NAME}', ENTRY_POINT]
    run(opts)
    # Build Artifacts
    if platform.system() == 'Linux':
        # Compress to zip
        compress_to_zip()
        # Compress to tar.gz
        compress_to_tar_gz()
    else:
        print('Skipping compression phase (Linux Only).')