import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "0.0.0.0" # hardcoded local ip

port = 10004

server_socket.bind((host, port))

server_socket.listen(1)

while True:
	client_socket, addr = server_socket.accept()
	msg = client_socket.recv(1024)
	msg = msg.decode().upper()
	client_socket.send(msg.encode())
	client_socket.close()