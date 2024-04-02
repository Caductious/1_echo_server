import socket

port=9075
sock = socket.socket()
sock.bind(('', port))
print("Сервер запущен")
sock.listen(0)
print("Порт",port,"работяга")
conn, addr = sock.accept()
print("Клиент подключен")
print("Адрес клиента:",addr[0])
print("Порт клиента:",addr[1])


while True:
	msg = ''
	data = conn.recv(1024)
	if not data:
			print(" Coобщение принято")
			msg=''
			break
	msg += data.decode()
	conn.send(msg.upper().encode())

print(msg)

conn.close()
