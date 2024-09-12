from socket import *
from threading import Thread, Lock

# Definindo as rotas e trechos
rotas = {
    "Belém-Curitiba": [
        [("Belém", "Fortaleza"), ("Fortaleza", "São Paulo"), ("São Paulo", "Curitiba")],
        [("Belém", "Brasília"), ("Brasília", "Curitiba")]
    ],
    "Rio de Janeiro-Porto Alegre": [
        [("Rio de Janeiro", "São Paulo"), ("São Paulo", "Porto Alegre")],
        [("Rio de Janeiro", "Florianópolis"), ("Florianópolis", "Porto Alegre")]
    ],
    "Salvador-Manaus": [
        [("Salvador", "Brasília"), ("Brasília", "Manaus")],
        [("Salvador", "Recife"), ("Recife", "Manaus")]
    ]
}

# Trechos comprados
trechos_comprados = {rota: [[False] * len(trechos) for trechos in caminhos] for rota, caminhos in rotas.items()}
lock = Lock()  # Lock para garantir que apenas um cliente possa comprar um trecho por vez

def handle_client(con, adr):
    con.send("Bem-vindo ao sistema de compra de passagens!\n".encode())
    con.send("Rotas disponíveis:\n".encode())
    for i, rota in enumerate(rotas.keys()):
        con.send(f"{i+1}. {rota}\n".encode())

    con.send("Escolha uma rota pelo número: ".encode())
    rota_idx = int(con.recv(1024).decode()) - 1
    rota_escolhida = list(rotas.keys())[rota_idx]
    
    con.send(f"Você escolheu a rota: {rota_escolhida}\n".encode())
    con.send("Caminhos disponíveis:\n".encode())

    for i, caminho in enumerate(rotas[rota_escolhida]):
        con.send(f"{i+1}. Caminho {i+1}:\n".encode())
        for trecho in caminho:
            con.send(f"   - {trecho}\n".encode())

    con.send("Escolha um caminho pelo número: ".encode())
    caminho_idx = int(con.recv(1024).decode()) - 1
    caminho_escolhido = rotas[rota_escolhida][caminho_idx]

    con.send("Trechos disponíveis nesse caminho:\n".encode())
    
    with lock:
        for i, trecho in enumerate(caminho_escolhido):
            status = "Disponível" if not trechos_comprados[rota_escolhida][caminho_idx][i] else "Indisponível"
            con.send(f"{i+1}. {trecho} - {status}\n".encode())

        con.send("Escolha um trecho pelo número: ".encode())
        trecho_idx = int(con.recv(1024).decode()) - 1

        if not trechos_comprados[rota_escolhida][caminho_idx][trecho_idx]:
            trechos_comprados[rota_escolhida][caminho_idx][trecho_idx] = True
            con.send(f"Trecho {caminho_escolhido[trecho_idx]} comprado com sucesso!\n".encode())
        else:
            con.send("Trecho já foi comprado por outro cliente!\n".encode())
    
    con.close()

def main():
    host = '172.16.103.8'
    port = 2000

    server = socket(AF_INET, SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print("Servidor de passagens aéreas rodando...")

    while True:
        con, adr = server.accept()
        Thread(target=handle_client, args=(con, adr)).start()

if __name__ == "__main__":
    main()
