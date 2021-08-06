#!/usr/bin/env python

import socket, sys, time


print('''
    ______	                                ____                  ______
   / ____/_  __________  ___  _____            / __ \_   _____  _____/ __/ /___ _      __
  / /_  / / / /_  /_  / / _ \/ ___/  ______   / / / / | / / _ \/ ___/ /_/ / __ \ | /| / /
 / __/ / /_/ / / /_/ /_/  __/ /     /_____/  / /_/ /| |/ /  __/ /  / __/ / /_/ / |/ |/ / 
/_/    \__,_/ /___/___/\___/_/               \____/ |___/\___/_/  /_/ /_/\____/|__/|__/  
                                                                                       
                                  [*] Starting...	                                                                                         
''')
	


try:
	a = sys.argv[1]
	b = sys.argv[2]

except:
	print("[!] Usage: python fuzzer.py <target> <port>")
	sys.exit()	

ip = str(a)
port = int(b)
	
prefix = b""
buffer = b"A" * 100
postfix = b""
timeout = 5

req = prefix + buffer + postfix

print("[*] Connecting to " + ip + ":" + str(port))

while True:
	try:
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		s.connect((ip,port))
		s.settimeout(timeout)
		s.recv(1024)
		print("[*] Fuzzing with " + str(len(buffer)) +" bytes")
		s.send(req + b'\r\n')
		s.recv(1024)
		
	except:
		print("[-] Fuzzing stopped at " + str(len(buffer)) + " bytes")
		sys.exit()
	
	buffer += b"A" * 100
	time.sleep(1)
	
