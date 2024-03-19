import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

host = "192.168.92.136" # hardcoded local ip

port = 10004

server_socket.bind((host, port))

server_socket.listen(1)

client_socket, addr = server_socket.accept()

while True:
	msg = client_socket.recv(1024).decode('ascii')
	if (msg == "quit"):
		client_socket.close()
		break
	msg = msg.upper()
	print(msg)
	client_socket.send(msg.encode('ascii'))

server_socket.close()