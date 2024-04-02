import socket
from time import sleep

sock = socket.socket()
sock.setblocking(1)
try:
    sock.connect(('localhost', 9075))
    print('Соединение установлено')
except ConnectionRefusedError:
    print('Ошибка подключения')
while True:
    msg = input("Введите строку:")
    if msg == 'exit':
        print('Была подана команда, завершение работы')
        sock.send(msg.encode())
        break
    if msg == 'shutdown now':
        print('Была подана команда, Выключения сервера')
        sock.send(msg.encode())
        break
    sock.send(msg.encode())
    print(f"Сообщение {msg} отправлено серверу")
    data = sock.recv(1024)
    print(data.decode())
    print("Сообщение успешно получено")
    msg=''
sock.close()