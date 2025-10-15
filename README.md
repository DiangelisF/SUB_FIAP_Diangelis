# Projeto MLOps: Previsão de Ações EMBR3 com LSTM - Avaliação substituta FIAP

## Resumo: Este projeto demonstra a implementação de um pipeline Machine Learning (MLOps) para a previsão de séries temporais. O foco é prever o preço de abertura das ações da Embraer (EMBR3) usando uma Rede Neural Recorrente (RNN) do tipo LSTM.


**Empresa (Ticker):	Embraer (EMBR3)**
**Algoritmo:**	LSTM (Long Short-Term Memory)
**Previsão:**	Preço de Abertura da ação no dia seguinte.
**Janela de Observação:**	Os últimos 90 dias de preços de fechamento.

**Componentes Chave:**
 Modelo Treinado (Artefato):
 Algoritmo: LSTM, ideal para capturar dependências de longo prazo em séries temporais.

### Serialização: O modelo e o MinMaxScaler foram serializados (salvos em .h5 e ajustado via CSV, respectivamente) para serem carregados diretamente na API.
Serviço de Predição (API):
Framework: Flask (Python).

### Endpoint: Recebe uma requisição POST no /predict contendo exatamente 90 preços de entrada.
 Virtualização (Container):
 Ferramenta: Docker.
 Servidor: Gunicorn, usado para garantir a estabilidade e o desempenho em ambiente de produção.

## Como Executar e Testar:
1. Pré-requisitos
- Python 3.x
- Docker
- pip install -r requirements.txt (Instala Flask, TensorFlow, Scikit-learn, etc.)

2. Teste Local da API
Iniciar o Servidor Flask: (O servidor deve iniciar na porta 5000, dependendo da sua configuração local.)

### Fazer a Requisição (Postman/cURL):
Envie um POST para o endpoint http://localhost:5000/predict (ajuste a porta se necessário) com um corpo JSON contendo exatamente 90 preços de fechamento:
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
