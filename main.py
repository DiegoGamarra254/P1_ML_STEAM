from fastapi import FastAPI
# Importa tus funciones desde funciones.py
from funciones import PlayTimeGenre
from funciones import UserForGenre
from funciones import UsersRecommend
from funciones import UsersWorstDeveloper
from funciones import sentiment_analysis
from funciones import recomendacion_juego

from fastapi.responses import JSONResponse
from typing import List, Dict, Tuple, Sequence, Any, Union, Optional, Callable



app = FastAPI()

@app.get("/")
def read_root():
    return {"mensaje": "BIENVENIDOS A LA API DEL PROYECTO 1, Realizado por Diego Gamarra Rivera"}


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