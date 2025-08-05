# Prueba__Tecnica
Prueba técnica de simulación de votaciones hecha por Samuel Esteban Zea Cardona usando Python y MySQL.

Pasos de ejecución:

1*Clona el repositorio

2*Instala dependencias: python -m venv venv, venv\Scripts\activate, pip install fastapi uvicorn mysql-connector-python

3*Ejecuta el Script en MySQL: para esto, haz el siguiente .env: 
DB_HOST=localhost
DB_USER=tu_usuario
DB_PASSWORD=tu_contraseña
DB_NAME=nombre_de_tu_base
DB_PORT=3306

4*Haz la conexión en Models/database.py:

import mysql.connector

def get_connection(): return mysql.connector.connect( host="localhost", user="tu_usuario_mysql", password="tu_contraseña_mysql", database="Votos_bd" ) 5* Ejecuta la API insertando lo siguiente en terminal:

uvicorn main:app --reload

6* En caso de cualquier error, inserte en la terminal los siguientes comandos en el orden indicado (De esta forma me funciono a mi):

1: .\env\Scripts\activate 2: pip install fastapi uvicorn 3: pip install pymysql sqlalchemy 4: pip install mysql-connector-python 5: pip install pydantic[email] 6: uvicorn main:app --reload

7*Accede desde el navegador con la URL:

http://127.0.0.1:8000/docs

8* Ya en el Swagger se puede hacer uso del post para insertar ya sea votantes, candidatos o votos, y ver estas inserciones en el get o en la BD de MySQL usando un select * from "tabla"
