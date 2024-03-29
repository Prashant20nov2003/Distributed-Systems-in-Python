from socket  import *

s = socket(AF_INET, SOCK_STREAM) 
(conn, addr) = s.accept()  # returns new socket and addr. client 
while True:                # forever
  data = conn.recv(1024)   # receive data from client
  if not data: break       # stop if client stopped
  msg = data.decode()+"*"  # process the incoming data into a response
  conn.send(msg.encode())  # return the response
conn.close()               # close the connection
