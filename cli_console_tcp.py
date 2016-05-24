import socket
import sys

SERVER_PORT = 8888
SERVER_IP = '127.0.0.1'

request = "Could you send me a reply? Please."

# socket creation.
# using a stream socket (TCP).
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to server.
clientSocket.connect((SERVER_IP, SERVER_PORT))
print
print "Connected to server on IP: " + SERVER_IP + " and port: " + str(SERVER_PORT)
print
print "---------- SENDING ----------"

print "Choose between sending a standard message (1) or your own message (2)"
choice = sys.stdin.readline()
int_choice = int(choice)
if int_choice == 2:
	print "Please type your message. Press ENTER to send."
	request = sys.stdin.readline()
elif int_choice != 1:
	print "Your choice is invalid. Bye..."
	clientSocket.close()
	sys.exit()

# send a message to server.
# address and port already known
clientSocket.send(request)
print "Message sent: " + request
print
print "---------- RECEIVING ----------"

# waiting to receive the reply message
msg = clientSocket.recv(1024)

print "Message received: " + msg
print
print "The end..."

# close the socket
clientSocket.close()
