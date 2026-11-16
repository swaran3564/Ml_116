
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('localhost', 1234))

msg, addr = s.recvfrom(1024)
print("Client:", msg.decode())

s.sendto("Hello Client".encode(), addr)
s.close()
