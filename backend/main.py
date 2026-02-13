#logica de API

from fastapi import FastAPI
import requests
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="MeLi Portfolio API")

# Permitir que tu Frontend (HTML/JS) se conecte al Backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"status": "Online", "message": "API de Portfolio vinculada a Mercado Libre"}

@app.get("/mercado-libre/tendencias/{category_id}")
async def get_trends(category_id: str):
    """
    Obtiene tendencias reales de una categoría para mostrar en tu web.
    Ejemplo de category_id: MLA1055 (Celulares)
    """
    url = f"https://api.mercadolibre.com/trends/MLA/{category_id}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()[:5]  # Devolvemos solo las primeras 5 tendencias
    return {"error": "No se pudo conectar con MeLi"}

@app.get("/mercado-libre/producto/{item_id}")
async def get_item(item_id: str):
    """Muestra detalles técnicos de un producto específico"""
    url = f"https://api.mercadolibre.com/items/{item_id}"
    response = requests.get(url)
    return response.json()