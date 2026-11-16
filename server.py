
import socket

s = socket.socket()
s.bind(('localhost', 1234))
s.listen(1)

c, addr = s.accept()
print("Connected:", addr)

msg = c.recv(1024).decode()
print("Client:", msg)

c.send("Hello Client".encode())
c.close()
s.close()
