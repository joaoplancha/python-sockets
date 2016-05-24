import socket

SERVER_PORT = 8888
SERVER_IP = '127.0.0.1'

request = "Could you send me a reply? Please."

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clientSocket.connect((SERVER_IP, SERVER_PORT))
print
print "Connected to server on IP: " + SERVER_IP + " and port: " + str(SERVER_PORT)
print
print "---------- SENDING ----------"

clientSocket.send(request)

print "Message sent: " + request
print
print "---------- RECEIVING ----------"

msg = clientSocket.recv(1024)

print "Message received: " + msg
print
print "Third word that was received: " + msg.split()[2]
print
print "The end..."

clientSocket.close()
