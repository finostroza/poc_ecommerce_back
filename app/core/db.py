# app/core/db.py

import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Carga variables desde .env
load_dotenv()

# Leer la URL completa desde la variable de entorno
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("❌ La variable DATABASE_URL no está definida en el .env")

# Motor de SQLAlchemy
engine = create_engine(DATABASE_URL)

# Sesión de base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para modelos
Base = declarative_base()

# Inicializa la base de datos
def init_db():
    from app.models import user, product, order  # importa tus modelos
    Base.metadata.create_all(bind=engine)
    print("✅ Base de datos inicializada correctamente")

# Dependencia para inyectar la sesión en los routers
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
