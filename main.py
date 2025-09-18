# main.py
# ------------------------------
# Fichier principal de l'application FastAPI
# ------------------------------

# Importation des modules nécessaires
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

# Création d'une instance de l'application FastAPI
# C'est l'objet principal qui gère les routes et les requêtes
app = FastAPI(
    title="Mon Projet FastAPI",
    description="Un petit projet d’exemple pour découvrir FastAPI 🚀",
    version="1.0.0"
)

# Monter le dossier static pour les fichiers CSS, JS, images
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configurer le dossier des templates HTML
templates = Jinja2Templates(directory="templates")

# ------------------------------
# Routes de l'application
# ------------------------------

# Route d'accueil ("/") qui retourne une page HTML simple
@app.get("/", response_class=HTMLResponse)
async def home():
    """
    Route principale de l'application.
    Retourne une simple page HTML avec un message de bienvenue.
    """
    return "<h1>Bienvenue sur mon projet FastAPI 🚀</h1><p>Ceci est la page d'accueil.</p>"

# Route API classique qui retourne du JSON
@app.get("/api/hello")
async def api_hello(name: str = "Isabelle"):
    """
    Route API qui accepte un paramètre `name` (par défaut = 'Isabelle').
    Retourne une réponse JSON.
    Exemple : http://127.0.0.1:8000/api/hello?name=Alice
    """
    return {"message": f"Bonjour {name}, bienvenue sur FastAPI !"}

# Route HTML utilisant un template avec paramètre optionnel
@app.get("/hello")
async def hello(request: Request, name: str = "FastAPI"):
    """
    Route qui utilise un template HTML.
    Paramètre `name` optionnel.
    Exemple : http://127.0.0.1:8000/hello?name=Alice
    """
    return templates.TemplateResponse("hello.html", {"request": request, "name": name})
