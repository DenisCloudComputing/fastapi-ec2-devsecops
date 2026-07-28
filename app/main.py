# ============================================================
# main.py — Point d'entrée de l'API FastAPI
# ============================================================
# Ce fichier est le coeur de notre application.
# Il définit ce que fait notre serveur quand quelqu'un
# lui envoie une requête HTTP.
# ============================================================

from fastapi import FastAPI

# Création de l'application FastAPI
# C'est comme ouvrir un restaurant : on crée l'établissement
app = FastAPI(
    title="Mon API FastAPI sur EC2",
    description="Projet DevSecOps — déployé sur AWS EC2 par Denis",
    version="1.0.0"
)

# ============================================================
# ROUTE 1 — La page d'accueil de notre API
# ============================================================
# @app.get("/") signifie :
# "Quand quelqu'un fait une requête GET sur /,
#  exécute la fonction ci-dessous et renvoie son résultat"
# GET = la méthode HTTP pour "je veux lire quelque chose"
# "/" = la racine, la page d'accueil
# ============================================================
@app.get("/")
def accueil():
    return {
        "message": "Bienvenue sur l'API FastAPI de Denis !",
        "statut": "en ligne",
        "projet": "DevSecOps FastAPI sur AWS EC2"
    }

# ============================================================
# ROUTE 2 — Vérification de santé (health check)
# ============================================================
# Dans le monde DevOps, on crée toujours une route /health
# Elle permet de vérifier rapidement que l'API fonctionne.
# Les Load Balancers AWS utilisent cette route automatiquement.
# ============================================================
@app.get("/health")
def health_check():
    return {
        "statut": "ok",
        "service": "FastAPI",
        "version": "1.0.0"
    }

# ============================================================
# ROUTE 3 — Une route avec paramètre
# ============================================================
# {nom} entre accolades = une variable dans l'URL
# Si quelqu'un appelle /bonjour/Denis
# Python reçoit nom = "Denis" et peut l'utiliser
# ============================================================
@app.get("/bonjour/{nom}")
def dire_bonjour(nom: str):
    return {
        "message": f"Bonjour {nom} ! Ton API FastAPI fonctionne parfaitement.",
        "deploye_sur": "Amazon EC2 — Paris (eu-west-3)"
    }
