import socket

SERVER_PORT = 8888
SERVER_IP   = '127.0.0.1'

request = "Can you send me a reply? Please."

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print "---------- SENDING ----------"

clientSocket.sendto(request, (SERVER_IP, SERVER_PORT))

print "Message sent: " + request
print
print "---------- RECEIVING ----------"

(msg,addr) = clientSocket.recvfrom(1024)

print "Message received: " + msg
print "Sender: IP:" + addr[0] + "   Port: " + str(addr[1])
print
print "Third word that was received: " + msg.split()[2]
print
print "The end..."

clientSocket.close()
