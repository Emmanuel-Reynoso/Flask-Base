from fastapi import FastAPI
from items.items import router as items_router  # Importa el enrutador
import uvicorn  # Importa Uvicorn

app = FastAPI()

# Incluye el enrutador
app.include_router(items_router)

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

# Bloque para ejecutar Uvicorn directamente
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

