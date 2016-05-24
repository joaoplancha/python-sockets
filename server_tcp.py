import socket

SERVER_PORT = 8888
reply = "Sure, here's your reply"

# socket creation.
# using a stream socket (TCP).
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# socket bind to localhost on SERVER_PORT defined above.
serverSocket.bind(('', SERVER_PORT))

# socket listening for incoming connection requests.
# number between brackets is the number of simultaneous connections supported.
serverSocket.listen(1)

# when a new connection is received, accept it.
# create a new socket object to refer to that (in case more connections are coming).
# get the address of the sender, although not needed.
newClientSocket, addr = serverSocket.accept()

print
print "New client connected"
print "IP:" + addr[0] + "   Port: " + str(addr[1])
print
print "---------- RECEIVING ----------"

# waiting to receive the message
msg = newClientSocket.recv(1024)

print "Message received: " + msg
print
print "Word received after question mark: " + msg.split('?')[1]
print
print "---------- SENDING ----------"

# send the reply
newClientSocket.send(reply)

print "Message replied: " + reply
print
print "The end..."

# close the sockets
newClientSocket.close()
serverSocket.close()
