
# Documentación oficial: https://fastapi.tiangolo.com/es/

# Instala FastAPI: pip install "fastapi[all]"

from fastapi import FastAPI
from routers import products_db
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = [''],
    allow_credentials = True,
    allow_methods=['*'],
    allow_headers=['*']
)

app.include_router(products_db.router)



# Inicia el server: uvicorn main:app --reload
# Detener el server: CTRL+C
