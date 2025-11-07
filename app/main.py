# app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Importar inicialización de DB
from app.core.db import init_db

# Importar routers
from app.routers import products, users, order

# ===========================
# Crear app FastAPI
# ===========================
app = FastAPI(
    title="E-commerce Clonable API",
    description="API clonable para tiendas de eCommerce",
    version="1.0.0"
)

# ===========================
# Configuración CORS (si frontend está en otro dominio)
# ===========================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cambiar por dominios permitidos en producción
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ===========================
# Inicializar DB
# ===========================
# Esto crea todas las tablas si no existen
init_db()

# ===========================
# Incluir routers
# ===========================
app.include_router(products.router, prefix="/products", tags=["Products"])
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(order.router, prefix="/orders", tags=["Orders"])

# ===========================
# Ruta principal
# ===========================
@app.get("/")
def read_root():
    return {"message": "Bienvenido a tu E-commerce clonable"}

# ===========================
# Ejecutar con:
# uvicorn app.main:app --reload
# ===========================
