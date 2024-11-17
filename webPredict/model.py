from keras.models import load_model
import joblib

# Carregar o modelo previamente treinado
model = load_model('modelo_mlp_median_income.h5')

# Carregar o scaler
scaler = joblib.load('scaler.pkl')

def prever_valor_usuario(median_income_usuario):
    # Normalizar o valor da entrada do usuário
    usuario_normalizado = scaler.transform([[median_income_usuario]])
    
    # Fazer a previsão com o modelo carregado
    valor_predito = model.predict(usuario_normalizado)
    
    return valor_predito[0][0]  # Retorna o valor predito
