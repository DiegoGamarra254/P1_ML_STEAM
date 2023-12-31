import pandas as pd
import fastapi
from fastapi import FastAPI
import pyarrow.parquet as pq
import pickle
import numpy as np






#funcion1
def PlayTimeGenre(genero):
    playtimegenre4 = pd.read_parquet('playtimegenre4.parquet')
    genero_lower = genero.lower()

    if genero_lower not in playtimegenre4['genres'].str.lower().unique():
        return {"Género no pertenece al conjunto de datos"}

    genre_data = playtimegenre4[playtimegenre4['genres'].str.lower() == genero_lower]

    if genre_data.empty:
        return {"No hay datos disponibles para el género especificado"}

    max_year = genre_data.loc[genre_data['total_playtime'].idxmax(), 'year']
    max_year=int(max_year)

    out = {"Año de lanzamiento con más horas jugadas para genero {}".format(genero): max_year}
    return out

#funcion2

def UserForGenre(genero):
    merged_df=pd.read_parquet('usuariostime.parquet')
    if genero not in merged_df['genres'].unique():
        return {"Género no pertenece al conjunto de datos"}
    
    grouped_df = merged_df[merged_df['genres'] == genero].groupby(['user_id', 'year']).agg({'playtime_forever_h': 'sum'}).reset_index()
    playtime_list = []
    user_ids = grouped_df['user_id'].tolist()
    user_id1 = str(user_ids[0])
    
    for index, row in grouped_df.iterrows():
        playtime_dict = {
            'Año': row['year'],
            'Horas': row['playtime_forever_h']
        }
        playtime_list.append(playtime_dict)
    
    
    out={"Usuario con más horas jugadas para {}:" .format(genero) : user_id1 , "Horas jugadas":playtime_list}
    
    return out

#funcion3
def UsersRecommend(year):
    top_items_per_year1=pd.read_parquet('topitemsperyear1.parquet')
    if year not in top_items_per_year1['year'].unique():
        return {"No se tiene información respecto al año ingresado"}
    # Filter the DataFrame based on the given year
    selected_year = top_items_per_year1[top_items_per_year1['year'] == year]

    # Sort the values based on the 'binary_recommend' column in descending order
    sorted_items = selected_year.sort_values(by='binary_recommend', ascending=False)

    # Create a list of dictionaries with the desired format
    result_list = [{"Puesto {}: ".format(i+1): item_name} for i, item_name in enumerate(sorted_items['item_name'])]

    return result_list

#funcion4
def UsersWorstDeveloper(year):
    worstdev1=pd.read_parquet('worstdev1.parquet')
    if year not in worstdev1['year'].unique():
        return {"No se tiene información respecto al año ingresado"}
    # Filter the DataFrame based on the given year
    selected_year = worstdev1[worstdev1['year'] == year]

    # Sort the values based on the 'binary_recommend' column in descending order
    sorted_items = selected_year.sort_values(by='binary_recommend', ascending=False)

    # Create a list of dictionaries with the desired format
    result_list = [{"Puesto {}: ".format(i+1): developer} for i, developer in enumerate(sorted_items['developer'])]

    return result_list

#funcion5
def sentiment_analysis(developer):
    sentiment1=pd.read_parquet('sentimentfinal.parquet')
    if developer not in sentiment1['developer'].unique():
        return {"No se tiene información respecto a {}" .format(developer)}
    # Filter the DataFrame for the specified developer
    developer_data = sentiment1[sentiment1['developer'] == developer]

    # Extract the total counts for each sentiment category
    negative_count = developer_data['Negative'].values[0]
    neutral_count = developer_data['Neutral'].values[0]
    positive_count = developer_data['Positive'].values[0]

    # Create a dictionary with the desired format
    result_dict = {developer: [f"Negative = {negative_count}", f"Neutral = {neutral_count}", f"Positive = {positive_count}"]}

    return result_dict

#funcion6  
def recomendacion_juego(id):
    df_recommendation = pd.read_parquet('recommendation.parquet')
    
    # Verifica si el id está en el DataFrame
    if id in df_recommendation['id'].values:
        # Recoge las recomendaciones como una cadena
        recommendations_array = df_recommendation.loc[df_recommendation['id'] == id, 'recommendations'].iloc[0]

        # Se observo que el resultado es un array asi que convertimos el array de NumPy a una lista de Python
        recommendations_list = list(np.asarray(recommendations_array))

        return recommendations_list
    else:
        # Si el id no está presente, muestra el siguiente mensaje
        return f"No se encontraron recomendaciones para ID {id}"