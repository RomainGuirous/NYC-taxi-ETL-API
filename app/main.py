from fastapi import FastAPI
from app.api.kpi import router as kpi_router

#creation instance app
app = FastAPI()

# Importation du routeur KPI
# kpi_router est l'objet router défini dans kpi.py
# prefix permet de définir un préfixe d'URL pour toutes les routes du routeur
# tags permet de regrouper les routes dans la documentation Swagger
app.include_router(kpi_router, prefix= "/kpi", tags=["KPI"])

#On définit une route / (la page d’accueil) qui retourne un message.
@app.get("/")
def read_root():
    return {"message": "Bienvenue sur FastAPI!"}

@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Bonjour, {name} !"}


# http://127.0.0.1:8000/docs  pour accéder à la documentation Swagger et tester les routes.
# Pour lancer l'application, utilisez la commande suivante dans le terminal :
# uvicorn app.main:app --reload