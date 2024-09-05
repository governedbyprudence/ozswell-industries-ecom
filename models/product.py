from sqlalchemy import Boolean, Column, DateTime, Integer, String, Float,func
from sqlalchemy.dialects.postgresql import JSONB
from db.db import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True,autoincrement=True)
    sku_id = Column(String, index=True, nullable=False)
    name = Column(String, index=True)
    description = Column(String, nullable=False)
    maximum_retail_price = Column(Float, nullable=False)
    sale_price_excl_tax = Column(Float, nullable=False)
    sale_price_incl_tax = Column(Float, nullable=False)
    specifications = Column(JSONB,nullable=False)
    is_active = Column(Boolean, default=True)
    out_of_stock = Column(Boolean, default=False)
    image = Column(JSONB, nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    
    