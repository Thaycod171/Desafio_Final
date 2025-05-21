# Usar uma imagem base oficial do Python
FROM python:3.9-slim

# Definir o diretório de trabalho dentro do container
WORKDIR /app

# Copiar o arquivo de dependências para o container
COPY requirements.txt .

# Instalar as dependências da aplicação
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todos os arquivos do projeto para dentro do container
COPY . .

# Expor a porta 1313 que a API vai usar
EXPOSE 1313

# Comando para iniciar a aplicação
CMD ["python", "app.py"]
