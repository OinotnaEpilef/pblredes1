from socket import *

host = '172.16.112.1'
port = 10000

print (f'HOST: {host}, PORT: {port}')
server = socket(AF_INET, SOCK_STREAM)
server.bind((host, port))
server.listen(3)

while 1:
    con, adr = server.accept()
    while 1:
        message = con.recv(1024)
        print(message.decode())