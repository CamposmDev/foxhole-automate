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
	while foxhole.alive:
		time.sleep(1)
	print('Bye Bye')


def terminate(code, frame):
	global foxhole
	if foxhole is not None:
		foxhole.stop()


if __name__ == "__main__":
	main()
		
