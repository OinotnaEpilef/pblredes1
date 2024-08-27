from socket import *

host = gethostname()
port = 10000

client = socket(AF_INET, SOCK_STREAM)
client.connect((host, port))

while 1:
    message = input ('digite sua mensagem: ')
    client.send(message.encode())