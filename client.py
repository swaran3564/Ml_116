
import socket

s = socket.socket()
s.connect(('localhost', 1234))

s.send("Hello Server".encode())
msg = s.recv(1024).decode()

print("Server:", msg)
s.close()
