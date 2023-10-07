
### product schema ###

def product_schema(product) -> dict:
    return {"id": str(product["_id"]),
            "code": product["code"],
            "description": product["description"],
            "stock": product["stock"],
            "value": product["value"],
            "altcode": product["altcode"]}


def products_schema(products) -> list:
    return [product_schema(product) for product in products]
