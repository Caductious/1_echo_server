import socket
from datetime import datetime

port=9075
sock = socket.socket()
file=open('log.txt', 'a+')
sock.bind(('', port))
file.write((datetime.now().strftime("%m/%d/%Y, %H:%M:%S")) + " Сервер запущен\n")
shutdown=False
while not shutdown:
	sock.listen(0)
	file.write((datetime.now().strftime("%m/%d/%Y, %H:%M:%S")) + f" Порт {port} прослушивается\n")
	conn, addr = sock.accept()
	print(f"Клиент {addr[0]}:{addr[1]} подключен\n")

	while True:
		msg = ''
		data = conn.recv(1024)
		if not data:
				file.write((datetime.now().strftime("%m/%d/%Y, %H:%M:%S")) + " Coобщения приняты и отправлено обратно\n")
				msg=''
				break
		msg += data.decode()
		if msg=="exit":
			file.write((datetime.now().strftime("%m/%d/%Y, %H:%M:%S")) + " Клиент отключен\n")
			conn.close()
			break
		if msg =="shutdown now":
			sock.close()
			shutdown=True
			break
		file.write((datetime.now().strftime("%m/%d/%Y, %H:%M:%S")) + f' Сообщение {msg} получено\n')
		conn.send(msg.upper().encode())
		file.write((datetime.now().strftime("%m/%d/%Y, %H:%M:%S")) + ' Сообщение обработано и отправлено\n')
file.write((datetime.now().strftime("%m/%d/%Y, %H:%M:%S")) + ' Сервер отключен\n')
file.close()