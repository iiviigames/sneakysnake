#!/usr/bin/python3

#	Using hackthissite.org

#		IMPORTS			#
#-----------------------#
import socket

#		GLOBALS			#
#-----------------------#
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)

host = "137.74.187.103"
localhost = "192.168.1.1"
port = 443
localport = 22

#		FUNCTIONS		#
#-----------------------#


def port_scanner(port):
	"""
	Finds out if the port on a given host is open.
	"""
	if s.connect_ex((host, port)):
		print("The port is closed")
	else:
		print("The port is open")


def get_ip():
	"""
	Requests an IP Address and a Port Number from the user.
	"""
	host = input("Please enter the IP you wish to scan\n::: ")
	port = str(input("Please enter the port number you wish to use\n::: "))
	return host, port


def connect_to(ip, port):
	s.connect((ip, int(port)))


def log_connection(amt):
	print(s.recv(1024))

#		MAINLOOP		#
#-----------------------#

host, port = get_ip()
# print(host, port)
#port_scanner(port)
