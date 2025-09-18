# tests/test_main.py
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from fastapi.testclient import TestClient
from main import app

# Création d'un client de test pour simuler les requêtes HTTP
client = TestClient(app)

def test_home_status_code():
    """
    Test de la route racine "/"
    Vérifie que le statut HTTP est 200
    """
    response = client.get("/")
    assert response.status_code == 200

def test_home_content():
    """
    Test du contenu de la page d'accueil
    Vérifie que le texte de bienvenue est présent
    """
    response = client.get("/")
    assert "Bienvenue sur mon projet FastAPI" in response.text

def test_api_hello_default():
    """
    Test de la route API "/api/hello" sans paramètre
    Vérifie que le nom par défaut est utilisé
    """
    response = client.get("/api/hello")
    assert response.status_code == 200
    assert response.json() == {"message": "Bonjour Isabelle, bienvenue sur FastAPI !"}

def test_api_hello_with_name():
    """
    Test de la route API "/api/hello" avec paramètre name
    """
    response = client.get("/api/hello?name=Alice")
    assert response.status_code == 200
    assert response.json() == {"message": "Bonjour Alice, bienvenue sur FastAPI !"}
