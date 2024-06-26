#!/bin/python3
import warnings
warnings.warn("Use Makefile. This file will be removed in the future.")
from PyInstaller.__main__ import run
import subprocess
import platform

WIN = 'Windows'
LINUX = 'Linux'
PROG_NAME = 'foxhole-auto'
BUILD_VERSION = '1.0.0'
ENTRY_POINT = 'src/main.py'
BUILD_OPTS = ['--onedir', f'--name={PROG_NAME}', ENTRY_POINT]

def compress_to_zip():
    ZIP_NAME = f'{PROG_NAME}_{BUILD_VERSION}_{platform.system().lower()}.zip'
    try:
        print('Compressing to zip... ', end='')
        if platform.system() == WIN:
            ZIP_WIN_CMD = ['powershell.exe', 'Compress-Archive', f'dist/{PROG_NAME}', ZIP_NAME, '-Force']
            subprocess.run(ZIP_WIN_CMD, check=True)
        else:
            ZIP_LINUX_CMD = ['zip', '-r', '-j', ZIP_NAME, f'dist/{PROG_NAME}']
            subprocess.run(ZIP_LINUX_CMD, check=True)
        print('Good.')
    except subprocess.CalledProcessError:
        print('FAILED.')

def compress_to_tar_gz():
    TAR_GZ_NAME = f'{PROG_NAME}_{BUILD_VERSION}_{LINUX.lower()}.tar.gz'
    try:
        print('Compressing to tar.gz... ', end='')
        TAR_GZ_CMD = ['tar', '-czf', TAR_GZ_NAME, '-C', 'dist', f'{PROG_NAME}']
        subprocess.run(TAR_GZ_CMD, check=True)
        print('Good.')
    except subprocess.CalledProcessError:
        print('FAILED.')

if __name__ == '__main__':
    # Production Build
    run(BUILD_OPTS)
    # Build Artifacts
    if platform.system() == WIN:
        compress_to_zip()
    else:
        compress_to_tar_gz()
