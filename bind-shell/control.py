#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Control module. Send commands to server
# bind-tcp

import socket

target = 'localhost'
port = 9090

#sock.connect((target, port))
try:
	while True:
		try:
			#print("Initializating socket...")
			sock = socket.socket()
			sock.connect((target, port))
		except Exception as e:
			print("Error when connecting {}".format(e))
		print(sock.recv(1024))
		command = raw_input('Command: ')
		try:
			sock.send(command)
			data = sock.recv(1024) # receive answer
			print(data)
		except:
			print("Couldn\'t send command")

		#print ("Destroying sock")
		sock.close()
except: # may be it helps with Ctrl+C 
	sock.close()
finally:
	sock.close()

'''
Клиент так же постоянно подключен к серверу, отправляет сообщения и получает ответ.
Далее снова отправляет и получает.
'''