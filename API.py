# Importa as bibliotecas necessárias
import os 
from flask import Flask, request, jsonify
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler
import pandas as pd

# Inicializa o Flask
app = Flask(__name__)

# Carrega o modelo e o scaler na inicialização da API
# Isso é feito uma única vez para otimizar o desempenho
MODEL = tf.keras.models.load_model('modelo_Embraer_lstm.h5')

# Em um projeto de produção, o scaler deve ser salvo junto com o modelo.
# Para este exemplo, ele será reajustado com os dados de treinamento.
df_data = pd.read_csv('embraer_treinLO.csv')
data = df_data['Close'].values.reshape(-1, 1)
SCALER = MinMaxScaler(feature_range=(0, 1))
SCALER.fit(data)


# Define a rota da API para fazer a previsão
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extrai os dados de entrada da requisição JSON
        json_data = request.json
        input_data = np.array(json_data['data']).reshape(-1, 1)

        # Verifica se a sequência de entrada tem o tamanho correto
        if len(input_data) != 90:
            return jsonify({'error': 'A entrada deve conter 90 dias de dados.'}), 400

        # Pré-processa os dados usando o scaler
        scaled_input = SCALER.transform(input_data)
        scaled_input = scaled_input.reshape(1, 90, 1)

        # Faz a predição
        prediction = MODEL.predict(scaled_input)

        # Desnormaliza a predição para o valor original
        prediction_real = SCALER.inverse_transform(prediction)[0][0]

        # Retorna a previsão como um JSON
        return jsonify({'prediction': float(prediction_real)})

    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Executa a aplicação
#if __name__ == '__main__':
    # Para rodar localmente na porta 5000
#app.run(debug=True, host='0.0.0.0', port=5000)


if __name__ == '__main__':
    #Obtém a porta do ambiente ($PORT) ou usa 5000 como fallback local
    port = int(os.environ.get('PORT', 5000))
    #port = int(os.environ.get('PORT', 8080))
app.run(host='0.0.0.0', port=port)



