from keras.models import load_model
import joblib
import os

# Carregar o modelo previamente treinado

base_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(base_dir, "..", "webPredict", "modelo_mlp_median_income.h5")

model = load_model(path)

pathScaler = os.path.join(base_dir, "..", "webPredict", "scaler.pkl")

# Carregar o scaler
scaler = joblib.load(pathScaler)

def prever_valor_usuario(median_income_usuario):
    # Normalizar o valor da entrada do usuário
    usuario_normalizado = scaler.transform([[median_income_usuario]])
    
    # Fazer a previsão com o modelo carregado
    valor_predito = model.predict(usuario_normalizado)
    
    return valor_predito[0][0]  # Retorna o valor predito
