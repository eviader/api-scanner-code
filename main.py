
# Documentación oficial: https://fastapi.tiangolo.com/es/

# Instala FastAPI: pip install "fastapi[all]"

from fastapi import FastAPI
from routers import products_db

app = FastAPI()

app.include_router(products_db.router)



# Inicia el server: uvicorn main:app --reload
# Detener el server: CTRL+C
