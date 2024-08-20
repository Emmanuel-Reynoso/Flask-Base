from fastapi import FastAPI
from items.items import router as items_router  # Importa el enrutador
import uvicorn  # Importa Uvicorn

app = FastAPI()

# Incluye el enrutador
app.include_router(items_router)

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}
