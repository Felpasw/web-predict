import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os



  # Diretório base onde o script está localizado
    
    # Caminho relativo ao arquivo
def analisar_CSV():
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base_dir, "..", "Data", "housing.csv")
    
    chp = pd.read_csv(path)

    categorical_columns = chp.select_dtypes(include=['object', 'category']).columns

    dummies = pd.get_dummies(chp[categorical_columns]).astype(int)

    data_without_categoricals = chp.drop(categorical_columns, axis=1)

    # Combinar o DataFrame sem categóricas com os dummies
    data = pd.concat([data_without_categoricals, dummies], axis=1)
    data = data.dropna()
    
    # Criar o gráfico
    ax = data.hist(figsize=(19.2, 10.8), bins=50)
    
    # Ajustar o layout

    plt.figure(figsize = (16,10))
    sns.heatmap(data.corr(), annot = True)
    plt.tight_layout()
    
    # Salvar como PNG
    plt.savefig("grafico.png", dpi=300)


analisar_CSV()
