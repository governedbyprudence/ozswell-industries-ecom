from fastapi import Depends
from db.db import get_db
from models.product import Product
from schemas.product import ProductCreate
from sqlalchemy.orm import Session

from utilities.image import ImageUtil

class ProductService:

    def __init__(self, db: Session,image_util: ImageUtil):
        self.db = db
        self.image_util = image_util

    def create_product(self, product: ProductCreate, images: list =[]):
        
        # Upload images to S3
        image_dict = self.image_util.upload_images(product.sku_id, images)

        product = Product(
      name=product.name,
      sku_id=product.sku_id,
      description=product.description,
      maximum_retail_price=product.maximum_retail_price,
      sale_price_excl_tax=product.sale_price_excl_tax,
      sale_price_incl_tax=product.sale_price_incl_tax,
      specifications=product.specifications,
      is_active=product.is_active,
      out_of_stock=product.out_of_stock,
      image=image_dict
        )
        self.db.add(product)
        self.db.commit()
        self.db.refresh(product)
        return product  
    

def get_product_service(db: Session = Depends(get_db), image_util: ImageUtil = Depends(ImageUtil)):
    return ProductService(db=db, image_util=image_util)