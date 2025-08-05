from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from Models.database import get_connection
import mysql.connector #Conexiones a bd

router = APIRouter()

    #Tipo de datos del voto
class VotoIn(BaseModel):
    Id_Votante: int
    Id_Candidato: int

    #ENDPOINTS:

    #Registro de votos
def registrar_voto(voto: VotoIn):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        #Funcion para ver si la persona ya ha votado y ya esta registrada
        cursor.execute("SELECT Ha_Votado FROM Votantes WHERE Id = %s", (voto.Id_Votante,))
        resultado = cursor.fetchone()
        if not resultado:
            raise HTTPException(status_code=404, detail="Votante no encontrado")
        if resultado[0]: 
            raise HTTPException(status_code=400, detail="Este votante ya ha votado")

        
        cursor.execute("SELECT * FROM Candidatos WHERE Id = %s", (voto.Id_Candidato,))
        if not cursor.fetchone():
            raise HTTPException(status_code=404, detail="Candidato no encontrado")

        # Registro del voto
        cursor.execute(
            "INSERT INTO Votos (Id_Votante, Id_Candidato) VALUES (%s, %s)",
            (voto.Id_Votante, voto.Id_Candidato)
        )

        # Marca que el votante ya ha ejercido su voto
        cursor.execute(
            "UPDATE Votantes SET Ha_Votado = TRUE WHERE Id = %s",
            (voto.Id_Votante,)
        )

        # Funcion que incrementa votos del candidato
        cursor.execute(
            "UPDATE Candidatos SET Votos = Votos + 1 WHERE Id = %s",
            (voto.Id_Candidato,)
        )

        connection.commit()
        return {"mensaje": "Voto registrado exitosamente"}

       #Mensaje de error
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Error al registrar voto: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def obtener_votos():
    try:
        connection = get_connection()
        cursor = connection.cursor(dictionary=True)

        query = """
        SELECT V.Id, V.Id_Votante, V.Id_Candidato, C.Nombre_Candidato, Vt.Nombre_Votante
        FROM Votos V
        JOIN Candidatos C ON V.Id_Candidato = C.Id
        JOIN Votantes Vt ON V.Id_Votante = Vt.Id
        """
        cursor.execute(query)
        return cursor.fetchall()

    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Error al obtener votos: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()