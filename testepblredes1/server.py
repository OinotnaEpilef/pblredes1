from socket import *
from threading import Thread, Lock
import random

# Lista de 10 cidades
cidades = ["Belém", "Fortaleza", "Brasília", "São Paulo", "Curitiba", 
           "Rio de Janeiro", "Porto Alegre", "Salvador", "Manaus", "Recife"]

# Lock para controlar acesso a dados compartilhados
lock = Lock()

# Função que gera as rotas entre as cidades com caminhos e trechos
def gerar_rotas(cidades):
    rotas = {}
    for i in range(len(cidades)):
        for j in range(len(cidades)):
            if i != j:
                rota_nome = f"{cidades[i]}-{cidades[j]}"
                rotas[rota_nome] = []
                num_caminhos = random.randint(1, 3)
                for _ in range(num_caminhos):
                    caminho = []
                    cidades_intermediarias = random.sample(cidades[:i] + cidades[i+1:], random.randint(1, 3))
                    caminho_cidades = [cidades[i]] + cidades_intermediarias + [cidades[j]]
                    for k in range(len(caminho_cidades) - 1):
                        caminho.append((caminho_cidades[k], caminho_cidades[k+1], random.randint(2, 5)))  # Gerar passagens
                    rotas[rota_nome].append(caminho)
    return rotas

# Função para enviar mensagens ao cliente
def enviar_mensagem(con, mensagem):
    con.send(f"{mensagem}\n".encode())

# Função para listar rotas disponíveis para o cliente
def listar_rotas(con, rotas):
    enviar_mensagem(con, "Rotas disponíveis:")
    for i, rota in enumerate(rotas.keys()):
        enviar_mensagem(con, f"{i+1}. {rota}")
    
    enviar_mensagem(con, "Escolha uma rota pelo número:")
    rota_idx = int(con.recv(1024).decode().strip()) - 1
    return list(rotas.keys())[rota_idx]

# Função para listar caminhos dentro de uma rota
def listar_caminhos(con, rota_escolhida, rotas):
    enviar_mensagem(con, f"Você escolheu a rota: {rota_escolhida}")
    enviar_mensagem(con, "Caminhos disponíveis para essa rota:")
    
    for i, caminho in enumerate(rotas[rota_escolhida]):
        enviar_mensagem(con, f"{i+1}. Caminho {i+1}:")
        for trecho in caminho:
            enviar_mensagem(con, f"   - {trecho[0]} -> {trecho[1]} com {trecho[2]} passagens disponíveis")
    
    enviar_mensagem(con, "Escolha um caminho pelo número:")
    caminho_idx = int(con.recv(1024).decode().strip()) - 1
    return rotas[rota_escolhida][caminho_idx], caminho_idx

# Função para verificar disponibilidade dos trechos
def verificar_disponibilidade(caminho):
    for trecho in caminho:
        if trecho[2] <= 0:  # Sem passagens disponíveis
            return False
    return True

# Função para realizar a compra de todos os trechos de uma rota
def realizar_compra(caminho):
    for i, trecho in enumerate(caminho):
        caminho[i] = (trecho[0], trecho[1], trecho[2] - 1)  # Decrementa o número de passagens

# Função para lidar com um cliente
def handle_client(con, adr, rotas):
    enviar_mensagem(con, "Bem-vindo ao sistema de compra de passagens!")
    
    while True:
        rota_escolhida = listar_rotas(con, rotas)
        caminho_escolhido, caminho_idx = listar_caminhos(con, rota_escolhida, rotas)

        enviar_mensagem(con, "Verificando a disponibilidade dos trechos...")

        with lock:  # Bloquear para garantir consistência
            if verificar_disponibilidade(caminho_escolhido):
                realizar_compra(caminho_escolhido)
                enviar_mensagem(con, "Compra realizada com sucesso! Todos os trechos foram adquiridos.")
            else:
                enviar_mensagem(con, "Não foi possível realizar a compra. Um ou mais trechos não possuem passagens suficientes.")
        
        # Perguntar ao cliente se deseja realizar outra compra ou sair
        enviar_mensagem(con, "Deseja realizar outra compra? (sim/não)")
        resposta = con.recv(1024).decode().strip().lower()
        if resposta != "sim":
            enviar_mensagem(con, "Obrigado por usar o sistema de passagens. Até a próxima!")
            break

    con.close()

# Função principal do servidor
def main():
    host = '0.0.0.0'  # Escuta em todas as interfaces
    port = 10000

    rotas = gerar_rotas(cidades)
    
    server = socket(AF_INET, SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print("Servidor de passagens aéreas rodando...")

    while True:
        con, adr = server.accept()
        Thread(target=handle_client, args=(con, adr, rotas)).start()

if __name__ == "__main__":
    main()
