# Relatório PBL 1 - TEC 502 - MI-Concorrência e Conectividade
Antônio Felipe Ferreira de Jesus Moreira

UEFS - 23 de setembro de 2024

email: felipetompsomf18@gmail.com
# Resumo(Abstract):
# Introdução: 
A indústria da aviação mudou drasticamente nos últimos anos, com o surgimento de transportadoras de baixo custo (LCCs) democratizando o transporte aéreo. Estas empresas promovem o turismo e a conectividade global, tornando as viagens aéreas acessíveis a cada vez mais pessoas, oferecendo voos acessíveis. Este relatório descreve a implementação de um sistema de compra de passagens baseado em um servidor utilizando comunicação TCP/IP, projetado para proporcionar uma experiência simplificada e eficiente aos clientes. O sistema permite que os usuários selecionem os segmentos de voo disponíveis, garantindo prioridade por ordem de chegada. Com isso, foi solicitado aos alunos da disciplina do MI de redes (TEC 502 - MI-Concorrência e Conectividade) que desenvolvessem uma aplicação que fizesse uma comunicação com servidor utilizando protocolos TCP/IP para solucionar o problema
# Fundamentação teórica
1. Comunicação em sistemas distribuídos

Um sistema distribuído consiste em vários componentes que se comunicam entre si para executar tarefas em conjunto. A comunicação em sistemas distribuídos pode ser alcançada de diversas maneiras, sendo o protocolo TCP/IP um dos mais populares. Este protocolo fornece um conjunto de regras para troca de dados entre dispositivos em uma rede.

Protocolo TCP/IP: TCP (Protocolo de Controle de Transmissão) é um protocolo orientado a conexão que garante transmissão confiável de dados. Ele segmenta as mensagens em pacotes e remonta esses pacotes no destino, garantindo que a comunicação não seja perdida. IP (Internet Protocol) é responsável por endereçar e rotear pacotes de dados na rede.

Sockets: Um soquete é uma interface de programação que permite a comunicação entre processos, sejam eles locais ou distribuídos. Eles são amplamente utilizados no desenvolvimento de aplicações que requerem comunicação em rede, como servidores e clientes.

2. API (Interface de Programação de Aplicativo)

Uma API é um conjunto de definições e protocolos que permitem que diferentes softwares interajam entre si. Eles definem como os componentes do sistema devem se comunicar e são a base para a construção de aplicativos escaláveis ​​e modulares.

API de sockets: Na arquitetura de software que utiliza soquetes, a API de soquete fornece a funcionalidade necessária para criar e gerenciar conexões de rede, permitindo que servidores e clientes se comuniquem de forma eficiente.

3. Concorrência e Controle de Acesso

Em aplicações que atendem a múltiplos usuários simultaneamente, como no caso do sistema de compra de passagens aéreas, o controle de concorrência é um aspecto crítico a ser considerado. Isso garante que os dados compartilhados não sejam corrompidos por acessos simultâneos.

Locks: O uso de locks (bloqueios) é uma técnica comum para gerenciar o acesso a recursos compartilhados. Em Python, o módulo threading fornece mecanismos para garantir que apenas um thread tenha acesso a uma seção crítica do código por vez, evitando problemas de inconsistência de dados.
# Metodologia
1. Definição de requisitos

Durante esta fase inicial, os requisitos do sistema são reunidos e definidos com base nas necessidades da companhia aérea e do usuário final. Os principais requisitos identificados incluem:

Recursos do sistema: conferir rotas disponíveis, escolher os segmentos e caminhos a percorrer, verificar a disponibilidade de ingressos, e fazer uma compra de ingresso. Requisitos de disponibilidade: fornecer aos usuários uma interface amigável e intuitiva, propor uma esposta rápida às solicitações dos clientes, e mostrar informações claras sobre rotas e ingressos.

2. Análise da Arquitetura

Com os requisitos definidos, a próxima etapa foi a elaboração da arquitetura do sistema. A arquitetura proposta é baseada em um modelo cliente-servidor, ondeo servidor é responsável por gerenciar as rotas, interagir com os clientes e processar as compras de passagens, e o cliente é a interface que permite ao usuário interagir com o servidor para consultar rotas e realizar compras.

3. Implementação

A implementação do sistema é realizada em Python, utilizando a biblioteca de sockets para comunicação entre cliente e servidor. As principais etapas de implementação incluem o desenvolvimento de servidor, no qual foi criada uma lógica para gerar rotas e caminhos aleatórios entre cidades, lista rotas, verifica a disponibilidade e realiza a compra de passagens. Também foram utilizadas threads para gerenciar várias conexões de clientes simultaneamente para garantir que o servidor possa atender vários usuários ao mesmo tempo.

Já no desenvolvimento do cliente, foi criada uma interface simples no terminal do python para interagir com o servidor e implementar as funções para receber mensagens do servidor e enviar respostas, como selecionar rotas e caminhos.