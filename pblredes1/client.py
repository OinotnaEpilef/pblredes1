#arquivo cliente correto para o pbl
from socket import *

def main():
    host = '172.16.103.3'
    port = 10000

    client = socket(AF_INET, SOCK_STREAM)
    client.connect((host, port))

    while True:
        message = client.recv(1024).decode()
        print(message)
        if "Escolha" in message:
            choice = input("Digite sua escolha: ")
            client.send(choice.encode())

if __name__ == "__main__":
    main()
