import socket
import time

UDP_IP = "127.0.0.1"
UDP_PORT = 33333
MESSAGE = b"Hello, World!"
cont = 0

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

while True:
    print(cont)
    sock.sendto(str(cont).encode(), (UDP_IP, UDP_PORT))
    cont = cont + 1
    time.sleep(1)