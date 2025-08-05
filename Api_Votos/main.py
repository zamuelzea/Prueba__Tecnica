from fastapi import FastAPI
from Models.votante import router as votante_router
from Models.candidato import router as candidato_router
from Models.voto import registrar_voto, obtener_votos, VotoIn
from Models.resultados import resultados_router 

app = FastAPI()

#Routers
app.include_router(votante_router)
app.include_router(candidato_router)
app.include_router(resultados_router)

@app.post("/votos")
def votar(voto: VotoIn):
    return registrar_voto(voto)

@app.get("/votos")
def ver_votos():
    return obtener_votos()


