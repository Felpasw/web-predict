import pandas as pd
import os
from sklearn.model_selection import train_test_split
from tensorflow.keras.layers import Dense
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential

def treinar_modelo_novo():
    base_dir = os.path.dirname(os.path.abspath(__file__))

    uploads_dir = os.path.join(base_dir, 'uploads')

    chp = pd.DataFrame()

    data = pd.DataFrame()

    if os.path.exists(uploads_dir):
        csv_files = [f for f in os.listdir(uploads_dir) if f.endswith('.csv')]

        if csv_files:
            file_path = os.path.join(uploads_dir, csv_files[0])

            data = pd.read_csv(file_path)
            print(f"Arquivo carregado: {file_path}")
            print(chp)
        else:
            print("Nenhum arquivo .csv encontrado no diretório uploads.")
    else:
        print(f"O diretório {uploads_dir} não existe.")

    if not chp.empty:
        print("Soma de valores ausentes por coluna:")
        print(chp.isnull().sum())

        categorical_columns = chp.select_dtypes(include=['object', 'category']).columns
        print(f"Colunas categóricas encontradas: {categorical_columns}")


        if len(categorical_columns) > 0:
            dummies = pd.get_dummies(chp[categorical_columns]).astype(int)
            print("Dummies gerados com sucesso:")
            print(dummies)
        else:
            print("Nenhuma coluna categórica encontrada para gerar dummies.")
    else:
        print("O DataFrame está vazio.")

    X = data[['median_income']]  
    y = data['median_house_value']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    model = Sequential()
    model.add(Dense(64, input_dim=X_train.shape[1], activation='relu'))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(16, activation='relu'))
    model.add(Dense(1)) 

    model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mean_absolute_error'])

    history = model.fit(X_train, y_train, epochs=100, batch_size=32, validation_split=0.2, verbose=1)

    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)

    print("Mean Squared Error (MSE):", mse)
    print("Mean Absolute Error (MAE):", mae)



    y_pred = model.predict(X_test)

    y_test_values = y_test.values

    print("Valores reais:", y_test_values[:10].flatten())
    print("Valores preditos:", y_pred[:10].flatten())


    # Salvar o modelo treinado
    model.save('modelo_mlp_median_income.h5')  # O modelo é salvo como 'modelo_mlp_median_income.h5'
