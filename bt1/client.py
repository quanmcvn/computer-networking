import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "192.168.92.136" # hardcoded local ip

port = 10004

client_socket.connect((host, port))

while True:
	msg = input()
	client_socket.send(msg.encode('ascii'))
	print(client_socket.recv(1024).decode('ascii'))
	if (msg == "quit"):
		break

client_socket.close()
