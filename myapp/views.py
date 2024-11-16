from django.shortcuts import render
from .forms import AverageForm

def average_data_view(request):
    result = None  # Para armazenar o resultado do processamento
    if request.method == 'POST':
        form = AverageForm(request.POST)
        if form.is_valid():
            # Pega os dados enviados
            average_price = form.cleaned_data['average_price']
            average_salary = form.cleaned_data['average_salary']

            # Processa os dados conforme necessário (exemplo: calcular a relação preço/salário)
            ratio = average_price / average_salary if average_salary != 0 else "Undefined"
            
            # Envia o resultado para o template
            result = {
                'average_price': average_price,
                'average_salary': average_salary,
                'ratio': ratio
            }
    else:
        form = AverageForm()

    return render(request, 'average_form.html', {'form': form, 'result': result})
