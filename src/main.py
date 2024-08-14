#!/bin/python3
import war

foxhole: war.Foxhole | None = None

def main():
	global foxhole
	foxhole = war.build()
	foxhole.start()

if __name__ == "__main__":
	main()
		
