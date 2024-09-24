# Relatório PBL 1 - TEC 502 - MI-Concorrência e Conectividade
# Antônio Felipe Ferreira de Jesus Moreira
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