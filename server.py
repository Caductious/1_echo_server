import socket

port=9075
sock = socket.socket()
sock.bind(('', port))
print("Сервер запущен")
sock.listen(0)
print("Порт",port,"прослушивается")
conn, addr = sock.accept()
print(f"Клиент {addr[0]}:{addr[1]} подключен")

while True:
	msg = ''
	data = conn.recv(1024)
	if not data:
			print("Coобщения приняты и отправлено обратно")
			msg=''
			break
	msg += data.decode()
	if msg=="ClientShutsDownNow":
		print('Клиент отключен')
		break
	print(f'Сообщение {msg} получено')
	conn.send(msg.upper().encode())
	print('Сообщение обработано и отправлено')

conn.close()
print('Сервер отключен')