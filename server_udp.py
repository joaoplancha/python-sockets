import socket

SERVER_PORT = 8888
reply = "Here's your reply"

# socket creation.
# using a datagram socket (UDP).
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# socket bind to localhost on SERVER_PORT defined above.
serverSocket.bind(('',SERVER_PORT))

print
print "---------- RECEIVING ----------"

# waiting for something to come through the socket.
# msg = message received, addr = ip:port of the sender.
(msg,addr) = serverSocket.recvfrom(1024)

print "Message received: " + msg
print "Sender: IP:" + addr[0] + "   Port: " + str(addr[1])
print
print "Word received after question mark: " + msg.split('?')[1]
print

print "---------- SENDING ----------"

# send something back the way it came from. reply defined above.
serverSocket.sendto(reply,(addr[0],addr[1]))

print "Message replied: " + reply
print
print "The end..."

# close the socket
serverSocket.close()
