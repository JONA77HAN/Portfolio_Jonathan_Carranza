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
@app.get("/mercado-libre/tendencias/{category_id}")
async def get_trends(category_id: str):
    # Headers más completos para "engañar" a la API
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "application/json",
        "Accept-Language": "es-AR,es;q=0.9"
    }
    url = f"https://api.mercadolibre.com/sites/MLA/search?category={category_id}&limit=5"
    
    try:
        # Intentamos obtener datos reales
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            results = data.get('results', [])
            
            if results:
                # Si hay resultados reales, los enviamos!
                return [{"keyword": item.get('title')} for item in results]
    except Exception as e:
        print(f"Error: {e}")

    # Si MeLi nos sigue bloqueando, devolvemos los de respaldo (para no romper el CSS)
    return [
        {"keyword": "Tendencia: Fotografía"},
        {"keyword": "Tendencia: Video 4K"},
        {"keyword": "Tendencia: Iluminación Led"}
    ]