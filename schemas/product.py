from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class ProductCreate(BaseModel):
    name: str
    sku_id: str
    description: str
    maximum_retail_price: float
    sale_price_excl_tax: float
    sale_price_incl_tax: float 
    specifications: dict
    is_active: bool = True
    out_of_stock: bool = False


class Product(ProductCreate):
    id: int
    created_at: datetime
    updated_at: datetime



class ProductUpdate(BaseModel):
    name: Optional[str] = None
    sku_id: Optional[str] = None
    description: Optional[str] = None
    maximum_retail_price: Optional[float] = None
    sale_price_excl_tax: Optional[float] = None
    sale_price_incl_tax: Optional[float] = None
    specifications: Optional[dict] = None
    is_active: Optional[bool] = None
    out_of_stock: Optional[bool] = None
    image: Optional[list] = None
    description: Optional[str] = None   