
from dotenv import load_dotenv
import os

load_dotenv()  # esto carga las variables del .env

print(os.getenv("DATABASE_URL"))       # debería imprimir "ecommerce"
print(os.getenv("DB_USER"))       # debería imprimir "user"
