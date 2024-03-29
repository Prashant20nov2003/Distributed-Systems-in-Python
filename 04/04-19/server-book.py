from socket  import *

class Server:
  def run(self):
    s = socket(AF_INET, SOCK_STREAM) 
    s.bind((HOST, PORT))  
    s.listen(1)       
    (conn, addr) = s.accept()  # returns new socket and addr. client 
    while True:                # forever
      data = conn.recv(1024)   # receive data from client
      if not data: break       # stop if client stopped
      conn.send(data+b"*")     # return sent data plus an "*"
    conn.close()               # close the connection
