from django.shortcuts import render
from .forms import AverageForm
from keras.models import load_model
import joblib
import matplotlib
matplotlib.use('Agg')  
import pandas as pd
import matplotlib.pyplot as plt
from .model import prever_valor_usuario
from django.http import JsonResponse
import plotly.express as px
import io
from django.http import HttpResponse, JsonResponse
import os
import csv
from .upload_csv import treinar_modelo_novo


base_dir = os.path.dirname(os.path.abspath(__file__))
pathScaler = os.path.join(base_dir, "..", "webPredict", "scaler.pkl")
scaler = joblib.load(pathScaler)

path = os.path.join(base_dir, "..", "webPredict", "modelo_mlp_median_income.h5")

model = load_model(path)


def average_data_view(request):
    result = None  # Para armazenar o resultado
    error_message = None  # Para armazenar uma mensagem de erro caso ocorra

    if request.method == 'POST':
        form = AverageForm(request.POST)
        if form.is_valid():
            try:
                average_salary = form.cleaned_data['average_salary']

                predicted_value = prever_valor_usuario(average_salary)

                result = {
                    'average_salary': average_salary,
                    'predicted_value': predicted_value
                }
            except Exception as e:
                error_message = str(e)
        else:
            error_message = form.errors

    else:
        form = AverageForm()

    return render(request, 'average_form.html', {
        'form': form,
        'result': result,
        'error': error_message
    })

def analisar_csv(request):
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(base_dir, "..", "Data", "housing.csv")
    
        chp = pd.read_csv(path)
        

        categorical_columns = chp.select_dtypes(include=['object', 'category']).columns
        
        dummies = pd.get_dummies(chp[categorical_columns]).astype(int)
        
        data_without_categoricals = chp.drop(categorical_columns, axis=1)
        
        data = pd.concat([data_without_categoricals, dummies], axis=1).dropna()
        ax = data.hist(figsize=(19.2, 10.8), bins=50)
        
        plt.tight_layout()
        
        plt.savefig("grafico.png", dpi=300)
        
        
        img_buf = io.BytesIO()
        plt.savefig(img_buf, format='png')
        img_buf.seek(0) 
        plt.close()  
        
        print(f"Image size in buffer: {img_buf.getbuffer().nbytes} bytes")
        
        # Retorna a imagem como resposta HTTP
        return HttpResponse(img_buf, content_type='image/png')
    except Exception as e:
        print(f"Error: {str(e)}")
        return JsonResponse({"status": "error", "message": str(e)})
    
def mapa_casas(request):
    return render(request, 'mapa_casas.html')
   
def retrain_base(request):
    if request.method == 'POST':
        try:
            from .upload_csv import treinar_modelo_novo  # Certifique-se de que o caminho está correto
            treinar_modelo_novo()
            return JsonResponse({"status": "success", "message": "Modelo retreinado com sucesso."})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})
    return JsonResponse({"status": "error", "message": "Método inválido."})


def upload_csv(request):
    if request.method == "POST" and request.FILES.get("file"):
        csv_file = request.FILES["file"]

        if not csv_file.name.endswith('.csv'):
            return HttpResponse("Por favor, envie um arquivo CSV.")

        try:
            save_path = os.path.join(base_dir, 'uploads', csv_file.name)

            os.makedirs(os.path.dirname(save_path), exist_ok=True)

            with open(save_path, 'wb') as f:
                for chunk in csv_file.chunks():
                    f.write(chunk)

            with open(save_path, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                for row in reader:
                    print(row)

            return HttpResponse(f"Arquivo salvo e processado com sucesso em {save_path}.")
        except Exception as e:
            return HttpResponse(f"Erro ao salvar ou processar o arquivo: {e}")

