import socket

SERVER_PORT = 8888
SERVER_IP   = '127.0.0.1'

request = "Can you send me a reply? Please."

# socket creation.
# using a datagram socket (UDP).
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print "---------- SENDING ----------"

# send something to the server (defined above).
clientSocket.sendto(request, (SERVER_IP, SERVER_PORT))

print "Message sent: " + request
print
print "---------- RECEIVING ----------"

# waiting for something to come through the socket.
(msg,addr) = clientSocket.recvfrom(1024)

print "Message received: " + msg
print "Sender: IP:" + addr[0] + "   Port: " + str(addr[1])
print
print "Third word that was received: " + msg.split()[2]
print
print "The end..."

# close the socket
clientSocket.close()
