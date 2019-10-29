#!/usr/bin/python3

#   Using hackthissite.org

#       IMPORTS         #
#-----------------------#
import socket

#       GLOBALS         #
#-----------------------#
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "137.74.187.103"
port = 443

#       FUNCTIONS       #
#-----------------------#
def port_scanner(port):
    if s.connect_ex((host, port)):
        print("The port is closed")
    else:
        print("The port is open")

port_scanner(port)