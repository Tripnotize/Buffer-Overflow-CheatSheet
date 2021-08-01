#!/usr/bin/env python
# Fuzzer for testing Overflows

import socket, sys, time

ip = '192.168.0.0'
port = 9999

prefix = b""
buffer = b"A" * 100
timeout = 5
postfix = b""

while True:
	try:
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		s.connect((ip,port))
		s.settimeout(timeout)
		s.recv(1024)
		print("[*] Fuzzing with " + str(len(buffer)) +" bytes")
		s.send(buffer + b'\r\n')
		s.recv(1024)
		
	except:
		print("[-] Fuzzing stopped at " + str(len(buffer)) + " bytes")
		sys.exit()
	
	buffer += b"A" * 100
	time.sleep(1)
	
