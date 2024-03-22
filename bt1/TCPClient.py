import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1" # hardcoded local ip

port = 10004

client_socket.connect((host, port))

msg = input("Input lowercase sentence:")

client_socket.send(msg.encode())

print(client_socket.recv(1024).decode())

client_socket.close()
