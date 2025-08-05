from fastapi import APIRouter, HTTPException
from Models.database import get_connection
import mysql.connector

resultados_router = APIRouter()

@resultados_router.get("/resultados")
def obtener_resultados():
    try:
        connection = get_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Candidatos ORDER BY Votos DESC")
        resultados = cursor.fetchall()
        return resultados
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Error al obtener resultados: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

