import socket

SERVER_PORT = 8888
reply = "Here's your reply"

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind(('',SERVER_PORT))

print
print "---------- RECEIVING ----------"

(msg,addr) = serverSocket.recvfrom(1024)

print "Message received: " + msg
print "Sender: IP:" + addr[0] + "   Port: " + str(addr[1])
print
print "Word received after question mark: " + msg.split('?')[1]
print

print "---------- SENDING ----------"

serverSocket.sendto(reply,(addr[0],addr[1]))

print "Message replied: " + reply
print
print "The end..."

serverSocket.close()
