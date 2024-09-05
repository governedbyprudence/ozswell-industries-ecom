
import json
from typing import Annotated, List
from fastapi import APIRouter, Depends, Form, UploadFile
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from db.db import get_db
from schemas.product import Product, ProductCreate
from services.products import ProductService, get_product_service

router = APIRouter(
    prefix="/products",
    tags=["products"]
)


# Add Product
@router.post("/create",response_model=None)
async def create_product_route(
    images: List[UploadFile],
    sku_id: str = Form(...),
    name: str = Form(...),
    description: str = Form(...),
    maximum_retail_price: float = Form(...),
    sale_price_excl_tax: float = Form(...),
    sale_price_incl_tax: float = Form(...),
    specifications: str = Form(...),
    product_service: ProductService = Depends(get_product_service)
):
    
    # Check if images are valid for type and size of 2 mb
    for image in images:
        if image.content_type not in ['image/jpeg', 'image/png'] or image.size > 2 * 1024 * 1024:
            return JSONResponse(content={"detail":"Invalid Image. Please upload valid images of size less than 2 mb"},status_code=400)
    
    # Decode json for specifications
    
    try:
        specifications = json.loads(specifications)
    except Exception as e:
        return JSONResponse(content={"detail":"Invalid Specification"},status_code=400)

    product = ProductCreate(sku_id=sku_id, name=name, description=description, maximum_retail_price=maximum_retail_price, sale_price_excl_tax=sale_price_excl_tax, sale_price_incl_tax=sale_price_incl_tax, specifications=specifications)
    
    product_obj = product_service.create_product(product=product, images=images)

    return {"detail": "Product created","product":product_obj.__dict__}
    