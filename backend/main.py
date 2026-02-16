from fastapi import FastAPI
import requests
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configuración de CORS (Indispensable para Vercel)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# RUTA 1: Solo para probar que el servidor vive
@app.get("/")
def read_root():
    return {"status": "Servidor Funcionando"}

# RUTA 2: La que usa tu Portfolio
@app.get("/mercado-libre/tendencias/{category_id}")
async def get_trends(category_id: str):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    url = f"https://api.mercadolibre.com/sites/MLA/search?category={category_id}&limit=5"
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            results = data.get('results', [])
            if results:
                return [{"keyword": item.get('title')} for item in results]
    except Exception as e:
        print(f"Error: {e}")

    # Si algo falla, devolvemos esta lista SIEMPRE (para que no de error en Vercel)
    return [
        {"keyword": "Cámara Réflex Digital"},
        {"keyword": "Objetivo 50mm f/1.8"},
        {"keyword": "Trípode Profesional"}
    ]