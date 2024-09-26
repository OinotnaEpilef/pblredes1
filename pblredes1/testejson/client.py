from socket import *
import json

# Função para enviar mensagem JSON ao servidor
def enviar_mensagem(client, mensagem):
    client.send(json.dumps(mensagem).encode())

# Função para receber mensagem JSON do servidor
def receber_mensagem(client):
    return json.loads(client.recv(1024).decode())

# Função principal do cliente
def main():
    host = '172.16.103.2'
    port = 10000

    client = socket(AF_INET, SOCK_STREAM)
    client.connect((host, port))

    while True:
        mensagem = receber_mensagem(client)

        if mensagem["tipo"] == "info":
            print(mensagem["dados"])

        elif mensagem["tipo"] == "rotas":
            print("Rotas disponíveis:")
            for i, rota in enumerate(mensagem["dados"], 1):
                print(f"{i}. {rota}")
            escolha = int(input("Escolha uma rota pelo número: "))
            enviar_mensagem(client, {"dados": escolha})

        elif mensagem["tipo"] == "caminhos":
            print("Caminhos disponíveis:")
            for caminho in mensagem["dados"]:
                print(f"Caminho {caminho['caminho']}:")
                for trecho in caminho['trechos']:
                    print(f"   - {trecho['origem']} -> {trecho['destino']} com {trecho['passagens']} passagens disponíveis")
            escolha = int(input("Escolha um caminho pelo número: "))
            enviar_mensagem(client, {"dados": escolha})

        elif mensagem["tipo"] == "sucesso":
            print(mensagem["dados"])

        elif mensagem["tipo"] == "erro":
            print(mensagem["dados"])

        elif mensagem["tipo"] == "pergunta":
            resposta = input(mensagem["dados"] + " ")
            enviar_mensagem(client, {"dados": resposta})

        if mensagem["tipo"] == "info" and "Até a próxima" in mensagem["dados"]:
            break

if __name__ == "__main__":
    main()
