from fastapi import FastAPI
import requests
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="MeLi Portfolio API")

# 1. Configuración de CORS Mejorada
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://portfolio-jonathan-carranza-scpe.vercel.app",
        "http://127.0.0.1:5500",
        "http://localhost:5500",
        "*" 
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"status": "Online", "message": "API de Portfolio vinculada a Mercado Libre"}

@app.get("/mercado-libre/tendencias/{category_id}")
async def get_trends(category_id: str):
    """Obtiene tendencias reales de MeLi"""
    url = f"https://api.mercadolibre.com/trends/MLA/{category_id}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()[:5]
    return {"error": "No se pudo conectar con MeLi"}

@app.get("/mercado-libre/producto/{item_id}")
async def get_item(item_id: str):
    """Muestra detalles técnicos de un producto específico"""
    url = f"https://api.mercadolibre.com/items/{item_id}"
    response = requests.get(url)
    return response.json()