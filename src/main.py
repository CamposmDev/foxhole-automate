#!/bin/python3
import sys
import war
import signal
import time
from signal import SIGINT

foxhole: war.Foxhole | None = None

def main():
	global foxhole
	# add signal handler for SIGINT
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
		
