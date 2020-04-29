# Write your code here :-)
import socket
import numpy as np
import time

t = np.linspace(0,2*np.pi,100)
y0 = np.float16(np.sin(t))
y1 = np.float16(0.5*np.sin(t)*np.sin(2*t))
i=0


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ''  #or host = '192.168.16.134'
port = 8089
server.bind((host,port))
server.listen(1)

try:
  while True:
    s, addr = server.accept()
    cmnd = s.recv(4)
    print(cmnd)
    #print(str(client_msg))
    if 'INIT' in str(cmnd):
        st0 = "CH0"+str(y0[i])+"\n"
        st1 = "CH1"+str(y1[i])+"\n"
        byt0 = st0.encode()
        byt1 = st1.encode()
        s.send(byt0)
        s.send(byt1)

    i += 1
    if i>=99:
        i = 0
except KeyboardInterrupt:
   s.close()
