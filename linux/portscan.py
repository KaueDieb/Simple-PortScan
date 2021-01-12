import socket

port = input("Enter the port: ")
ip = raw_input("Enter the ip: ")

print "PORT|STATUS"
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(0.5)
code = client.connect_ex((ip, port))
if code == 0:
	print port, "[OPEN]"
else: 
	print port, "[CLOSED]"
