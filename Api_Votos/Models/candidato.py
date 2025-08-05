from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from Models.database import get_connection
import mysql.connector #Conexiones a bd

router = APIRouter()  

    #Tipo de datos del candidato
class CandidatoIn(BaseModel):
    Nombre_Candidato: str
    Partido: str

class CandidatoOut(CandidatoIn):
    Id: int
    Votos: int

    #ENDPOINTS: 

    #Inserción de candidatos
@router.post("/candidatos")
def crear_candidato(candidato: CandidatoIn):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = "INSERT INTO Candidatos (Nombre_Candidato, Partido) VALUES (%s, %s)"
        values = (candidato.Nombre_Candidato, candidato.Partido)
        cursor.execute(query, values)
        connection.commit()
        return {"mensaje": "Candidato registrado exitosamente"}
    
    #Mensaje de error
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Error al registrar candidato: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

    #Visualización de candidatos
@router.get("/candidatos")
def obtener_candidatos():
    try:
        connection = get_connection()
        cursor = connection.cursor(dictionary=True)
        query = "SELECT * FROM Candidatos"
        cursor.execute(query)
        candidatos = cursor.fetchall()
        return candidatos
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Error al obtener candidatos: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
