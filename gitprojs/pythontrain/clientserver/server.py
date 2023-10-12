import socket

s = socket.socket()
host = socket.gethostname()
port = 12346
s.bind((host, port))

s.listen(5)
while True:
    c, addr = s.accept()
    print('адрес подключения:', addr)
    c.send('Добро пожаловать')
    c.close


