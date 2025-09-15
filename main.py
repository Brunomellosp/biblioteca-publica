
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import database
from routers import usuarios
import os

# cria tabelas
database.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Biblioteca Pública - MVP Semana 2", version="0.1.0")

# CORS básico para testes locais
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Servir pasta de uploads para acessar os arquivos (apenas para testes)
upload_dir = os.getenv("UPLOAD_DIR", "../uploads")
if not os.path.isabs(upload_dir):
    # normalizar com base no backend/
    upload_dir = os.path.normpath(os.path.join(os.path.dirname(__file__), upload_dir))
os.makedirs(upload_dir, exist_ok=True)
app.mount("/uploads", StaticFiles(directory=upload_dir), name="uploads")

# Rotas
app.include_router(usuarios.router)

@app.get("/", tags=["Health"])
def health():
    return {"ok": True, "name": "Biblioteca Pública - MVP Semana 2"}
