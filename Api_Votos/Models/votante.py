from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
from Models.database import get_connection #Conexiones a bd

router = APIRouter()

    #TIpo de datos del votante
class VotanteCreate(BaseModel):
    nombre: str
    correo: EmailStr

    #Los ENDPOINTS:

    #Crea votante
@router.post("/votantes")
def crear_votante(votante: VotanteCreate):
    connection = get_connection()
    cursor = connection.cursor()

    #Verifica que el correo sea único
    try:
        cursor.execute("SELECT * FROM Votantes WHERE Correo = %s", (votante.correo,))
        if cursor.fetchone():
            raise HTTPException(status_code=400, detail="Este correo ya está registrado.")

    #Registra votante
        cursor.execute(
            "INSERT INTO Votantes (Nombre_Votante, Correo) VALUES (%s, %s)",
            (votante.nombre, votante.correo)
        )
        connection.commit()
        return {"mensaje": "Votante registrado exitosamente."}

    #Para que sea vea el error en terminal en caso de que haya
    except Exception as e:
        print(e) 
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        cursor.close()
        connection.close()

    #Muestra votantes registrados
@router.get("/votantes")
def obtener_votantes():
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    try:
        cursor.execute("SELECT * FROM Votantes")
        resultado = cursor.fetchall()
        return resultado

    #Para que se vea el error en terminal en el caso de que haya
    except Exception as e:
        print(e) 
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        cursor.close()
        connection.close()

