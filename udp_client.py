
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.sendto("Hello Server".encode(), ('localhost', 1234))
msg, addr = s.recvfrom(1024)

print("Server:", msg.decode())
s.close()
