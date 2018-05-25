#!/usr/bin/python

import socket
import time
import datetime
import subprocess


# writing the log entries to a log file
def logEntry(msg):
	st = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
	LOG = st + " " + msg + "\n"
	logfile.write(LOG)
	print(LOG)

# Log file (file buffer size is set to 0 to write immediately)
logfile = open("logfile.txt", "w", 0)

# Setting up the server socket
UDP_IP="127.0.0.1"
UDP_PORT=5005
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while True:
	msg, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
	#if msg=="init":
	#	startHackRF()
	#elif msg=="start":
	#	print("Log entry: Starting an encryption")
	#elif msg=="stop":
	#	print("Log entry: Stopping the encryption")
	#elif msg=="quit":
	#	print("Log entry: Stopping EM capturing")
	#else:
	#	print("Didn't recognize the message")

	# Putting a log entry
	logEntry(msg)


