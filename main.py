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
@app.get("/PlayTimeGenre/{genero}", response_class=HTMLResponse)
async def user(genero: str):
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>PlayTimeGenre Result</title>
    </head>
    <body>
        <h1>PlayTimeGenre Result</h1>
        <p>Consulta para el género: {genero}</p>
        <!-- Agrega más contenido según sea necesario -->
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)

# Endpoint para UserForGenre
@app.get("/userforgenre/{genero}", response_class=HTMLResponse)
def read_user_for_genre(genero: str):
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>UserForGenre Result</title>
    </head>
    <body>
        <h1>UserForGenre Result</h1>
        <p>Consulta para el género: {genero}</p>
        <!-- Agrega más contenido según sea necesario -->
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)

# Endpoint para UsersRecommend
@app.get("/usersrecommend/{year}", response_class=HTMLResponse)
def read_users_recommend(year: int):
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>UsersRecommend Result</title>
    </head>
    <body>
        <h1>UsersRecommend Result</h1>
        <p>Consulta para el año: {year}</p>
        <!-- Agrega más contenido según sea necesario -->
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)

# Endpoint para UsersWorstDeveloper
@app.get("/usersworstdeveloper/{year}", response_class=HTMLResponse)
def read_users_worst_developer(year: int):
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>UsersWorstDeveloper Result</title>
    </head>
    <body>
        <h1>UsersWorstDeveloper Result</h1>
        <p>Consulta para el año: {year}</p>
        <!-- Agrega más contenido según sea necesario -->
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)

# Endpoint para sentiment_analysis
@app.get("/sentiment/{developer}", response_class=HTMLResponse)
def read_sentiment(developer: str):
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Sentiment Analysis Result</title>
    </head>
    <body>
        <h1>Sentiment Analysis Result</h1>
        <p>Consulta para el desarrollador: {developer}</p>
        <!-- Agrega más contenido según sea necesario -->
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)

# Endpoint para recomendacion_juego
@app.get("/recomendacion_juego/{id}", response_class=HTMLResponse)
def user(id: int):
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Recomendacion Juego Result</title>
    </head>
    <body>
        <h1>Recomendacion Juego Result</h1>
        <p>Consulta para el ID