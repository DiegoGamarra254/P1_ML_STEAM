from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from funciones import PlayTimeGenre
from funciones import UserForGenre
from funciones import UsersRecommend
from funciones import UsersWorstDeveloper
from funciones import sentiment_analysis
from funciones import recomendacion_juego

from fastapi.responses import JSONResponse
from typing import List, Dict, Tuple, Sequence, Any, Union, Optional, Callable



app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>FastAPI Example</title>
    </head>
    <body>
        <h1>BIENVENIDOS A LA API DEL PROYECTO 1, Realizado por Diego Gamarra Rivera</h1>
        <ul>
            <li><a href="/PlayTimeGenre/Accion">Consulta PlayTimeGenre para el género Acción</a></li>
            <li><a href="/userforgenre/Accion">Consulta UserForGenre para el género Acción</a></li>
            <li><a href="/usersrecommend/2023">Consulta UsersRecommend para el año 2023</a></li>
            <li><a href="/usersworstdeveloper/2023">Consulta UsersWorstDeveloper para el año 2023</a></li>
            <li><a href="/sentiment/EA">Consulta Sentiment Analysis para el desarrollador EA</a></li>
            <li><a href="/recomendacion_juego/123">Consulta Recomendacion Juego para el ID 123</a></li>
        </ul>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)

# Endpoint para PlayTimeGenre
@app.get("/PlayTimeGenre/{genero}")
async def user(genero: str):
    result = PlayTimeGenre(genero)
    return result

# Endpoint para UserForGenre
@app.get("/userforgenre/{genero}")
def read_user_for_genre(genero: str):
    result = UserForGenre(genero)
    return result

# Endpoint para UsersRecommend
@app.get("/usersrecommend/{year}")
def read_users_recommend(year: int):
    result = UsersRecommend(year)
    return result

# Endpoint para UsersWorstDeveloper
@app.get("/usersworstdeveloper/{year}")
def read_users_worst_developer(year: int):
    result = UsersWorstDeveloper(year)
    return result

# Endpoint para sentiment_analysis
@app.get("/sentiment/{developer}")
def read_sentiment(developer: str):
    result = sentiment_analysis(developer)
    return result

# Endpoint para recomendacion_juego
@app.get("/recomendacion_juego/{id}")
def user(id: int):
    result = recomendacion_juego(id)
    return result