import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "192.168.1.169" # hardcoded server's ip
port = 1105
client_socket.connect((host, port))

print("GUESSING GAME")
print("Enter 'END GAME' to quit the game")
print("Enter 'NEW GAME' to start a new game")

while True:
	msg = input("Please enter a guess, or a command: ")
	client_socket.send(msg.encode('ascii'))

	status_code = client_socket.recv(1024).decode('ascii')
	msg_back = client_socket.recv(1024).decode('ascii')
	print(msg_back)

	if (status_code == "1"):
		break

client_socket.close()
