# Usa uma imagem base leve do Python (recomendado para deploy)
FROM python:3.10-slim

# Define a porta que o Flask/Gunicorn irá usar
EXPOSE 5000

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia e instala as dependências primeiro para otimizar a construção
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copia todos os outros arquivos do projeto (código, modelo, dados)
COPY . .

# Comando para iniciar o servidor Gunicorn (modo de produção)
# Ele aponta para o seu arquivo API.py
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "API:app"]