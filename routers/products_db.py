# Clase en vídeo: https://youtu.be/_y9qQZXE24A?t=20480

### Users DB API ###

from fastapi import APIRouter, HTTPException, status
from db.models.products import Product
from db.schemas.product import product_schema, products_schema
from db.client import db_client
from bson import ObjectId

router = APIRouter(prefix="/products",
                   tags=["products"],
                   responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})


@router.get("/", response_model=list[Product])
async def products():
    return products_schema(db_client.products.find())


@router.get("/{id}")  # Path
async def product(id: str):
    return search_product("_id", ObjectId(id))

@router.get("/")  # Query
async def product(id: str):
    return search_product("_id", ObjectId(id))


@router.post("/", response_model=Product, status_code=status.HTTP_201_CREATED)
async def product(product: Product):
    if type(search_product("code", product.code)) == Product:
        raise HTTPException(
           status_code=status.HTTP_404_NOT_FOUND, detail="El usuario ya existe")

    try:
        product_dict = dict(product)
        del product_dict["id"]

        id = db_client.products.insert_one(product_dict).inserted_id

        new_product = product_schema(db_client.products.find_one({"_id": id}))

        return Product(**new_product)
    except:
        return {"error": "No se ah podido cargar el producto"}
# Helper

def search_product(field: str, key):

    try:
        product = db_client.products.find_one({field: key})
        return Product(**product_schema(product))
    except:
        return {"error": "No se ha encontrado el producto"}
