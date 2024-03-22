import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = "0.0.0.0" # hardcoded local ip

port = 10004

server_socket.bind((host, port))

while True:
	msg, client_address = server_socket.recvfrom(2048)
	msg = msg.decode().upper()
	server_socket.sendto(msg.encode(), client_address)