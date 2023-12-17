#!/usr/bin/python
import socket,sys

argv = str(input("Type your target: "))

if len(argv) <= 1:
        print ("Use mode: ./portscan.py 10.10.0.1 or ./portscan.py https://site.com")
else:
        for port in range(1,65535):
                mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client = mysocket.connect_ex((argv,port))

                if (client == 0):
                        print ("Port:",port,"[OPEN]")
                        mysocket.close()
