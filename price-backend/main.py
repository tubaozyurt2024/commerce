from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

# CORS middleware'ini ekleyin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Bu satır, frontend uygulamanızın adresini belirler
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],  # İzin verilen HTTP metotları
    allow_headers=["*"],  # İzin verilen başlıklar
)

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Fake Store API Proxy"}

# Fake Store API'den tüm ürünleri çeken endpoint
@app.get("/products")
def get_products():
    response = requests.get("https://fakestoreapi.com/products")
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to fetch products from Fake Store API"}

# Fake Store API'den tek bir ürünü çeken endpoint
@app.get("/products/{product_id}")
def get_product(product_id: int):
    response = requests.get(f"https://fakestoreapi.com/products/{product_id}")
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Failed to fetch product with ID {product_id}"}

# Ürünlerin fiyatına göre sıralama yapan endpoint
@app.get("/products-sorted")
def get_sorted_products(order: str = "asc"):
    response = requests.get("https://fakestoreapi.com/products")
    if response.status_code == 200:
        products = response.json()
        return sorted(products, key=lambda x: x["price"], reverse=(order == "desc"))
    else:
        return {"error": "Failed to fetch products"}
