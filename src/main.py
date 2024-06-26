#!/bin/python3
import sys

import war
import signal
from signal import SIGINT
import time

foxhole: war.Foxhole | None = None


def main():
	global foxhole
	signal.signal(SIGINT, terminate)
	foxhole = war.build()
	foxhole.start()
	while True:
		time.sleep(1)


def terminate(code, frame):
	print('Terminating...')
	global foxhole
	if foxhole is not None:
		foxhole.stop()
	sys.exit(0)


if __name__ == "__main__":
	main()
		
