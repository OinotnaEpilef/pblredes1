# Relatório PBL 1 - TEC 502 - MI-Concorrência e Conectividade
Antônio Felipe Ferreira de Jesus Moreira

UEFS - 23 de setembro de 2024

email: felipetompsomf18@gmail.com
# Resumo(Abstract):
Este documento apresenta a criação de um sistema para a compra de passagens aéreas, elaborado com base na comunicação TCP/IP, como parte da disciplina de redes (TEC 502 - MI-Concorrência e Conectividade). O objetivo do sistema é oferecer uma experiência mais ágil para os usuários, permitindo que façam a escolha de rotas e realizem a aquisição de passagens de forma eficaz. A base teórica abrange conceitos sobre comunicação em sistemas distribuídos, APIs e controle de concorrência. Já a metodologia incluiu a definição de requisitos, análise da arquitetura cliente-servidor e implementação em Python, utilizando sockets e threads. Os resultados obtidos confirmaram que o sistema atende às especificações propostas, assegurando comunicação eficiente e integridade dos dados durante a concorrência. Testes funcionais, de concorrência e usabilidade validaram a eficácia do sistema, demonstrando sua viabilidade para o mercado de aviação de baixo custo.
# Introdução: 
A indústria da aviação mudou drasticamente nos últimos anos, com o surgimento de transportadoras de baixo custo (LCCs) democratizando o transporte aéreo. Estas empresas promovem o turismo e a conectividade global, tornando as viagens aéreas acessíveis a cada vez mais pessoas, oferecendo voos acessíveis. Este relatório descreve a implementação de um sistema de compra de passagens baseado em um servidor utilizando comunicação TCP/IP que foi solicitado aos alunos da disciplina do MI de redes (TEC 502 - MI-Concorrência e Conectividade), projetado para proporcionar uma experiência simplificada e eficiente aos clientes. O sistema permite que os usuários selecionem os segmentos de voo disponíveis, garantindo prioridade por ordem de chegada.
# Fundamentação teórica
1. Comunicação em sistemas distribuídos

Um sistema distribuído consiste em vários componentes que se comunicam entre si para executar tarefas em conjunto. A comunicação em sistemas distribuídos pode ser alcançada de diversas maneiras, sendo o protocolo TCP/IP um dos mais populares. Este protocolo fornece um conjunto de regras para troca de dados entre dispositivos em uma rede.

Protocolo TCP/IP: TCP (Protocolo de Controle de Transmissão) é um protocolo orientado a conexão que garante transmissão confiável de dados. Ele segmenta as mensagens em pacotes e remonta esses pacotes no destino, garantindo que a comunicação não seja perdida. IP (Internet Protocol) é responsável por endereçar e rotear pacotes de dados na rede.

Sockets: Um socket é uma interface de programação que permite a comunicação entre processos, sejam eles locais ou distribuídos. Eles são amplamente utilizados no desenvolvimento de aplicações que requerem comunicação em rede, como servidores e clientes.

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
# Resultados e discussões
O sistema implementado possibilitou uma comunicação eficiente entre os clientes e o servidor, permitindo a busca e compra de passagens aéreas de maneira prática e ágil. Durante os testes, observou-se que o uso de locks garantiu a integridade dos dados, prevenindo problemas de concorrência quando vários clientes tentavam adquirir passagens ao mesmo tempo. As funcionalidades desenvolvidas, como a listagem de rotas e a verificação de disponibilidade, corresponderam aos requisitos estabelecidos na fase inicial do projeto.

Ademais, a experiência obtida durante o desenvolvimento do sistema sublinhou a relevância de um bom design de APIs, além da necessidade de levar em conta aspectos como escalabilidade e segurança em sistemas que operam com transações financeiras. A implementação do sistema evidenciou não apenas a viabilidade técnica da solução apresentada, mas também o potencial de crescimento e adaptação às demandas do setor de aviação de baixo custo.

**Testes:**

Após a implementação, a etapa de testes se mostrou crucial para assegurar o funcionamento adequado do sistema e a conformidade com os requisitos estabelecidos. Os testes executados incluíram:

**Testes Funcionais:**
- Validação das funcionalidades relativas à consulta de rotas e à aquisição de passagens.
- Verificação da lógica que conferia a disponibilidade de assentos, assegurando que a compra fosse impedida na ausência de lugares livres.

**Testes de Concorrência:**
- Simulação de vários usuários tentando efetuar compras ao mesmo tempo, para avaliar se o sistema conseguia gerenciar de forma correta o acesso a dados compartilhados, utilizando bloqueios para prevenir conflitos.

**Testes de Usabilidade:**
- Análise da interface do usuário, garantindo que fosse intuitiva e de fácil navegação, com a coleta de opiniões de usuários em potencial para realizar aprimoramentos.

Todos os testes foram satisfatórios, mostrando que o sistema funciona totalmente

# Conclusão
A implementação do sistema para a compra de passagens aéreas via comunicação TCP/IP foi um sucesso, atingindo os objetivos buscados em termos de eficiência e praticidade para os usuários. A adoção de um modelo cliente-servidor possibilitou uma interação dinâmica entre os clientes e o servidor, enquanto a lógica de concorrência assegurou a integridade dos dados em situações de acesso simultâneo. Os testes realizados confirmaram a funcionalidade do sistema e sua capacidade de operar em um cenário com múltiplos usuários. A experiência adquirida ao longo do desenvolvimento ressaltou a relevância de um design sólido de APIs, além de enfatizar a importância de considerar a escalabilidade e a segurança, essenciais em sistemas que gerenciam transações financeiras. O sistema não apenas provou ser viável do ponto de vista técnico, mas também demonstrou um grande potencial para se adaptar às exigências do mercado de aviação de baixo custo, ajudando na democratização do transporte aéreo.

# Passo a passo para a execução do código
1. Clone o repositório do github nas máquinas que utilizarão o servidor e os clientes
2. Com o docker instalado, execute o código abaixo no terminal do linux:
        cd testepblredes
        docker build -f server.Dockerfile -t tcp_server .
        docker run -p 10000:10000 --name tcp_server_container tcp_server
Isso, na máquina do servidor, iniciará o contêiner com o Docker, garantindo que a porta 10000 seja mapeada para o host.
3. Execute o arquivo client.py pelo terminal do linux ou por alguma IDE em um número máximo pré-definido de computadores (4)