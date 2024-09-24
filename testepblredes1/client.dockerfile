# Usa a imagem base do Python
FROM python:3.11-slim

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia os arquivos necessários para o contêiner
COPY client.py /app/

# Exponha a porta em que o servidor irá escutar
EXPOSE 10000

# Comando para rodar o servidor
CMD ["python", "client.py"]
