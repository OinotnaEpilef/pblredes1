from socket import *

host = '172.16.112.1'
port = 10000

client = socket(AF_INET, SOCK_STREAM)
client.connect((host, port))

while 1:
    message = input ('digite sua mensagem: ')
    client.send(message.encode())