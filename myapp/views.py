from django.shortcuts import render
from .forms import AverageForm
from keras.models import load_model
import joblib
import matplotlib
matplotlib.use('Agg')  # Força o backend não interativo
import pandas as pd
import matplotlib.pyplot as plt
from .model import prever_valor_usuario
from django.http import JsonResponse
import plotly.express as px
import io
from django.http import HttpResponse, JsonResponse

# Carregar o modelo e o scaler globalmente
model = load_model("C:\\Users\\luizo\\OneDrive\\Área de Trabalho\\Projetos\\A1_House_Pricing\\modelo_mlp_median_income.h5")
scaler = joblib.load('C:\\Users\\luizo\\OneDrive\\Área de Trabalho\\Projetos\\A1_House_Pricing\\web-predict\\webPredict\\scaler.pkl')

def average_data_view(request):
    result = None  # Para armazenar o resultado
    error_message = None  # Para armazenar uma mensagem de erro caso ocorra

    if request.method == 'POST':
        form = AverageForm(request.POST)
        if form.is_valid():
            try:
                # Pega o dado de 'average_salary' do formulário
                average_salary = form.cleaned_data['average_salary']

                # Faz a previsão com o valor da renda média
                predicted_value = prever_valor_usuario(average_salary)

                # Armazenar o resultado para ser exibido no template
                result = {
                    'average_salary': average_salary,
                    'predicted_value': predicted_value
                }
            except Exception as e:
                error_message = str(e)
        else:
            # Passa os erros de validação para o template
            error_message = form.errors

    else:
        form = AverageForm()

    # Passa o formulário, o resultado (ou erro) e os erros de validação para o template
    return render(request, 'average_form.html', {
        'form': form,
        'result': result,
        'error': error_message
    })

def analisar_csv(request):
    try:
        # Lê o arquivo CSV
        chp = pd.read_csv("C:\\Users\\luizo\\OneDrive\\Área de Trabalho\\Projetos\\A1_House_Pricing\\web-predict\\Data\\housing.csv")
        
        # Identifica colunas categóricas
        categorical_columns = chp.select_dtypes(include=['object', 'category']).columns
        
        # Cria variáveis dummy para as colunas categóricas
        dummies = pd.get_dummies(chp[categorical_columns]).astype(int)
        
        # Remove as colunas categóricas originais
        data_without_categoricals = chp.drop(categorical_columns, axis=1)
        
        # Combina os dados e remove as linhas com valores ausentes
        data = pd.concat([data_without_categoricals, dummies], axis=1).dropna()
        # Criar o gráfico
        ax = data.hist(figsize=(19.2, 10.8), bins=50)
        
        # Ajustar o layout
        plt.tight_layout()
        
        # Salvar como PNG
        plt.savefig("grafico.png", dpi=300)
        
        
        # Cria um buffer de memória para armazenar a imagem
        img_buf = io.BytesIO()
        plt.savefig(img_buf, format='png')
        img_buf.seek(0)  # Reseta o ponteiro do buffer para o início
        plt.close()  # Fecha a figura do matplotlib para liberar memória
        
        # Exibe o tamanho da imagem no log
        print(f"Image size in buffer: {img_buf.getbuffer().nbytes} bytes")
        
        # Retorna a imagem como resposta HTTP
        return HttpResponse(img_buf, content_type='image/png')
    except Exception as e:
        # Caso haja um erro, retorna um JSON com a mensagem de erro
        print(f"Error: {str(e)}")
        return JsonResponse({"status": "error", "message": str(e)})
    

def mapa_casas(request):
    return render(request, 'mapa_casas.html')
