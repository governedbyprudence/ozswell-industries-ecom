from fastapi import FastAPI
from routers.product import router as product_router
from db.db import engine, Base

app = FastAPI()

Base.metadata.create_all(bind=engine)


app.include_router(product_router)

@app.get("/health")
def read_health():
    return {"message": "OK"}