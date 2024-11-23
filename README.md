# Analise de valores de casa da California

## Introdução

Os dados contêm informações do censo da Califórnia de 1990. Então, embora eles possam não ajudar você a prever os preços atuais de moradias como o conjunto de dados Zillow Zestimate, eles fornecem um conjunto de dados introdutório acessível para ensinar as pessoas sobre os fundamentos do aprendizado de máquina.


- Base de dados: https://www.kaggle.com/datasets/camnugent/california-housing-prices

- Dados da base:

![image](https://github.com/user-attachments/assets/89cc27d4-fcb4-42a8-b35e-da5ecabfb642)

## Manipulação de dados

- Os dados são gerenciados por meio da remoção de valores nulos e dados categóricos, garantindo maior consistência e adequação para análises posteriores.

![image](https://github.com/user-attachments/assets/212aa415-f484-414f-b46a-13b65bbd5f66)

![image](https://github.com/user-attachments/assets/0c962f81-71f4-4204-a1fe-c8e85e070413)

## Matriz de confusão

![image](https://github.com/user-attachments/assets/b4b3fb52-bdec-40d5-a67d-d57316b74c40)

- Com base nessa matriz de confusão podemos inferir que a variavel que tem maior relevancia em relação ao preço medio da casa é a renda média.

## Aplicação

![image](https://github.com/user-attachments/assets/7606b147-e320-4145-b592-e18021350b17)

- Utilizamos o valor da renda média como valor para ser usado na predição do valor da casa.

- Ao inserir o valor da renda media e clicar em fazer previsão é retornado o valor do imovel

![image](https://github.com/user-attachments/assets/a55eaa25-4af4-4a64-a192-29c57012b743)

- Ao clicar em fazer análise são mostrados diversos gráficos de distribuição.

![image](https://github.com/user-attachments/assets/40aa6254-af05-4597-94dd-4df5f00fc884)

- Ao clicar em mostrar mapa uma nova página é carregada mostrando a localização dos imoveis e também o seu valor(Quanto mais escuro mais caro)

![image](https://github.com/user-attachments/assets/fff74ea6-92a1-4755-80d2-93e44725e4b8)

**Obs: Podemos ver que os imoveis mais caros estão próximos da costa.**

## Como executar

- Para rodar execute:

`python manage.py runserver`
