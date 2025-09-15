
from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class UsuarioCreate(BaseModel):
    nome: str = Field(..., min_length=3)
    email: EmailStr
    telefone: Optional[str] = None
    endereco: Optional[str] = None

class UsuarioOut(BaseModel):
    id: int
    nome: str
    email: EmailStr
    telefone: Optional[str] = None
    endereco: Optional[str] = None
    documento_path: Optional[str] = None
    comprovante_path: Optional[str] = None
    status: str

    class Config:
        from_attributes = True
