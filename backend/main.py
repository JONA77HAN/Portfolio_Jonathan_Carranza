from fastapi import FastAPI
import requests
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="MeLi Portfolio API")

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"status": "Online", "message": "API de Portfolio vinculada a Mercado Libre"}

# AQUÍ PEGAS EL NUEVO CÓDIGO:
@app.get("/mercado-libre/tendencias/{category_id}")
async def get_trends(category_id: str):
    """Obtiene productos reales de MeLi simulando tendencias"""
    url = f"https://api.mercadolibre.com/sites/MLA/search?category={category_id}&limit=5"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        # Mapeamos 'title' a 'keyword' para que tu script.js no tenga que cambiar
        results = [{"keyword": item['title']} for item in data.get('results', [])]
        return results
    return {"error": "No se pudo conectar con MeLi"}

@app.get("/mercado-libre/producto/{item_id}")
async def get_item(item_id: str):
    url = f"https://api.mercadolibre.com/items/{item_id}"
    response = requests.get(url)
    return response.json()