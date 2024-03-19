import socket
import random


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

host = socket.gethostname()
port = 1105
server_socket.bind((host, port))

server_socket.listen(1)

client_socket, addr = server_socket.accept()

x = random.randint(1, 100)

while True:
	msg = client_socket.recv(1024).decode('ascii')

	print("Received message from client:", msg)

	msg = msg.upper()
	print("Edited message from client:", msg)
	# quit game
	if (msg == "END GAME"):
		client_socket.send("1".encode('ascii'))
		client_socket.send("GOOD BYE, SEE YOU AGAIN !".encode('ascii'))
		break
	elif (msg == "NEW GAME"):
		x = random.randint(1, 100)
		client_socket.send("2".encode('ascii'))
		client_socket.send("New game started!!!".encode('ascii'))
		continue

	# check if the message is a number
	try:
		guess = int(msg)
		client_socket.send("3".encode('ascii'))
		if (guess == x):
			client_socket.send("Correct!!!\nNew game started!!!".encode('ascii'))
		elif (guess < x):
			client_socket.send("Too low!!!".encode('ascii'))
		else:
			client_socket.send("Too high!!!".encode('ascii'))
	except:
		client_socket.send("4".encode('ascii'))
		client_socket.send("Please enter a number!!!".encode('ascii'))
		continue

client_socket.close()
server_socket.close()