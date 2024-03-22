import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = "127.0.0.1" # hardcoded local ip

port = 10004

message = input('Input lowercase sentence:')

client_socket.sendto(message.encode(),(host, port))

msg = client_socket.recv(1024)

print(msg.decode())

client_socket.close()