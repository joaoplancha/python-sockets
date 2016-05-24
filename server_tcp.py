import socket

SERVER_PORT = 8888
reply = "Sure, here's your reply"

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serverSocket.bind(('', SERVER_PORT))

serverSocket.listen(2)

newClientSocket, addr = serverSocket.accept()

print
print "New client connected"
print "IP:" + addr[0] + "   Port: " + str(addr[1])
print
print "---------- RECEIVING ----------"

msg = newClientSocket.recv(1024)

print "Message received: " + msg
print
print "Word received after question mark: " + msg.split('?')[1]
print
print "---------- SENDING ----------"

newClientSocket.send(reply)

print "Message replied: " + reply
print
print "The end..."

newClientSocket.close()
serverSocket.close()
