from socket import *

host = gethostname()
port = 10000

print (f'HOST: {host}, PORT: {port}')
server = socket(AF_INET, SOCK_STREAM)
server.bind((host, port))
server.listen(2)

while 1:
    con, adr = server.accept()
    while 1:
        message = con.recv(1024)
        print(message.decode())