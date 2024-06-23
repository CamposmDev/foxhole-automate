#!/bin/python3
import war
import sys
import signal
from signal import SIGINT

foxhole: war.Foxhole | None = None

def main():
	global foxhole
	signal.signal(SIGINT, terminate)
	foxhole = war.build()
	foxhole.start()

def terminate(code, frame):
	global foxhole
	if foxhole is not None:
		foxhole.stop()
	sys.exit(0)


if __name__ == "__main__":
	main()
		
