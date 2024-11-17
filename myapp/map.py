import folium
import pandas as pd
from branca.colormap import linear

def create_map():
    data = pd.read_csv("C:\\Users\\luizo\\OneDrive\\Área de Trabalho\\Projetos\\A1_House_Pricing\\web-predict\\Data\\housing.csv")

    # Criar um mapa base
    base_map = folium.Map(location=[data['latitude'].mean(), data['longitude'].mean()], zoom_start=10)

    # Configurar o gradiente de cores
    colormap = linear.YlOrRd_09.scale(data['median_house_value'].min(), data['median_house_value'].max())
    colormap.caption = "Median House Value"

    # Adicionar pontos ao mapa
    for _, row in data.iterrows():
        folium.CircleMarker(
            location=[row['latitude'], row['longitude']],
            radius=5,  # Tamanho do marcador
            color=colormap(row['median_house_value']),  # Cor baseada no valor
            fill=True,
            fill_color=colormap(row['median_house_value']),
            fill_opacity=0.7,
            popup=f"Valor da casa: ${row['median_house_value']:.2f}"
        ).add_to(base_map)

    # Adicionar a legenda de cores ao mapa
    colormap.add_to(base_map)

    # Salvar o mapa como um arquivo HTML
    base_map.save("mapa_casas.html")

    print("Mapa salvo como 'mapa_casas.html'. Abra o arquivo no navegador para visualizá-lo.")
