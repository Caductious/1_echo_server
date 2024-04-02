import socket
from time import sleep

sock = socket.socket()
sock.setblocking(1)
sock.connect(('localhost', 9075))
while True:
    msg = input("Введите строку:")
    if msg == '':
        break
    sock.send(msg.encode())
    data = sock.recv(1024)
    print(data.decode())
    msg=''
sock.close()