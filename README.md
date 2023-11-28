# Proyecto Individual 1 
## Machine Learning Operations (MLOps)
*Desarrollado por Diego Gamarra Rivera*

### Descripción del Proyecto
Este proyecto propone el desarrollo de 6 funciones que entreguen información específica de los datasets públicos de la plataforma Steam, para lo cual se debe ejecutar procesos de carga y transformación de datos, análisis exploratorio, creación de funciones de consulta,  implementación de modelos de Machine Learning y deploy en FastApi para que las consultas puedan ser hechas desde la web.

### Objetivo
Obtención de un Producto Mínimo Viable (MVP) que consista en el despliegue del modelo a través de una API en Render o plataformas similares
<br />

## Desarrollo <br />


### Ingeniería de Datos (ETL y EDA) <br />
Los datasets iniciales se recibieron en un formaton JSON anidado de un repositorio público se realizó la carga y exploración de los datos, revisión de datos anómalos, eliminación de duplicados, revisión de valores nulos  y vacios, revisión de tipo de datos, reemplazo de valores nulos y vacios en las columnas requeridas para las funciones, aprovechando la data limpia se realizó la busqueda de patrones e información sobre las relaciones de los datos para tener un panorama más claro al momento de hacer las recomendaciones para esto utilizamos gráficas y funciones estadísticas.<br />  
### Feature Engineering:
Se implementó la columna ` sent_an ` aplicando análisis de sentimiento a las reseñas de los usuarios aplicando las librerias NLTK y Vader_Lexicon <br />
### Desarrollo de funciones
Para generar las funciones de consulta solicitadas, he separado las columnas de interés y he tratado la información de tal modo que el producto final sean datasets condensados que contienen especificamente la información relevante, para posteriormente ser consultada a través de la API, se aplicó la misma metodología para todas las funciones<br />
### Modelos de Aprendizaje Automático <br />
Sistema de Recomendación ítem-ítem: Aplicando la similitud de coseno, y basándonos en los géneros, elaboramos un sistema de recomendación que recoge el top 5 de juegos más similares al id ingresado. (Es posible también utilizar otras caracteristicas para establecer la comparación) <br />

### Implementación de MLOps
Deploy del Modelo: Desplegué el modelo de recomendación como parte de la API. 


## Estructura del Repositorio <br /> 
Los archivos en el orden que aparecen el repositorio son:

**DESARROLLO-FUNCIONES** Contiene el archivo 'ipynb' en el que se trabajó con la información de ETL-EDA se condensó la información y se elaboraron las funciones de consulta requeridas para el proyecto<br />

**ETL-EDA (ITEMS, REVIEWS, OUTPUT)** Contiene los pasos detallados para la carga, exploración y manipulación de los datos, estos pasos producen archivos CSV que se deben cargar en la etapa de DESARROLLO-FUNCIONES.<br />

**Modelo de ML:** Contiene el código del sistema de recomendación por similitud del coseno.<br />

El resto de archivos son los requerimientos para el deploy, los archivos main y las funciones que son utilizadas para la API y los archivos de datos condensados para las consultas de la API  
<br />

## Enlaces <br />
- Enlace al video explicativo 
- Enlace a la API  https://ml-steam-api.onrender.com
- Enlace a la API/docs https://ml-steam-api.onrender.com/docs
- Enlace a los dataset originales:
 - https://drive.google.com/drive/folders/1HqBG2-sUkz_R3h1dZU5F2uAzpRn7BSpj
 - https://drive.google.com/file/d/1GPf0wEV1MNreATjIu4DqEqysgua7XzSs/view?usp=drive_link
 - https://drive.google.com/file/d/1RPGQrpxkmoWxHjmij_mnnzkZJn3shmvL/view?usp=drive_link
 - https://drive.google.com/file/d/1uZfXi0Vtfv2mnNBuzofO9XOKmSwwk744/view?usp=drive_link
 - https://docs.google.com/spreadsheets/d/1GN8bOdiRIzdRzJjo04UOjjTutqp1l_0ZJNhgSrzk-bY/edit?usp=drive_link
 
