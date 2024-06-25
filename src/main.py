#!/bin/python3
import war
import signal
from signal import SIGINT
import sys

foxhole: war.Foxhole | None = None

def main():
	global foxhole
	signal.signal(SIGINT, terminate)
	foxhole = war.build()
	foxhole.start()

def terminate(code, frame):
	print('Stopping program...')
	global foxhole
	if foxhole is not None:
		foxhole.stop()

if __name__ == "__main__":
	main()
		
