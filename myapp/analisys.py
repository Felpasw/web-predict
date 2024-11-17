import pandas as pd
import matplotlib.pyplot as plt

def analisar_CSV():
    # Carregar os dados
    chp = pd.read_csv("C:\\Users\\luizo\\OneDrive\\Área de Trabalho\\Projetos\\A1_House_Pricing\\web-predict\\Data\\housing.csv")
    
    # Filtrar apenas a coluna 'median_house_value'
    data = chp[['median_house_value']]
    
    # Criar o gráfico
    ax = data.hist(figsize=(19.2, 10.8), bins=50)
    
    # Ajustar o layout
    plt.tight_layout()
    
    # Salvar como PNG
    plt.savefig("grafico.png", dpi=300)
    
# Chamar a função para gerar o gráfico
analisar_CSV()
