#!/usr/bin/python

import socket
import time

# Setting up the client socket
UDP_IP="127.0.0.1"
UDP_PORT=5005
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


# Send init
sock.sendto("init", (UDP_IP, UDP_PORT))
time.sleep(1)


for i in range(1,10):

	# Send start
	sock.sendto("start", (UDP_IP, UDP_PORT))
	
	# Perform the encryption operation
	time.sleep(1)

	# Send stop
	sock.sendto("stop", (UDP_IP, UDP_PORT))
	time.sleep(1)

# Send quit
sock.sendto("quit", (UDP_IP, UDP_PORT))


