Projeto MLOps: Previsão de Ações EMBR3 com LSTM - Avaliação substituta FIAP

Resumo: Este projeto demonstra a implementação de um pipeline Machine Learning (MLOps) para a previsão de séries temporais. O foco é prever o preço de abertura das ações da Embraer (EMBR3) usando uma Rede Neural Recorrente (RNN) do tipo LSTM.


Empresa (Ticker):	Embraer (EMBR3)
Algoritmo:	LSTM (Long Short-Term Memory)
Previsão:	Preço de Abertura da ação no dia seguinte.
Janela de Observação:	Os últimos 90 dias de preços de fechamento.

Componentes Chave:
 Modelo Treinado (Artefato):
 Algoritmo: LSTM, ideal para capturar dependências de longo prazo em séries temporais.

Serialização: O modelo e o MinMaxScaler foram serializados (salvos em .h5 e ajustado via CSV, respectivamente) para serem carregados diretamente na API.
Serviço de Predição (API):
Framework: Flask (Python).

Endpoint: Recebe uma requisição POST no /predict contendo exatamente 90 preços de entrada.
 Virtualização (Container):
 Ferramenta: Docker.
 Servidor: Gunicorn, usado para garantir a estabilidade e o desempenho em ambiente de produção.

Como Executar e Testar:
1. Pré-requisitos
- Python 3.x
- Docker
- pip install -r requirements.txt (Instala Flask, TensorFlow, Scikit-learn, etc.)

2. Teste Local da API
Iniciar o Servidor Flask: (O servidor deve iniciar na porta 5000, dependendo da sua configuração local.)

Fazer a Requisição (Postman/cURL):
Envie um POST para o endpoint http://localhost:5000/predict (ajuste a porta se necessário) com um corpo JSON contendo exatamente 90 preços de fechamento:
{
    "data": [
        59.97,
        59.12,
        ... (87 valores restantes) ...
        57.18 
    ]
}

É um ótimo projeto de Machine Learning Engineering! Seu trabalho de construir uma API com Flask, Docker e Cloud Run, usando LSTM para prever ações da Embraer, cobre perfeitamente os requisitos do desafio.

Com base nas informações do seu projeto e nos requisitos do desafio, preparei uma sugestão de estrutura para o seu arquivo README.md do GitHub. O objetivo é ser claro, direto e focado em MLOps, como exige o desafio.

🚀 Projeto MLOps: Previsão de Ações EMBR3 com LSTM
Este projeto demonstra a implementação completa de um pipeline de Machine Learning (MLOps) para a previsão de séries temporais. O foco é prever o preço de abertura das ações da Embraer (EMBR3) usando uma Rede Neural Recorrente (RNN) do tipo LSTM.

🎯 Objetivo do Projeto
O objetivo principal deste sistema é fornecer uma previsão robusta e acessível sobre a cotação das ações da Embraer, seguindo todos os requisitos de um desafio de MLOps.

Detalhes da Previsão
Parâmetro	Detalhe
Empresa (Ticker)	Embraer (EMBR3)
Algoritmo	LSTM (Long Short-Term Memory)
Previsão	Preço de Abertura da ação no dia seguinte.
Janela de Observação	Os últimos 90 dias de preços de fechamento.
Comparação	Acurácia testada em janeiro de 2025.

Exportar para as Planilhas
⚙️ Arquitetura do MLOps e Deploy
A estratégia de MLOps foi empregada para garantir a reprodutibilidade, escalabilidade e monitoramento do modelo em produção.


Componentes Chave:
Modelo Treinado (Artefato):


Algoritmo: LSTM, ideal para capturar dependências de longo prazo em séries temporais.


Serialização: O modelo e o MinMaxScaler foram serializados (salvos em .h5 e ajustado via CSV, respectivamente) para serem carregados diretamente na API.

Serviço de Predição (API):


Framework: Flask (Python).

Endpoint: Recebe uma requisição POST no /predict contendo exatamente 90 preços de entrada.

Virtualização (Container):


Ferramenta: Docker.

Servidor: Gunicorn, usado para garantir a estabilidade e o desempenho em ambiente de produção.

Deploy e Hospedagem:

Plataforma: Google Cloud Run. Serviço Serverless que gerencia automaticamente a escalabilidade e o ambiente.

URL da API: [INSIRA O LINK DO SEU CLOUD RUN AQUI]

Monitoramento:


Ferramentas: Google Cloud Logging e Cloud Monitoring.

Função: Acompanha logs de requisição, latência e erros (código 400 se o input não for de 90 dias, por exemplo).

💻 Como Executar e Testar
1. Pré-requisitos
Python 3.x

Docker

pip install -r requirements.txt (Instala Flask, TensorFlow, Scikit-learn, etc.)

2. Teste Local da API
Iniciar o Servidor Flask:

Bash

python API.py
(O servidor deve iniciar na porta 5000 ou 8080, dependendo da sua configuração local.)

Fazer a Requisição (Postman/cURL):
Envie um POST para o endpoint http://localhost:5000/predict (ajuste a porta se necessário) com um corpo JSON contendo exatamente 90 preços de fechamento:

JSON

{
    "data": [
        59.97,
        59.12,
        ... (87 valores restantes) ...
        57.18 
    ]
}
3. Build e Execução Docker
Construa a imagem e execute o contêiner:
